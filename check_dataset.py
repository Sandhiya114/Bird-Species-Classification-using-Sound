import os
dataset_path = "C:/Users/shalini/Documents/Bird-Sound-Classification-main/dataset"
# Check if the dataset folder exists
if os.path.exists(dataset_path):
    print("Dataset folder found. Listing contents:")
    print(os.listdir(dataset_path))
else:
    print(" Dataset folder not found! Please check the path.")
