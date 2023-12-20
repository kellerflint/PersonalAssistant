import azure.cognitiveservices.speech as speechsdk
from Config import SPEECH_SERVICE_KEY, SPEECH_SERVICE_REGION, OUTPUT_FILE
import time

class SpeechService:
    def __init__(self):
        # Set the speech recognition configuration
        self.speechConfig = speechsdk.SpeechConfig(subscription=SPEECH_SERVICE_KEY, region=SPEECH_SERVICE_REGION)
        self.audioConfig = speechsdk.audio.AudioConfig(filename=OUTPUT_FILE)
        self.speechRecognizer = speechsdk.SpeechRecognizer(speech_config=self.speechConfig, audio_config=self.audioConfig)

        # Set the speech synthesis configuration
        self.speechConfig.speech_synthesis_voice_name = "en-US-JennyNeural"
        self.speechConfig.set_speech_synthesis_output_format(speechsdk.SpeechSynthesisOutputFormat.Riff24Khz16BitMonoPcm)
        self.speechSynthesizer = speechsdk.SpeechSynthesizer(speech_config=self.speechConfig)

    def playSpeech(self, inputText):
        print(f"Playing speech on {inputText}.")
        result = self.speechSynthesizer.speak_text_async(inputText).get()

        # Play the synthesized audio
        audioStream = speechsdk.AudioDataStream(result)
        
    def getTranscription(self):
        print("Getting transcription...")
        done = False
        transcriptions = []

        def stop_cb(evt):
            """callback that stops continuous recognition upon receiving an event `evt`"""
            print('CLOSING on {}'.format(evt))
            nonlocal done
            done = True

        def recognized_cb(evt):
            """callback that is called when speech is recognized"""
            print('RECOGNIZED: {}'.format(evt))
            nonlocal transcriptions
            transcriptions.append(evt.result.text)

        self.speechRecognizer.recognized.connect(recognized_cb)
        self.speechRecognizer.session_stopped.connect(stop_cb)

        # Start continuous speech recognition
        self.speechRecognizer.start_continuous_recognition()
        while not done:
            time.sleep(.5)

        self.speechRecognizer.stop_continuous_recognition()

        # Join all transcriptions into a single string
        transcription_text = " ".join(transcriptions)

        # Specify the file path
        output_file_path = "transcription.txt"

        # Write the transcription to the file
        with open(output_file_path, "w") as file:
            file.write(transcription_text)

        print(f"Transcription written to {output_file_path}.")

        return transcription_text