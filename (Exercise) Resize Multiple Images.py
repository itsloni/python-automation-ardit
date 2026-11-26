import cv2
import logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
INPUT_DIR = BASE_DIR / "images"
OUTPUT_DIR = BASE_DIR / "Resized-Images"
LOG_FILE = BASE_DIR / "app.log"

logging.basicConfig(
    level=logging.INFO,
    format= "%(asctime)s-%(levelname)s-%(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

def calculate_image(scale_percentage, height, width):
    logging.info("Calculating new image size...")
    new_width = int(scale_percentage * width / 100)
    new_height = int(scale_percentage * height / 100)
    return (new_width, new_height)

def resize_image(image_path, scale_percentage, resized_image_path):
    logging.info("Resizing the image...")
    if not INPUT_DIR.exists():
        logging.error("Directory does not exist")
        return None
    for image in image_path:
        if not image.is_file():
            logging.warning(f"{image.name} is not a file, skipping {image.name}")
            continue
        old_sized_image = cv2.imread(image)
        if old_sized_image is None:
            logging.warning(f"{image.name} is not supported or is corrupted")
            continue
        new_dimension = calculate_image(scale_percentage, old_sized_image.shape[0], old_sized_image.shape[1])
        resized_image = cv2.resize(old_sized_image, new_dimension)

        if cv2.imwrite(f"{resized_image_path}/{image.name}", resized_image):
            logging.info(f"Resized {image.name} to {new_dimension}")
        else:
            logging.error(f"Am error has occurred and {image.name} cannot be resized")

def main():
    logging.info("starting image resizing.....")
    if not INPUT_DIR.exists():
        logging.error("Input directory does not exist")
        return
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    images_path = INPUT_DIR.glob("**/*")
    resize_image(images_path, 10, OUTPUT_DIR)
    logging.info("Image resizing complete")


if __name__ == "__main__":
    main()








# NOTE: IMPORTANT INFOR ABOUT PATHLI library:
# .mkdir() - A pathlib method that creates a new folder at the specified path.
#   parents=True  -> Automatically creates any missing parent/outer folders in the path (e.g., "Projects/Images/Resized") instead of crashing with FileNotFoundError.
#   exist_ok=True -> Prevents Python from crashing with FileExistsError if the folder already exists; it just skips creation and moves on.
# resized_image_folder.mkdir(parents=True, exist_ok=True)
