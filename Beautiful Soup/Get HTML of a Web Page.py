# Python's version used: 3.8.3 64 bit
# pip install beautifulsoup4
# To run the file on Windows
# Go in the terminal and type: chcp 65001
# Then go with the terminal in the folder of this file and type:
# python "Get HTML of a Web Page.py"
# The script may won't work if you launch it in other ways
from bs4 import BeautifulSoup
import requests

# Choosing the URL
URL = 'https://www.animeclick.it/'
# Request to the URL
content = requests.get(URL)
# Getting the HTML page of the selected URL
soup = BeautifulSoup(content.text, 'html.parser')
# Printing it in a comfortable format
print(soup.prettify())