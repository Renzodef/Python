# Python's version used: 3.8.2 64 bit
# pip install requests
import tkinter as tk
import tkinter.font as font
import sys
import os
import requests

# These  lines are only to create a correct executable file with Pyinstaller
# by importing correctly the icon file.
# To do this go in the terminal in the folder of this file and type
# For Windows:
# pyinstaller --onefile --noconsole --add-data="Weather.ico;." --icon=Weather.ico Weather.py
if getattr(sys, 'frozen', False):
    icon_path = os.path.join(sys._MEIPASS, "Weather.ico")
else:
    try:
        os.chdir(os.path.dirname(__file__))
    except:
        pass
    finally:
        icon_path = "Weather.ico"

# Window
window = tk.Tk()
# icon
try:
    # Windows
    window.iconbitmap(icon_path)
except:
    # Linux
    pass
window.geometry("600x300")
window.title("Weather")
window.grid_columnconfigure(0, weight=1)
window.resizable(False, False)
window.configure(background="grey")


# Function
def translate():
    try:
        user_input = text_input.get()
        # Enter your API key here
        # Get it from the openweathermap website
        api_key = "5742294789c8bd44d19781dbae797b3b"
        # Url for the request
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        # Complete_url variable to store
        # Complete url address
        complete_url = base_url + "appid=" + api_key + "&q=" + user_input
        # Get method of requests module
        # Return response object
        response = requests.get(complete_url)
        # Json method of response object
        # Convert json format data into
        # Python format data
        x = response.json()
        # Now x contains list of nested dictionaries
        # Check the value of "cod" key is equal to
        # "404", means city is found otherwise,
        # city is not found
        if x["cod"] != "404":
            # Store the value of "main"
            # key in variable y
            y = x["main"]
            # Store the value corresponding
            # to the "temp" key of y
            current_temperature = y["temp"]
            # Store the value corresponding
            # to the "pressure" key of y
            current_pressure = y["pressure"]
            # Store the value corresponding
            # to the "humidity" key of y
            current_humidiy = y["humidity"]
            # Store the value of "weather"
            # key in variable z
            z = x["weather"]
            # Store the value corresponding
            # to the "description" key at
            # the 0th index of z
            weather_description = z[0]["description"]
        text_response = (" Temperature = " +
                         str(round(current_temperature - 273.15)) + " °C" +
                         "\n Atmospheric pressure = " + str(current_pressure) +
                         " hPa" + "\n Humidity = " + str(current_humidiy) +
                         " %" + "\n Weather = " + str(weather_description))
    except:
        text_response = "Wrong input!"

    myFont = font.Font(size=20)
    textwidget = tk.Text()
    textwidget['font'] = myFont
    textwidget.insert(tk.END, text_response)
    textwidget.configure(background="grey")
    textwidget.place(x=20, y=150, height=135, width=560)


# Label
welcome_label = tk.Label(window,
                         text="Put the name of the city down below: ",
                         background="grey",
                         font=("Helvetica", 15))
welcome_label.grid(row=0, column=0, sticky="N", padx=20, pady=20)

# Input grid
text_input = tk.Entry(font=("Helvetica", 15))
# cursor is mandatory with the gray background
# or we won't see it
text_input.configure(background="gray", cursor="arrow")
text_input.grid(row=1, column=0, sticky="WE", padx=20)

# Button
button = tk.Button(text="SEARCH", command=translate)
button.configure(background="grey")
button.grid(row=2, column=0, sticky="WE", pady=10, padx=20)

if __name__ == "__main__":
    window.mainloop()
