import cv2
import logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
INPUT_DIR = BASE_DIR / "raw-images-to-detect"
INPUT_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR = BASE_DIR / "detected-images-having-face"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
image_path = INPUT_DIR.glob("**/*")
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
    for image in images:
        if not image.is_file():
            logging.warning(f"{image.name} is not a file")
            continue
        return image

def image_reader(image):
    read_image = cv2.imread(image)
    if read_image is None:
        logging.warning(f"{image.name} can't b accessed")
        return
    else:
        logging.info("Image has been read moving to scanner")
        return read_image




image_filter(image_path)
#     image = cv2.imread()
#
def face_finder(FACE_SCANNER, read_image):
    if FACE_SCANNER.is_file():
        logging.info("scanning started...")
        scanner = cv2.CascadeClassifier(FACE_SCANNER)
        face = scanner.detectMultiScale(read_image, 1.1, 4)
        return face

def face_marker(face,read_image):
    for (x, y, w, h) in face:






#
#
#
# def face_image_transfer():
#
# def main():
#
#
#
#
# if __name__ == "__main__":
#     main()