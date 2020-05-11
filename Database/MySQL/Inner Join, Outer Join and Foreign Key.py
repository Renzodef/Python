# Python's version used: 3.8.2 64 bit
# pip install mysqlclient
# MySQL or MariaDB's server need to be active
import MySQLdb
import pathlib
import os

# Connecting to the Database (mysql is a default database of MySQL)
password = input("Enter your MySQL's password: ")
db = MySQLdb.connect("localhost", "root", password, "mysql")
print("\n")

# Creating cursor
cursor = db.cursor()

# Deleting the database "Prova" if it exists
cursor.execute("DROP DATABASE IF EXISTS Prova;")

# Creating the database and use it as current database
cursor.execute("CREATE DATABASE Prova;")
cursor.execute("USE Prova;")

# Creating tables
Q1 = "CREATE TABLE Users (id int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), password VARCHAR(50));"
# Assigning the key "userID" with a reference to the key "id" of the table "Users"
Q2 = '''CREATE TABLE Scores (userID int PRIMARY KEY, FOREIGN KEY(userID) REFERENCES Users(id),
        game1 int DEFAULT 0, game2 int DEFAULT 0);'''
cursor.execute(Q1)
cursor.execute(Q2)

# Showing the tables in the database
print("TABLES")
cursor.execute("SHOW TABLES;")
for x in cursor:
    print(x)
print("\n")

# Putting elements in the tables
# Inserting 3 rows in the table Users
users = [("renzo", "prova"), ("michele", "prova2"), ("antonio", "prova3")]
Q3 = "INSERT INTO Users (name, password) VALUES (%s, %s);"
# and 3 rows in the table Scores
user_scores = [(45, 100), (19, 24), (36, 72)]
Q4 = "INSERT INTO Scores (userID, game1, game2) VALUES (%s, %s, %s);"
for x, user in enumerate(users):
    cursor.execute(Q3, user)
    # Selecting the id of the last row inserted in the table "Users"
    last_id = cursor.lastrowid
    # and assigning it as "userID" in the table "Scores"
    cursor.execute(Q4, (last_id, ) + user_scores[x])

# Showing all the rows in the table "Users"
print("TABLE Users")
cursor.execute("SELECT * FROM Users;")
for x in cursor:
    print(x)
print("\n")

# Showing all the rows in the table "Scores"
print("TABLE Scores")
cursor.execute("SELECT * FROM Scores;")
for x in cursor:
    print(x)
print("\n")

# Inner Join Query
print("INNER JOIN")
Q5 = "SELECT * FROM Users u INNER JOIN Scores s ON u.id = s.userID;"
cursor.execute(Q5)
for x in cursor:
    print(x)
print("\n")

# Adding a row in table "Users"
print("ADDING A ROW IN TABLE Users")
Q6 = "INSERT INTO Users (name, password) VALUES ('chiara', 'prova4');"
cursor.execute(Q6)
cursor.execute("SELECT * FROM Users;")
for x in cursor:
    print(x)
print("\n")

# Example of Foreign Key that doesn't respect the reference in the other table
print("ADDING A ROW IN TABLE Scores")
try:
    Q7 = "INSERT INTO Scores (userID, game1, game2) VALUES (5, 31, 21);"
    cursor.execute(Q7)
    cursor.execute("SELECT * FROM Scores;")
    for x in cursor:
        print(x)
except:
    print(
        "Can't add the row because the foreign key doesn't respect the reference in the table Users."
    )
finally:
    print("\n")

# Inner Join Query
print("INNER JOIN")
Q8 = "SELECT * FROM Users u INNER JOIN Scores s ON u.id = s.userID;"
cursor.execute(Q5)
for x in cursor:
    print(x)
print("\n")

# Outer Join Query
print("OUTER JOIN")
Q9 = '''SELECT * FROM Users u LEFT JOIN Scores s ON u.id = s.userID;'''
cursor.execute(Q9)
for x in cursor:
    print(x)

# Deleting the tables and the database
# Putting "Scores" before "Users" because we can't delete a table
# if another one that has a foreign key related to that table exists
cursor.execute("DROP TABLE Scores;")
cursor.execute("DROP TABLE Users;")
cursor.execute("DROP DATABASE Prova;")

# Closing the connection
db.close()
