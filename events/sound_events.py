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

# Example usage
play_distorted_audio('/home/troll/Documents/Troll/Troll-1/events/media/audio/bruh.wav', gain=2.0, threshold=0.5)