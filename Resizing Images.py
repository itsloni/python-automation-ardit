import cv2

# image = cv2.imread("galaxy.jpeg")
# print(image.shape)  #Using the '.shape' will give you an output like e.g: (779, 438, 3) where the Height is the
# first number, width is the second number, and the last number shows the number of matrices which is usually 3 for
# colored pictures and 2 for greyscaled images.

# When you want to calculate the new dimension you want to give it, like changing (779, 438, 3) particularly the
# first 2 numbers (height and width)to another size
#We create a function as below:

def calculate_size(scale_percentage, width, height): #Note that the parameter 'scale_percentage' is the scale by which we
    # want to reduce teh width/height. So if we set scale_percentage to 10 percent then we say 10 percent of the width is
    # what we want as the new width as you can see below in the function.
    new_width = int(width * scale_percentage / 100)
    new_height = int(height * scale_percentage / 100)
    return (new_width, new_height)


def resize_image(image_path, scale_percentage, resized_path):
    image = cv2.imread(image_path)
    new_dimension = calculate_size(scale_percentage, image.shape[1], image.shape[0])
    resized_image = cv2.resize(image, new_dimension)
    cv2.imwrite(resized_path, resized_image)

resize_image("galaxy.jpeg", 10, "resized-galaxy.jpeg")

