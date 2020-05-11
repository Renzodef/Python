# Python's version used: 3.8.2 64 bit
# Need also to install Sphinx:
# On Windows it seems to not work
# On Manjaro Linux install from AUR the package:
# sphinxbase
# then: pip install sphinxpocket
# So the script will be able to understand English offline
# pip install speechrecognition
# pip install playsound
import speech_recognition as sr
import playsound
import os

# Changing the current directory in the one of the .py file
try:
    os.chdir(os.path.dirname(__file__))
except:
    pass

# Creatiion of the recognizer instance
recognizer_instance = sr.Recognizer()

# Importing the audio file
wav = sr.AudioFile("Example.wav")

# Reproducing the file
playsound.playsound('Example.wav', True)

# Using the file as source of the audio
with wav as source:
    audio = recognizer_instance.record(source)

# Using the Sphinx for recognize the words
# Choosing English as default language
text = recognizer_instance.recognize_sphinx(audio)

# Printing the text recognized
print(text)