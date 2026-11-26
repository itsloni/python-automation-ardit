import cv2
from pathlib import Path

def calculate_image(scale_percentage, height, width):
    new_width = int(scale_percentage * width / 100)
    new_height = int(scale_percentage * height / 100)
    return (new_width, new_height)

def resize_image(image_path, scale_percentage, resized_image_path):

