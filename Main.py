from AudioRecorder import AudioRecorder
from TranscriptionService import TranscriptionService
from AIService import AIService
from TTSService import TTSService

recorder = AudioRecorder()
recorder.recordAudio()

transcriptionService = TranscriptionService()
transcription = transcriptionService.getTranscription()

aiService = AIService()
aiResponse = aiService.getAIResponse(transcription)

ttsService = TTSService()
ttsService.playSpeech(aiResponse)