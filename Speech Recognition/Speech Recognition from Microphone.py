# Python's version used: 3.8.2 64 bit
# Pyaudio is needed
# On Windows download the desired version from:
# https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
# choose the file based on the Python's version and the system's architecture
# and install it with: pip install name_of_the_file.whl
# On Manjaro Linux you need first to change the jack with:
# sudo pacman -S jack2
# then install pyaudio with: pip install pyaudio
# pip install speechrecognition
import speech_recognition as sr

# Creatiion of the recognizer instance
recognizer_instance = sr.Recognizer()

# Choosing language
language = input(
    "Choose between Italian or English.\nPress 'i' to select Italian language or any other key for English: "
)

# Italian language
if language == "i":
    while True:
        # Using microphone as source of the audio
        with sr.Microphone() as source:
            recognizer_instance.adjust_for_ambient_noise(source)
            print("Parla ora!")
            audio = recognizer_instance.listen(source)
            print("Sto elaborando quello che hai detto...")
        try:
            # Using the Google's API for recognize the words
            # Choosing italian as language
            # The list of the available language can be found at:
            # https://cloud.google.com/speech-to-text/docs/languages
            text = recognizer_instance.recognize_google(audio,
                                                        language="it-IT")
            # Printing the text recognized
            print("---------------------")
            print("Hai detto: " + text)
            print("---------------------")
            x = input(
                "Vuoi provare ancora?\nPremi 's' per sì o qualsiasi altro tasto per uscire dal programma: "
            )
            if x == "s":
                pass
            else:
                break
        except:
            print(
                "Non ho capito. Cerca di parlare più chiaramente per favore..."
            )

# English Language
else:
    while True:
        # Using microphone as source of the audio
        with sr.Microphone() as source:
            recognizer_instance.adjust_for_ambient_noise(source)
            print("Speak now!")
            audio = recognizer_instance.listen(source)
            print("I'm elaborating what you said...")
        try:
            # Using the Google's API for recognize the words
            # Choosing english as default language
            text = recognizer_instance.recognize_google(audio)
            # Printing the text recognized
            print("---------------------")
            print("You said: " + text)
            print("---------------------")
            x = input(
                "Do you wanna try again?\nPress 'y' if yes or any other key to exit the program... "
            )
            if x == "y":
                pass
            else:
                break
        except:
            print("I couldn't understand you. Speak more clearly please...")