import azure.cognitiveservices.speech as speechsdk
from Config import SPEECH_SERVICE_KEY, SPEECH_SERVICE_REGION, OUTPUT_FILE

class TranscriptionService:
    def __init__(self):
        self.speechConfig = speechsdk.SpeechConfig(subscription=SPEECH_SERVICE_KEY, region=SPEECH_SERVICE_REGION)
        self.audioConfig = speechsdk.audio.AudioConfig(filename=OUTPUT_FILE)
        self.speechRecognizer = speechsdk.SpeechRecognizer(speech_config=self.speechConfig, audio_config=self.audioConfig)


    def getTranscription(self):
        print("Getting transcription...")
        result = self.speechRecognizer.recognize_once()
        return result.text