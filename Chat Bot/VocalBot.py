# Python's version used: 3.6.8 64 bit
# pip install gtts
# pip install pydub
# pip install chatterbot
# pip install chatterbot-corpus
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import os
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Giving a name to the bot
bot = ChatBot('Candice')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(bot)

# Train the chatbot based on the english corpus
# You can choose also other language, look for them here:
# https://github.com/gunthercox/chatterbot-corpus/tree/master/chatterbot_corpus/data
trainer.train("chatterbot.corpus.english")

print("\nWrite 'bye' to exit from the bot.\n")

# Conditions for exit and responses
while True:
    # Input from user
    print("\n")
    message = input('You: ')
    print("\n")
    # If message is not "Bye"
    if message.strip() == 'Bye':
        text = "Bye bye!"
        tts = gTTS(text=text, lang='en')
        tts.save("output.mp3")
        # Listening to the created .mp3 file
        audio = AudioSegment.from_mp3("output.mp3")
        play(audio)
        # Deleting the .mp3 file
        file_path = 'output.mp3'
        os.remove(file_path)
        break
    if message.strip() == 'bye':
        text = "Bye bye!"
        tts = gTTS(text=text, lang='en')
        tts.save("output.mp3")
        # Listening to the created .mp3 file
        audio = AudioSegment.from_mp3("output.mp3")
        play(audio)
        # Deleting the .mp3 file
        file_path = 'output.mp3'
        os.remove(file_path)
        break
    else:
        reply = bot.get_response(message)
        text = str(reply)
        # Creating the .mp3 file
        tts = gTTS(text=text, lang='en')
        tts.save("output.mp3")
        audio = AudioSegment.from_mp3("output.mp3")
        play(audio)
        # Deleting the .mp3 file
        file_path = 'output.mp3'
        os.remove(file_path)