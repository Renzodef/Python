# Python's version used: 3.8.2 64 bit
# pip install pandas
# You don't need to install it with pip, just install SQLite3 on the device
# SQLite doesn't need to start a server
import sqlite3
import os
import pandas as pd

# Changing the working directory in the one of the .py file
try:
    os.chdir(os.path.dirname(__file__))
except:
    pass

# Deleting the file prova.db if it exists
if os.path.exists("prova.db"):
    os.remove("prova.db")

# Creating the file prova.db
# In the same directory of the .py file
# This file contains the database
db = sqlite3.connect("prova.db")

# Creating cursors
# One for every queries' result we want to print
cursor = db.cursor()
cursor2 = db.cursor()

# Creating table
cursor.execute(
    "CREATE TABLE people (Name VARCHAR(30), Sex VARCHAR(10), Age int, Height int, Weight int);"
)

# Loading .csv file into the table
pd.read_csv("People.csv").to_sql("people", db, if_exists='append', index=False)

# Simple SQL's queries
cursor.execute("SELECT AVG(Height) FROM people;")
cursor2.execute("SELECT AVG(Weight) FROM people;")

# Priting the first row from the results of the queries
data = cursor.fetchone(
)  # fetchone returns only the first row of the results, if you want all the rows use fetchall
data2 = cursor2.fetchone()
print("Average Height is: " + str(data))
print("Average Weight is: " + str(data2))

# Deleting the .db file and the database
os.remove("prova.db")

# Closing connection
db.close()