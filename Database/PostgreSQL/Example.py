# Python's version used: 3.8.2 64 bit
# pip install psycopg2
# PostgreSQL's server need to be active
import psycopg2
import os

# Change the working directory in the one of the .py file
# So we can import the .csv file always
try:
    os.chdir(os.path.dirname(__file__))
except:
    pass

# Creating connection
connection = psycopg2.connect(
    user="postgres",
    #password="",
    host="127.0.0.1",
    port="5432",
    database="prova")

# Creating cursor
cursor = connection.cursor()

# Deleting table peple if it exists
cursor.execute('''drop table if exists people;''')

# Creating table
cursor.execute(
    '''create table people (Name varchar,  Sex varchar, Age integer, Height integer, Weight integer);'''
)

# Initialize the executed query
# The commit is needed or the results will be saved only in a temporary memory
# And not saved on the PostgreSQL's database
connection.commit()

# Loading the .csv file into the table
# Passing the .csv file as an object
my_file = open("People.csv")
SQL_STATEMENT = """
    COPY %s FROM STDIN WITH
        CSV
        HEADER
        DELIMITER AS ','
    """
cursor.copy_expert(sql=SQL_STATEMENT % "people", file=my_file)
connection.commit()

# Query's execution
cursor.execute('''select avg(weight) from people;''')

# Printing the query's result
record = cursor.fetchall()
print("AVG(WEIGHT) = " + str(record))

# Deleting the table
cursor.execute('''drop table people;''')
connection.commit()