import cv2

image = cv2.imread("elfs.jpeg")
watermark_image = cv2.imread("watermark.png")

# To place an image in an image you use a method in cv2 called '.addWeighte()'[ it works by blending the images together and you
# can specify the position in the image the watermark will go. Hence, you will need to find the coordinate of that
# location in the image. and in an image the coordinate asper (0,0) always starts at th upper left corner!
# So FIRST you get teh shape of the image using the '.shape' so you get the height and width respectively.

print(watermark_image.shape)

x = image.shape[1] - watermark_image.shape[1]
y = image.shape[0] - watermark_image.shape[0]
print(x, y)

# QUICK TIP: to kinda cut out a specific section of an image you do belo. this tip btw is just to make you
# understand how the watermark will be pasted in a section of the image or blended rather.
watermark_place = image[y:, x:] # Note however this line is necessary to add watermark cause with the size of the watermark you
# carve out the exact size from teh image and then that carved image from teh images is now blended alone with the watermark
cv2.imwrite("tested_elf.jpeg", watermark_place)

blended_image = cv2.addWeighted(watermark_place,0.4, watermark_image,0.4, 0)#first variable is the image that is the section of the main image but the size of teh watermark image, the num beside it is the intensity for the blend , then the second variable is the watermark image itself, amd the number beside it is also the intensity to be applied for the blend, and the final value is the overall intensity for the new image formed usually zero.
cv2.imwrite("blend.jpeg", blended_image) # This is NOT ALL you. You will then paste teh section unto teh entire image like belo

