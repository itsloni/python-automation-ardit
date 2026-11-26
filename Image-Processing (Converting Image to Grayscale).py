# Open cv is a Python library that is used for computer vision, image processing, capturing video, detecting objects in images and in video
# in this file you are converting colored jpeg images to grayscale.
# Note:  'opencv' is installed by typing 'opencv-python' but imported and 'cv2' note that!
# Note: 'opencv' is based on Numpy. and Numpy is a python library used for numerical calculations using 2D and 3D matrixes
# Note When you think of an image you know it's made of pixels, but each pixel is associated with a number , a value from 0-255
import cv2
#cv2.rectangle() -----> You can draw a rectangle on an image.
color = cv2.imread("galaxy.jpeg", 0) # Note: The '.imread()' means image read so to read an image. The 1 is a flag and it means load the image in color and 0 is a flag meaning getting it in grey scale.
#print(color)                        # This shows you the complex structure of the image as it is made up of matrices.
#but if you want to see the dimension of the image you simply use the method '.ndim'
print(color.ndim)                   # Which will be 3 cause image is made of 3 matrices and the image we are viewing is just a single image

#Now we want to generate the image in grey scale we use the method '.imwrite()' which is used to convert to grey scale and also as shown below:

cv2.imwrite("New-grey-scale-image.jpeg", color) # So teh first string is the name of the new file image that will be created and the other argument is the .imread image file. NOTE:! To convert to gray scale you must make the .imread() argument 0 not 1 !!




