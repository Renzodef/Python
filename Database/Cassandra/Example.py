# Python's version used: 3.8.2 64 bit
# pip install cassandra-driver
# Before running the file we have to
# Start the Cassandra's server with:
# cassandra -f
from cassandra.cluster import Cluster

# Creating connection
cluster = Cluster(['0.0.0.0'], port=9042)
session = cluster.connect('prova', wait_for_all_pools=True)

# Deleting the columnfamily people if exists
session.execute('''DROP TABLE IF EXISTS people;''')

# Creating columnfamily
session.execute(
    '''CREATE COLUMNFAMILY people(Name text,Sex text,Age varint,Height_in varint,
    Weight_lbs varint,
    PRIMARY KEY(sex, age) )WITH CLUSTERING ORDER BY (age ASC);''')

# Loading data into columnfamily
session.execute('''INSERT INTO people (Name, Sex, Age) '''
                '''VALUES('Alex', 'M', 41) ''')
session.execute('''INSERT INTO people (Name, Sex, Age) '''
                '''VALUES('Bert', 'M', 42) ''')
session.execute('''INSERT INTO people (Name, Sex, Age) '''
                '''VALUES('Gwen', 'F', 33) ''')

# Printing the entire columnfamily
rows = session.execute('SELECT * FROM people')
for row in rows:
    print(row)

# Only for a better output
print(
    "\n///////////////////////////////////////////////////////////////////////////////////\n"
)

# Another query
rows = session.execute('''select avg(age) from people;''')
for row in rows:
    print(row)