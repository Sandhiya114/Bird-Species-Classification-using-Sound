from audio_preprocessing import extract_mfcc

# Specify the path to one of your audio files.
sample_file = r"C:\Users\shalini\.cache\kagglehub\datasets\soumendraprasad\sound-of-114-species-of-birds-till-2022\versions\1\Voice of Birds\Voice of Birds\Andean Tinamou_sound\Andean Tinamou10.mp3"

# Extract MFCC features
features = extract_mfcc(sample_file)
print("Extracted MFCC features:", features)
