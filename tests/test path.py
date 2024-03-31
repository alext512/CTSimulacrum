import os

image_path = r"C:\Obsidian\My Notes\Radiology\Virtual CT Scanner\CTSimulacrum\resources\fruits00000\fruits00001.png"  # Use the raw string

if os.path.exists(image_path):
    print("The path "+ image_path +" is correct, and the image exists.")
else:
    print("The path "+ image_path +" is incorrect, or the image is inaccessible.")
