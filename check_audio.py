import os

# Path to your downloaded Xeno-Canto audio dataset
audio_folder = "dataset/audio"

# List all audio files
audio_files = os.listdir(audio_folder)

# Print the first 10 files
print("First 10 audio files:", audio_files[:10])
