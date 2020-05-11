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

# Applying the model
detections = detector.detectObjectsFromImage(
    # Input image
    input_image=os.path.join(execution_path, "Resources/Test.webp"),
    # Output image
    output_image_path=os.path.join(execution_path, "Output.webp"),
    # Put True if you want the percentage to be displayed in the output image
    display_percentage_probability=False)

# Priting the list of the detections
print("--------------------------------")
for eachObject in detections:
    print(eachObject["name"], " : ", eachObject["percentage_probability"])
    print("--------------------------------")

# Showing the image
image = Image.open('Output.webp')
image.show()

# Deleting the image
file_path = 'Output.webp'
os.remove(file_path)
