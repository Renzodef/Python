# Python's version used: 3.8.2 64 bit
import speech_recognition as sr  # pip install speechrecognition
import playsound  # pip install playsound
import os  # standard library

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

# Using the Google's API for recognize the words
# Choosing English as default language
text = recognizer_instance.recognize_google(audio)

# Printing the text recognized
print(text)