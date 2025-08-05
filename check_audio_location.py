import os
import librosa

# Define the full path to the nested audio folder
audio_folder = r"C:\Users\shalini\.cache\kagglehub\datasets\soumendraprasad\sound-of-114-species-of-birds-till-2022\versions\1\Voice of Birds\Voice of Birds"

# List all files in the folder
try:
    files = os.listdir(audio_folder)
    print("Files in audio folder:")
    for f in files:
        print(f)
except Exception as e:
    print("Error accessing the folder:", e)

# If files exist, load a sample file to verify its contents
if files:
    sample_file = os.path.join(audio_folder, files[0])
    print("\nLoading sample audio file:", sample_file)
    try:
        audio, sr = librosa.load(sample_file, sr=None)
        print("Sample Rate:", sr)
        print("Audio shape:", audio.shape)
    except Exception as e:
        print("Error loading audio file:", e)
else:
    print("No files found in the audio folder.")
