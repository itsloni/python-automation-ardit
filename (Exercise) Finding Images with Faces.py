import cv2
import logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
INPUT_DIR = BASE_DIR / "raw-images-to-detect"
INPUT_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR = BASE_DIR / "detected-images-having-face"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
image_path = INPUT_DIR.glob("**/*")
FILE_LOG = BASE_DIR / "app.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(FILE_LOG),
        logging.StreamHandler()
    ]
)


def face_finder():



def face_image_transfer():

def main():




if __name__ == "__main__":
    main()