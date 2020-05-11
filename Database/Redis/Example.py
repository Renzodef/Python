# Python's version used: 3.8.2 64 bit
# pip install redis
# Redis' server need to be active
import redis

# Creating connection
client = redis.StrictRedis(host="127.0.0.1", port=6379, db=0)

# Setting some key-value couples
client.set("nome", "Renzo")
client.set("città", "Bari")
client.set("università", "Poliba")

# Printing the value of a key
print(client.get("nome"))

# Printing all the keys
for key in client.scan_iter():
    print(key)

# Deleting all the key-value couples in the database
client.flushdb()

# Printing the value of a key
# The result should be None since all the key-value couples were deleted
print(client.get("nome"))