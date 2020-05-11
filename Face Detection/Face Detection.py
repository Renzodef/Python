# Python's version used: 3.8.2 64 bit
# pip install opencv-python
# pip install matplotlib
import cv2
import os
import matplotlib.pyplot as plt

# Changing the current directory in the one of the .py file
try:
    os.chdir(os.path.dirname(__file__))
except:
    pass

# Input image
img = cv2.imread("Images/4.jpg")

# Initialiting the .xml file for face detection
# This file is needed by the Cascade Classifier
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Converting the image in black and white
# because the Cascade Classifier accepts only this kind of images
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Assigning the detected faces to a vector
# The argument of the detector are : image, scale factor and minimum number of neighbors
# If we increase the scale factor,
# then the algorithm will be less accurate but faster
# The minimum number of neighbors is the number of features that the algorithm
# should detect to recognize a face
# If the algorithm detects more faces than needed, increase this number
# If it detects less faces than needed, decrease this number
# Anyway, change scale factor and minimum number of neighbors
# according to the choosed photo and the speed you want to achieve.
faces = face_cascade.detectMultiScale(gray, 1.2, 10)
print("\n")
print("Number of detected faces: " + str(len(faces)))
print("\n")

# Every face of faces return 4 cardinal points
# Writing rectangles based on these point over the detected faces
# 0, 255, 0 is to make the rectangle's color green
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Saving the output image
# The image output won't be gray, but colored
cv2.imwrite("Output.jpg", img)

# Showing the output image
img = plt.imread('Output.jpg')
plt.imshow(img)
plt.show()

# Deleting the output image
file_path = 'Output.jpg'
os.remove(file_path)
