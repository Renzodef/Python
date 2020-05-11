# Python's version used: 3.8.2 64 bit
# pip install pymongo
# pip install pandas
# Before running the file we need to start the MongoDB's server:
# mongod --dbpath /path_directory_you_want_as_database
from pymongo import MongoClient
import json
import pandas as pd
import os

# Making the directory of the .py file as the current one
# So we can always import the .csv file
try:
    os.chdir(os.path.dirname(__file__))
except:
    pass


# This function imports a .csv file
def mongoimport(csv_path, db_name, coll_name, db_url, db_port):
    client = MongoClient(db_url, db_port)
    db = client[db_name]
    coll = db[coll_name]
    data = pd.read_csv(csv_path)
    payload = json.loads(data.to_json(orient='records'))
    coll.insert(payload)
    return coll.count()


# Creating connection
client = MongoClient('localhost', 27017)

# Choice of the database
db = client.demo

# Deleting the collection with the same name if it exists
db.taxi.drop()

# Importing the .csv file in the collection taxi of the demo database
mongoimport("Green.csv", "demo", "taxi", "localhost", 27017)
mongoimport("Yellow.csv", "demo", "taxi", "localhost", 27017)

# Only for a better output
print(
    "\n/////////////////////////////////////////////////////////////////////////\n"
)

# Same query as SQL's GROUP BY
print("RESULT QUERY 1:")
pipeline = [{
    "$group": {
        "_id": "$payment_type",
        "Sum": {
            "$sum": "$passenger_count"
        }
    }
}]
print(list(db.taxi.aggregate(pipeline)))

# Only for a better output
print(
    "\n/////////////////////////////////////////////////////////////////////////\n"
)

# Same query as SQL's SUM(column) FROM table
print("RESULT QUERY 2:")
pipeline2 = [{"$group": {"_id": "", "Sum": {"$sum": "$trip_distance"}}}]
print(list(db.taxi.aggregate(pipeline2)))

# Only for a better output
print("\n")

# Deleting the collection
db.taxi.drop()