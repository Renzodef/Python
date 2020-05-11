# Python's version used: 3.8.2 64 bit
# pip install gtts
# pip install playsound
from gtts import gTTS
import playsound
import os

# Input text
text = input("Print the text you want to listen from the PC: ")

# Creating the .mp3 file
# You can change the language by replacing 'en'
tts = gTTS(text=text, lang='en')
tts.save("output.mp3")

# Listening to the created .mp3 file
playsound.playsound('output.mp3', True)

# Deleting the .mp3 file
file_path = 'output.mp3'
os.remove(file_path)