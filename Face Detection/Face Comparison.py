# Python's version used: 3.8.2 64 bit
# Cmake and dlib packages are needed before this
# To install them on Manjaro Linux:
# sudo pacman -S cmake
# sudo pacman -S gcc
# Install from AUR the package "python-dlib"
# pip install face_recognition
import face_recognition
import json
import os

# Change the working directory in the one of the .py file
# So we can import the images everytime
try:
    os.chdir(os.path.dirname(__file__))
except:
    pass

# Load the images
first_image = face_recognition.load_image_file("Images/1.jpg")
second_image = face_recognition.load_image_file("Images/2.jpg")
third_image = face_recognition.load_image_file("Images/3.jpg")
# If you wanna see the matrix of an image:
# print(type(first_image))
# print(f"{first_image=}")

first_encoding = face_recognition.face_encodings(first_image)[0]
second_encoding = face_recognition.face_encodings(second_image)[0]
third_encoding = face_recognition.face_encodings(third_image)[0]
# If you wanna see the matrix of the encoding:
# print(first_encoding)

# Comparison between the two images with the same face
result = face_recognition.compare_faces([first_encoding], second_encoding)
answer = "Yes" if result[0] else "No"
print(f"The first and second images represent the same person? {answer}.")

# Comparison between the two images with different faces
result = face_recognition.compare_faces([first_encoding], third_encoding)
answer = "Yes" if result[0] else "No"
print(f"The first and third images represent the same person? {answer}.")

print(
    "\n///////////////////////////////////////////////////////////////////////\n"
)

# Distance between the two images wth the same face
face_distance = face_recognition.face_distance([first_encoding],
                                               second_encoding)
match = True if face_distance[0] <= 0.6 else False
print(
    f"The second image has a distance of {face_distance[0]:.2} from the first image. Match: {match}."
)

# Distance between the two images with different faces
face_distance = face_recognition.face_distance([first_encoding],
                                               third_encoding)
# We put 0.6 has maximum distance for the match because this is the dafault value in the imported library
match = True if face_distance[0] <= 0.6 else False
print(
    f"The third image has a distance of {face_distance[0]:.2} from the first image. Match: {match}."
)

# Distance between the same image
face_distance = face_recognition.face_distance([first_encoding],
                                               first_encoding)
match = True if face_distance[0] <= 0.6 else False
print(
    f"The first image has a distance of {face_distance[0]:.2} from the first image. Match: {match}."
)