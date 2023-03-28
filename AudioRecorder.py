import pyaudio
import wave
from Config import OUTPUT_FILE

class AudioRecorder:
    def __init__(self):
        # Set the audio format
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100
        self.CHUNK = 1024

        # Create a PyAudio object
        self.pAudio = pyaudio.PyAudio()
        self.deviceIndex = 2

    def recordAudio(self):
        # Open a stream to record audio from the microphone
        stream = self.pAudio.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True, input_device_index=self.deviceIndex, frames_per_buffer=self.CHUNK)

        # Record audio for a certain duration
        print("Recording...")
        frames = []
        for i in range(0, int(self.RATE / self.CHUNK * 5)):
            data = stream.read(self.CHUNK)
            frames.append(data)

        # Stop recording and close the stream
        print("Done recording.")
        stream.stop_stream()
        stream.close()
        self.pAudio.terminate()

        # Save the recorded audio to a WAV file
        waveFile = wave.open(OUTPUT_FILE, 'wb')
        waveFile.setnchannels(self.CHANNELS)
        waveFile.setsampwidth(self.pAudio.get_sample_size(self.FORMAT))
        waveFile.setframerate(self.RATE)
        waveFile.writeframes(b''.join(frames))
        waveFile.close()
    
    def setAudioDevice(self):
        # Get the list of audio devices
        info = audio.get_host_api_info_by_index(0)
        numDevices = info.get('deviceCount')
        devices = [audio.get_device_info_by_host_api_device_index(0, i) for i in range(numDevices)]

        # Print the list of audio devices
        for i, device in enumerate(devices):
            print(f"{i}: {device['name']}")

        # Choose the audio device to use
        self.deviceIndex = int(input("Enter the device index: "))