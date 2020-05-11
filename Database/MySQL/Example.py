# Python's version used: 3.8.2 64 bit
# pip install mysqlclient
# MySQL or MariaDB's server need to be active
import MySQLdb 
import pathlib 
import os 

# Changing the working directory in the one of the .py file
# So we can always import the .csv file correctly
try:
    os.chdir(os.path.dirname(__file__))
except:
    pass

# Connecting to the Database (mysql is a default database of MySQL)
password = input("Enter your MySQL's password: ")
db = MySQLdb.connect("localhost", "root", password, "mysql")
print("\n")

# Creating cursors
# One for every queries' output we want
cursor = db.cursor()
cursor2 = db.cursor()

# Deleting the database Prova if exists
cursor.execute("DROP DATABASE IF EXISTS Prova;")

# Creating the database and use it as current database
cursor.execute("CREATE DATABASE Prova;")
cursor.execute("USE Prova;")

# Creating table
cursor.execute(
    "CREATE TABLE people (Name VARCHAR(30), Sex VARCHAR(10), Age int, Height int, Weight int);"
)

# Loading .csv file into the table
# pathlib is needed so we can load the .csv file from the current directory 
cursor.execute("LOAD DATA LOCAL INFILE '" +
               str(pathlib.Path("Prova.csv").parent.absolute()) +
               "/People.csv" +
               "' INTO TABLE people COLUMNS TERMINATED BY ',' IGNORE 1 LINES;")

# Simple SQL's queries
cursor.execute("SELECT AVG(Height) FROM people;")
cursor2.execute("SELECT AVG(Weight) FROM people;")

# Priting a single row from the results of the queries
data = cursor.fetchone(
)  # fetchone returns only the first row of the results, if we want all the rows we should use fetchall
data2 = cursor2.fetchone()
print("Average Height is: " + str(data))
print("Average Weight is: " + str(data2))

# Deleting the table and the database
cursor.execute("DROP TABLE people;")
cursor.execute("DROP DATABASE Prova;")

# Closing the connection
db.close()
