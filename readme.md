# Install

Run:
```bash
pip install pyaudio openai azure-cognitiveservices-speech
```

Create a Config.py file with the following:
```python
OPENAI_API_KEY='your-openai-key'
SPEECH_SERVICE_KEY='your-speech-service-key'
SPEECH_SERVICE_REGION='your-speech-service-region'
OUTPUT_FILE='output.wav'
PROMPT='whatever you want open AI to do with your transcription'
```

For the prompt, you could use something as simple as "Make the following voice transcription readable." But you can play with that to get better results, ask it to summarize, etc.

# How to use

Since this is scuffed as hell, you need to move the audio file you want into the project folder and rename it to "output". The output file must be in the .wav format. If it not already you can use a converter like https://cloudconvert.com/m4a-to-wav

Then run:
```bash
python Main.py 
```

The direct transcription will be in the transcription.txt file. The output from OpenAI will be in the output.txt file. Each time you run this it will overwrite the previous transcription and output so make sure you save them somewhere (maybe with Obsidian, it should be good for this use case).