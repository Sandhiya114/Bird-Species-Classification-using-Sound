import os
import librosa

# Define the path to one sample audio file
sample_file = r"C:\Users\shalini\.cache\kagglehub\datasets\soumendraprasad\sound-of-114-species-of-birds-till-2022\versions\1\Voice of Birds\Voice of Birds\Andean Guan_sound\Andean Guan10.mp3"

# Check if the file exists
if os.path.isfile(sample_file):
    print("Found the sample file:", sample_file)
    try:
        # Load the audio file
        audio, sr = librosa.load(sample_file, sr=None)
        print("Audio loaded successfully!")
        print("Sample Rate:", sr)
        print("Audio shape:", audio.shape)
    except Exception as e:
        print("Error loading audio file:", e)
else:
    print("File not found. Please verify the file path and name.")
