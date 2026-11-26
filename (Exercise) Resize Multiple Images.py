import cv2
from pathlib import Path

images_folder_path = Path("images")
images_path = images_folder_path.glob("**/*")
print(images_folder_path)
print(images_path)
resized_image_folder = Path("Resized-Images")
# NOTE: IMPORTANT INFOR ABOUT PATHLI library:
# .mkdir() - A pathlib method that creates a new folder at the specified path.
#   parents=True  -> Automatically creates any missing parent/outer folders in the path (e.g., "Projects/Images/Resized") instead of crashing with FileNotFoundError.
#   exist_ok=True -> Prevents Python from crashing with FileExistsError if the folder already exists; it just skips creation and moves on.
# resized_image_folder.mkdir(parents=True, exist_ok=True)

def calculate_image(scale_percentage, height, width):
    new_width = int(scale_percentage * width / 100)
    new_height = int(scale_percentage * height / 100)
    return (new_width, new_height)

def resize_image(image_path, scale_percentage, resized_image_path):
    for image in image_path:
        print(image.name)
        old_sized_image = cv2.imread(image)
        new_dimension = calculate_image(scale_percentage, old_sized_image.shape[0], old_sized_image.shape[1])
        print(new_dimension)
        resized_image = cv2.resize(old_sized_image, new_dimension)
        cv2.imwrite(f"{resized_image_path}/{image.name}", resized_image)

resize_image(images_path, 10, resized_image_folder)

