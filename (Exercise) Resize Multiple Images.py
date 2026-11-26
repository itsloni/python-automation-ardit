import cv2
from pathlib import Path

images_folder_path = Path("images")
images_path = images_folder_path.glob("**/*")
resized_image_folder = Path("Resized-Images")

def calculate_image(scale_percentage, height, width):
    new_width = int(scale_percentage * width / 100)
    new_height = int(scale_percentage * height / 100)
    return (new_height, new_width)

def resize_image(image_path, scale_percentage, resized_image_path):
    for image in image_path:
        old_sized_image = cv2.imread(image)
        resized_image = cv2.resize(calculate_image(scale_percentage, old_sized_image.shape[0], old_sized_image.shape[1]))
        cv2.imwrite(resized_image_path, resized_image)



