# Python's version used: 3.8.2 64 bit
# pip install selenium
from selenium import webdriver 
import os 

# Creating the local path of the driver
try:
    os.chdir(os.path.dirname(__file__))
except:
    pass
finally:
    cwd = os.getcwd()
    # Executed as a simple script, the driver should be in `PATH`
    driver = webdriver.Chrome(executable_path= cwd + "/chromedriver.exe")

# Open a web page
driver.get('https://stackoverflow.com/')

# Printing the title of the web page
print(driver.title)

# Closing the browser
driver.quit()
