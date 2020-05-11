# Python's version used: 3.6.8 64 bit
# pip install chatterbot
# pip install chatterbot-corpus
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
    message = input('You: ')
    if message.strip() == 'Bye':
        print('Candice: Bye Bye!')
        break
    if message.strip() == 'bye':
        print('Candice: Bye Bye!')
        break
    else:
        reply = bot.get_response(message)
        print('Candice:', reply)