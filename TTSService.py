import azure.cognitiveservices.speech as speechsdk
from Config import SPEECH_SERVICE_KEY, SPEECH_SERVICE_REGION

class TTSService:
    def __init__(self):
        self.speechConfig = speechsdk.SpeechConfig(subscription=SPEECH_SERVICE_KEY, region=SPEECH_SERVICE_REGION)
        self.speechConfig.speech_synthesis_voice_name = "en-US-JennyNeural"
        self.speechConfig.set_speech_synthesis_output_format(speechsdk.SpeechSynthesisOutputFormat.Riff24Khz16BitMonoPcm)
        self.speechSynthesizer = speechsdk.SpeechSynthesizer(speech_config=self.speechConfig)

    def playSpeech(self, inputText):
        print(f"Playing speech on {inputText}.")
        result = self.speechSynthesizer.speak_text_async(inputText).get()

        # Play the synthesized audio
        audioStream = speechsdk.AudioDataStream(result)