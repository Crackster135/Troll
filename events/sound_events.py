import random
import sounddevice as sd
import soundfile as sf
import numpy as np

import os

directory = "events/media/audio/"

files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def add_distortion(audio, gain=1.0, threshold=0.5):
    # Apply gain
    audio = audio * gain

    # Clip the signal
    audio = np.clip(audio, -threshold, threshold)

    return audio

def play_distorted_audio(file_path, gain=2.0, threshold=0.5):
    # Load the audio file
    audio, fs = sf.read(file_path, dtype='float32')

    # Add distortion to the audio
    distorted_audio = add_distortion(audio, gain=gain, threshold=threshold)

    # Set the buffer size
    buffer_size = 1024  # Increase this value if underrun still occurs

    # Play the distorted audio using OutputStream for more control
    with sd.OutputStream(samplerate=fs, channels=distorted_audio.shape[1], blocksize=buffer_size) as stream:
        stream.write(distorted_audio)

def play_random_sound():
    play_distorted_audio(directory + files[random.randint(0, len(files) - 1)], gain=random.randint(900, 1000), threshold=0.5)

