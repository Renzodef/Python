# Python's version used: 3.6.8 64 bit
# pip install tensorflow==1.5.0
# pip install opencv-python
# pip install keras==2.1.5
# pip install imageai --upgrade
from imageai.Detection import ObjectDetection
from PIL import Image  
import os

# Changing the current directory in the one of the .py file
try:
    os.chdir(os.path.dirname(__file__))
except:
    pass
# Saving the current directory's path
execution_path = os.getcwd()

# Creating the detector model through YOLO
detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
# Path of the YOLO's file
detector.setModelPath(os.path.join(execution_path, "Resources/yolo.h5"))
detector.loadModel()
# We want to detect only the umbrella in the image
custom_objects = detector.CustomObjects(umbrella=True)

# Applying the model
detector.detectCustomObjectsFromImage(
    # Objects to detect
    custom_objects=custom_objects,
    # Input image
    input_image=os.path.join(execution_path, "Resources/Test.webp"),
    # Output image
    output_image_path=os.path.join(execution_path, "Output.webp"),
    # Minimum percentage for the objects' discrimination
    minimum_percentage_probability=30)

# Showing the image
image = Image.open('Output.webp')
image.show()

# Deleting the image
file_path = 'Output.webp'
os.remove(file_path)
