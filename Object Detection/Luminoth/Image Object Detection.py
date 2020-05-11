# Python's version used: 3.6.8 64 bit
# pip install tensorflow==1.5.0
# pip install luminoth
from luminoth import Detector, read_image, vis_objects
from PIL import Image 
import os

# Changing the current directory in the one of the .py file
try:
    os.chdir(os.path.dirname(__file__))
except:
    pass

# Reading the .jpg image
image = read_image('Pets.jpg')

# Creating the detector
detector = Detector()

# Returning a dictionary with the detections
objects = detector.predict(image)
print(objects)

# Creating a .jpg file with the detections
vis_objects(image, objects).save('Pets-out.jpg')

# Showing the image
image = Image.open('Pets-out.jpg')
image.show()

# Deleting the image
file_path = 'Pets-out.jpg'
os.remove(file_path)
