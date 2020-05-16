# Python's version used: 3.8.2 64 bit
# pip install selenium
# If you are on Linux
# go in the folder of the geckodriver and type:
# sudo chmod 777 geckodriver

from selenium import webdriver
from pprint import pprint
import os

# Creating the local path of the driver
try:
    os.chdir(os.path.dirname(__file__))
except:
    pass
finally:
    cwd = os.getcwd()
    try:
        # Executed as a simple script, the driver should be in `PATH`
        driver = webdriver.Firefox(executable_path=cwd +
                                   "/Windows/geckodriver.exe")
    except:
        driver = webdriver.Firefox(executable_path=cwd + "/Linux/geckodriver")

# Open a web page
driver.get("https://www.animeclick.it/")

# View the html page of the selected web page
html = driver.page_source
# Saving the content in a new file
f = open('savepage.html', 'wb')
# Changing the encoding
f.write(html.encode('utf-8'))
# Priting the html content
with open('savepage.html', 'rb') as file:
    # pprint for a clearer output
    pprint(str(file.read()))
f.close()
# Deleting the created file
file_path = 'savepage.html'
os.remove(file_path)

# Closing the browser
driver.quit()

# Deleting the logs
file_path = 'geckodriver.log'
os.remove(file_path)