import sounddevice as sd
import soundfile as sf
import numpy as np

def add_distortion(audio, gain=1.0, threshold=0.5):
    """
    Apply distortion to the audio signal.

    :param audio: NumPy array containing audio data
    :param gain: Gain factor to amplify the signal
    :param threshold: Threshold for clipping
    :return: Distorted audio signal
    """
    # Apply gain
    audio = audio * gain

    # Clip the signal
    audio = np.clip(audio, -threshold, threshold)

    return audio

# Load the audio file
file_path = 'path/to/your/soundfile.wav'
audio, fs = sf.read(file_path, dtype='float32')

# Add distortion to the audio
distorted_audio = add_distortion(audio, gain=2.0, threshold=0.5)

# Play the distorted audio
sd.play(distorted_audio, fs)
sd.wait()  # Wait until the sound has finished playing
