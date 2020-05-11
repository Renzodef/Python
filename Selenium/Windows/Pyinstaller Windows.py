# Python's version used: 3.8.2 64 bit
# by importing correctly the chromedriver in the .exe file.

from selenium import webdriver
import os
import sys

# URL to use later
x = input("Copy an URL here: ")

# These lines are to create an executable with Pyinstaller.
# To create the executable, go with the terminal in the folder of the -py file and type:
# pip install pyinstaller
# pyinstaller -F --add-binary "chromedriver.exe";"." "Pyinstaller Windows.py"
if __name__ == "__main__":
    if getattr(sys, 'frozen', False):
        chromedriver_path = os.path.join(sys._MEIPASS,
                                         "chromedriver.exe")
        driver = webdriver.Chrome(chromedriver_path)
    else:
        try:
            os.chdir(os.path.dirname(__file__))
        except:
            pass
        finally:
            cwd = os.getcwd()
            print(cwd)
            # Executed as a simple script, the driver should be in `PATH`
            driver = webdriver.Chrome(executable_path= cwd + "/chromedriver.exe")

# Example acions

# Open a web page
driver.get(x)

# Printing the title of the web page
print("\nThe title of the inserted URL is: " + str(driver.title) + "\n")

# Closing the browser
driver.quit()

# To make the executable not close after finishing
input("Press enter to exit. ")
