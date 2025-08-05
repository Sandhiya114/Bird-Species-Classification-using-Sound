import librosa

# Define the sample audio file path
sample_file = r"C:\Users\shalini\.cache\kagglehub\datasets\soumendraprasad\sound-of-114-species-of-birds-till-2022\versions\1\Voice of Birds\Voice of Birds\Andean Guan_sound\Andean Guan_01.mp3"

# Try loading the audio file
try:
    audio, sr = librosa.load(sample_file, sr=None)
    print("Audio loaded successfully!")
    print("Sample Rate:", sr)
    print("Audio shape:", audio.shape)
except Exception as e:
    print("Error loading audio file:", e)
