import cv2
from pathlib import Path

images_folder_path = Path("images")
images_path = images_folder_path.glob("**/*")
new_greyscale_images = Path("greyscale-images")

for image in images_path:
    greyscale = cv2.imread(image, 0)
    cv2.imwrite(f"{new_greyscale_images}/{image.stem}_greyscale_{image.suffix}", greyscale)

# ANOTHER WAY TO DO THE EXERCISE WHICH MY TUTOR GAVE ME IS:
# Using import os and it's method called os.listdir("directory path")

import os
images = os.listdir("images")
for image in images:
    grey = cv2.imread(f"images/{image}", 0)
    cv2.imwrite(f"checker/greyscale_{image}", grey)
