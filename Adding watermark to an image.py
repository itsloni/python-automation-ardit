import cv2

image = cv2.imread("elfs.jpeg")
image = cv2.imread("watermark.png")

# To place an image in an image you use a method in cv2 called add it works by blending the images together and you
# can specify the position in the image the watermark will go. Hence, you will need to find the coordinate of that
# location in rhe image. and in an image the coordinate asper (0,0) always starts at th upper left corner!
