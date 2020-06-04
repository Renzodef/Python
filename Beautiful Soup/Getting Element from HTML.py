# Python's version used: 3.8.3 64 bit
# pip install beautifulsoup4
from bs4 import BeautifulSoup
import requests

# Choosing the URL
URL = 'https://www.animeclick.it/'
# Request to the URL
content = requests.get(URL)
# Getting the HTML page of the selected URL
soup = BeautifulSoup(content.text, 'html.parser')
# em represents in HTML a Mark up emphasized text in a document
# This return the first occurence in the HTML document that contains em
row = soup.find('em')
# Print row with HTML formatting
print("=========HTML Result==========")
print(row)
print("\n")
# Print row as text
print("=========Text Result==========")
print(row.get_text())
