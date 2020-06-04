# Python's version used: 3.8.2 64 bit
# pip install selenium
# If you are on Linux
# go in the folder of the geckodriver and type:
# sudo chmod 777 geckodriver

# This program shows an example of "bot"
# that performs an automated click on a button of a web page
# for a specified number of times chosen by the user

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from pprint import pprint
import os

# Getting the input of the times you want the Cookie to be clicked
x = input(
    "Type of how many times you want the Cookie to be clicked.\nOnly numbers will be accepted: "
)
x = int(x)

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

# Open the web page
driver.get("https://orteil.dashnet.org/cookieclicker/")

# Selecting the big cookie to click
# In the HTML page this is represented by "bigCookie"
# You can find it by visualising the HTML page directly in the browser
cookie = driver.find_element_by_id("bigCookie")
# Selecting the element related to the count of the cookies
# In the HTML page this is represented by "cookies"
cookie_count = driver.find_element_by_id("cookies")

# Selecting the action to repeat multiple times
actions = ActionChains(driver)
actions.click(cookie)

print("Count of Cookies:")
for i in range(x):
    # Perform the click
    actions.perform()
    # Printing the count of the cookies
    count = int(cookie_count.text.split(" ")[0])
    print(count + 1)
print("Finished")
input("Press Enter to Exit the program...")

# Closing the browser
driver.quit()