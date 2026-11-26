import cv2
from pathlib import Path

images_folder_path = Path("images")
images_path = images_folder_path.glob("**/*")
new_greyscale_images = Path("greyscale-images")

for image in images_path:
    greyscale = cv2.imread(image, 0)
    cv2.imwrite(f"{new_greyscale_images}/{image.stem}_greyscale_{image.suffix}", greyscale)

