# Python's version used: 3.8.3 64 bit
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
driver.get("https://stackoverflow.com/")

# If the elements exists
try:
    # Finding an element with the selected words in the opened page
    link = driver.find_element_by_link_text("Use cases")
    # Clicking on that element
    link.click()
    # Go one page back
    driver.back()
    # Go one page forward
    driver.forward()
    # Finding an element with the selected words in the opened page
    link = driver.find_element_by_link_text("Explore Enterprise")
    # Click on that element
    link.click()
# If the elements not exists
except:
    # Closing the browser
    driver.quit()
