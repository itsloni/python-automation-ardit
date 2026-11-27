# Here we'll identify faces of human using cv2 and we'll do that by placing a rectangle on the face.
import cv2


image = cv2.imread("humans.jpeg", 1)

face_haar_cascade = cv2.CascadeClassifier("faces.xml") # This is calling the 'haar cascade' file so cv knows it.

face = face_haar_cascade.detectMultiScale(image, 1.1, 4) #This is used to detect multiple sizes and scales of faces in an image. The '1.1' is called the scale factor, and the '4' is called minimum neighbours.
# so those number are literally important so the 1.1 is like teh scale number so before python finds a face as it moves from pixel to pixel irt zooms or umzoom and for zooming the '1.1' is the scale it will use
# as it zooms until it find teh face or how a face looks at whatever scale the image has. And then '4' is the minimum neighbours which is like the smallest number of pixels it must be attached to or also consider as it zooms, so
# cause we set it to 4 it cant zoom with only 3 pixels rather it zooms with 4 at least 4 at a time to finally find a face.

#Note: when we then print face the variable above it give sa numpy array of 2Dlists that is a list with a list.
print(face) # so basically the output are coordinates of a rectangle and each list inside is a rectangle and that represents the each face so there are about 2 list so that means that there were 2 faces in the image hence 22 rectangles were created.