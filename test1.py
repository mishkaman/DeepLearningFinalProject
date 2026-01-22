import os

# Path to your image folder
folder_path = 'Images'

# List all files in the folder
all_files = os.listdir(folder_path)

# Filter for common image extensions
image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')
image_files = [f for f in all_files if f.lower().endswith(image_extensions)]

print(f"Number of images in the folder: {len(image_files)}")
