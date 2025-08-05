import os

images_path = "dataset/images"
labels_path = "dataset/labels"

image_files = set(f.split('.')[0] for f in os.listdir(images_path) if f.endswith(".jpg"))
label_files = set(f.split('.')[0] for f in os.listdir(labels_path) if f.endswith(".txt"))

print("Images without labels:", image_files - label_files)
print("Labels without images:", label_files - image_files)
