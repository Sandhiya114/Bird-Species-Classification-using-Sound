import kagglehub

# Download Bird Image Dataset
image_dataset_path = kagglehub.dataset_download("gpiosenka/birdies")

# Download Bird Audio Dataset
audio_dataset_path = kagglehub.dataset_download("soumendraprasad/sound-of-114-species-of-birds-till-2022")

print("Image Dataset Path:", image_dataset_path)
print("Audio Dataset Path:", audio_dataset_path)
