import cv2
import logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
INPUT_DIR = BASE_DIR / "raw-images-to-detect"
INPUT_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR = BASE_DIR / "detected-images-having-face"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
FACE_SCANNER = BASE_DIR / "faces.xml"
FILE_LOG = BASE_DIR / "app.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(FILE_LOG),
        logging.StreamHandler()
    ]
)


def image_filter(images):
    list_of_images = []
    for image in images:
        if not image.is_file():
            logging.warning(f"{image.name} is not a file")
            continue
        list_of_images.append(image)
    if len(list_of_images) == 0:
        logging.warning("No files/images found")
        return
    logging.info(f"Images moving to scanner.....")
    return list_of_images

def face_image_finder(images, FACE_SCANNER):
    if not FACE_SCANNER.is_file():
        logging.error(f"The scanner file{FACE_SCANNER.name} is not a file")
        return

    scanner = cv2.CascadeClassifier(FACE_SCANNER.name)
    for image in images:
        read_image = cv2.imread(image)
        if read_image is None:
            logging.warning(f"{image.name} can't be read. Most likely not an image or it's a corrupted image")
            continue
        else:
            logging.info(f"{image.name} has been read successfully, about to be scanned.")

            face = scanner.detectMultiScale(read_image, 1.1, 4)
            if len(face) >= 1:
                cv2.imwrite(OUTPUT_DIR / image.name, read_image)
                logging.info(f"{image.name} has been scanned, and face has been detected. It has been added to the {OUTPUT_DIR.name} directory.")
            else:
                logging.warning(f"{image.name} has been scanned, and No face was detected. Moving to the next image.")
                continue



def main():
    logging.info("Face scanning started...")
    image_path = INPUT_DIR.glob("**/*")
    filtered_image = image_filter(image_path)
    face_image_finder(filtered_image, FACE_SCANNER)
    logging.info(f"Scanning Complete! find detected images in {OUTPUT_DIR.name}")



if __name__ == "__main__":
    main()