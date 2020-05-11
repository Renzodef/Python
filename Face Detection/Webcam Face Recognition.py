# Python's version used: 3.8.2 64 bit
# Cmake and dlib packages are needed before this
# To install them on Manjaro Linux:
# sudo pacman -S cmake
# sudo pacman -S gcc
# Install from AUR the package "python-dlib"
# pip install face_recognition
# pip install opencv-python
import face_recognition
import cv2
import os

# Change the working directory in the one of the .py file
# So we can import the images everytime
try:
    os.chdir(os.path.dirname(__file__))
except:
    pass

webcam = cv2.VideoCapture(0)

# Images Database (you can change and add new Images)
target_image = face_recognition.load_image_file("Images/renzo.jpg")
target_encoding = face_recognition.face_encodings(target_image)[0]
target_image1 = face_recognition.load_image_file("Images/nicola.jpg")
target_encoding1 = face_recognition.face_encodings(target_image1)[0]
target_name = "RENZO"
target_name1 = "NICOLA"

process_this_frame = True

while True:
    ret, frame = webcam.read()

    small_frame = cv2.resize(frame, None, fx=0.20, fy=0.20)
    rgb_small_frame = cv2.cvtColor(small_frame, 4)

    if process_this_frame:

        face_locations = face_recognition.face_locations(rgb_small_frame)
        frame_encodings = face_recognition.face_encodings(rgb_small_frame)

        if frame_encodings:
            frame_face_encoding = frame_encodings[0]
            # When you add new images, you should add also the match and another elif
            match = face_recognition.compare_faces([target_encoding],
                                                   frame_face_encoding)[0]
            match1 = face_recognition.compare_faces([target_encoding1],
                                                    frame_face_encoding)[0]
            label = "Name"
            if match == True:
                label = target_name
            elif match1 == True:
                label = target_name1
            else:
                label = "Unknown"

    process_this_frame = not process_this_frame

    if face_locations:
        top, right, bottom, left = face_locations[0]

        top *= 5
        right *= 5
        bottom *= 5
        left *= 5

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        cv2.rectangle(frame, (left, bottom - 30), (right, bottom), (0, 255, 0),
                      cv2.FILLED)
        label_font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, label, (left + 6, bottom - 6), label_font, 0.8,
                    (255, 255, 255), 1)

    cv2.imshow("Video Feed", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

webcam.release()
cv2.destroyAllWindows()