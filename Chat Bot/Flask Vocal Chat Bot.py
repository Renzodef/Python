# Python's version used: 3.6.8 64 bit
# pip install chatterbot
# pip install chatterbot-corpus
# To run the web app, on Linux
# open the terminal in the folder of the .py file
# then type: export FLASK_APP="Flask Vocal Chat Bot.py"
# then: flask run
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import os

app = Flask(__name__)

english_bot = ChatBot("Chatterbot",
                      storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")


@app.route("/")
def homepage():
    return '''
<!DOCTYPE html>
<html>
  <head>
    <link rel="stylesheet" type="text/css" href="/static/style.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
  </head>
  <body>
    <h1>Flask Chatterbot Example</h1>
    <h3>A web implementation of ChatterBot using Flask.</h3>
    <div>
      <div id="chatbox">
        <p class="botText"><span>Hi! I'm Chatterbot.</span></p>
      </div>
      <div id="userInput">
        <input id="textInput" type="text" name="msg" placeholder="Message">
        <input id="buttonInput" type="submit" value="Send">
      </div>
      <script>
        function getBotResponse() {
          var rawText = $("#textInput").val();
          var userHtml = '<p class="userText"><span>' + rawText + '</span></p>';
          $("#textInput").val("");
          $("#chatbox").append(userHtml);
          document.getElementById('userInput').scrollIntoView({block: 'start', behavior: 'smooth'});
          $.get("/get", { msg: rawText }).done(function(data) {
            var botHtml = '<p class="botText"><span>' + data + '</span></p>';
            $("#chatbox").append(botHtml);
            document.getElementById('userInput').scrollIntoView({block: 'start', behavior: 'smooth'});
          });
        }
        $("#textInput").keypress(function(e) {
            if(e.which == 13) {
                getBotResponse();
            }
        });
        $("#buttonInput").click(function() {
          getBotResponse();
        })
      </script>
    </div>
  </body>
</html>'''


@app.route("/get")
def get():
    userText = request.args.get('msg')
    reply = english_bot.get_response(userText)
    text = str(reply)
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")
    audio = AudioSegment.from_mp3("output.mp3")
    play(audio)
    file_path = 'output.mp3'
    os.remove(file_path)