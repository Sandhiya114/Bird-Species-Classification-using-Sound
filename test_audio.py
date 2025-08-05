import os
import librosa

# Update the sample file path with an existing file
sample_file = r"C:\Users\shalini\.cache\kagglehub\datasets\soumendraprasad\sound-of-114-species-of-birds-till-2022\versions\1\Voice of Birds\Voice of Birds\Andean Tinamou_sound\Andean Tinamou10.mp3"

print("The sample file is:", sample_file)

if os.path.isfile(sample_file):
    print("File found!")
    try:
        audio, sr = librosa.load(sample_file, sr=22050)
        print("Audio loaded successfully!")
        print("Sample Rate:", sr)
        print("Audio shape:", audio.shape)
    except Exception as e:
        print("Error loading audio file:", e)
else:
    print("File not found. Please verify the file path and name.")
