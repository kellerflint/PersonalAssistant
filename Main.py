from AudioRecorder import AudioRecorder
from SpeechService import SpeechService
from AIService import AIService


recorder = AudioRecorder()
speechService = SpeechService()
aiService = AIService()

# to have it record from the mic, uncomment
#recorder.recordAudio()

transcription = speechService.getTranscription()

aiResponse = aiService.getAIResponse(transcription)

# To have it read the transcription aloud, uncomment
#speechService.playSpeech(aiResponse)



# Do the senior memeroy book thing but better. Have AI take natural languague. The person just clicks record and tell a story or thing. Then the AI transcribs it. The AI summarizes it. And AI goes through and without changing the words, just fixes up the text so it's more readable, better formatted for the story. Then they can go through and edit it if they want to.
# Could guide with various prompts. AI can ask intellegent follow up questions.

# Make a sylabbas chat bot for teachers. Make it easy to use and gerealizable so instructors can easilty input a few things and have their own. Integrate it with Canvas. Make it so students can ask it questions about the course. Could have it add other stuff too like office hours, contact info, class times, grading/late policies, dates assignments are due (maybe use canvas info on the actual page to train) and such.
