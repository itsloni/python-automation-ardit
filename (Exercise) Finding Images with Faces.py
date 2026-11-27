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
    #print(list_of_images)
    return list_of_images

def image_reader(images, FACE_SCANNER):
    print(FACE_SCANNER)
    print(FACE_SCANNER.name)
    if not FACE_SCANNER.is_file():
        logging.error(f"The scanner file{FACE_SCANNER.name} is not a file")
        return

    scanner = cv2.CascadeClassifier(FACE_SCANNER.name)
    for image in images:
        read_image = cv2.imread(image)
        if read_image is None:
            logging.warning(f"{image.name} can't be accessed")
            continue
        else:
            logging.info("Image has been read moving to scanner")
            logging.info("scanning started...")

            face = scanner.detectMultiScale(read_image, 1.1, 4)
            print(face)
            if len(face) >= 1:
                cv2.imwrite(OUTPUT_DIR / image.name, read_image)

    #print(list_of_read_images)


#
# def face_finder(FACE_SCANNER, read_images, filtered_images):
#     #print(read_images)
#     for read_image in read_images:
#         # for filtered in filtered_images:
#         if FACE_SCANNER.is_file():
#             logging.info("scanning started...")
#             scanner = cv2.CascadeClassifier(FACE_SCANNER.name)
#             face = scanner.detectMultiScale(read_image, 1.1, 4)
#             cv2.imwrite(OUTPUT_DIR / image.name , read_image)
#             print(face)
                #     print(f"{filtered.name} is has no face")
                #     continue
                # else:
                #     cv2.imwrite(OUTPUT_DIR / filtered.name, read_image)



                 # print(read_image)



# def face_image_transfer(face, read_image):
#     new_path = cv2.imwrite(OUTPUT_DIR / )


# def face_marker(face,read_image):
#     for (x, y, w, h) in face:
#        cv2.rectangle(read_image, (x, y), (x+w, y+h), (255, 255, 255), 4)
#     if not cv2.imwrite(OUTPUT_DIR / read_image.name, read_image):
#        return

def main():
    image_path = INPUT_DIR.glob("**/*")
    filtered_image = image_filter(image_path)
    image_reader(filtered_image, FACE_SCANNER)
    # face_finder(FACE_SCANNER, read_image, filtered_image)



if __name__ == "__main__":
    main()