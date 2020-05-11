# Python's version used: 3.6.8 64 bit
# pip install tensorflow==1.5.0
# pip install opencv-python
# pip install keras==2.1.5
# pip install imageai --upgrade
from imageai.Detection import VideoObjectDetection
import os  

# Changing the current directory in the one of the .py file
try:
    os.chdir(os.path.dirname(__file__))
except:
    pass
# Saving the current directory's path
execution_path = os.getcwd()

# Creating the detector model through YOLO
detector = VideoObjectDetection()
detector.setModelTypeAsYOLOv3()
# Path of the YOLO's file
detector.setModelPath(os.path.join(execution_path, "Resources/yolo.h5"))
# Choice of the detection's speed
# You can choose between normal" (default), "fast", "faster", "fastest" and "flash"
detector.loadModel(detection_speed="flash")

# Applying the model
detector.detectObjectsFromVideo(
    # Input file
    input_file_path=os.path.join(execution_path, "Resources/Video.mp4"),
    # Output file
    output_file_path=os.path.join(execution_path, "Output"),
    # Put True if you want the percentage to be displayed in the output image
    display_percentage_probability=False,
    # Put False if you don't wanna see in terminal the progress of the process
    log_progress=True)

import cv2 
import numpy as np
# Displaying the video
# Create a VideoCapture object and read from input file
cap = cv2.VideoCapture('Output.avi')
# Check if camera opened successfully
if (cap.isOpened() == False):
    print("Error opening video file")
# Read until video is completed
while (cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:
        # Display the resulting frame
        cv2.imshow('Frame', frame)
        # Press q on keyboard to exit
        # Change the number of waitKey according to the speed you want for the video
        # Lower numbers are faster
        if cv2.waitKey(60) & 0xFF == ord('q'):
            break
    # Break the loop
    else:
        break
# When everything done, release
# the video capture object
cap.release()
# Closes all the frames
cv2.destroyAllWindows()

# Displaying the video at original speed
# If you wanna use this
# Comment the lines related to Deleting the video
#import subprocess, sys  # standard library
#opener = "open" if sys.platform == "darwin" else "xdg-open"
#subprocess.call([opener, "Output.avi"])

# Deleting the video
file_path = 'Output.avi'
os.remove(file_path)
