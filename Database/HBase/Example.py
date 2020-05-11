# Python's version used: 3.8.2 64 bit
# pip install happybase
# Before running the file we have to
# Start the Thrift's server with:
# hbase-daemon.sh start thrift
# Start HBase's server with:
# start-hbase.sh
import happybase as hb
from w3lib.util import to_bytes

# Creating connection
connection = hb.Connection('127.0.0.1', 9090)

# Creating table
connection.create_table('emp', {
    'personal data': dict(),
    'professional data': dict()
})

# Assigning the table to an object
table = connection.table('emp')

# Printing all the tables of the connection
print(connection.tables())

# Adding data into the table
table.put(b'1', {
    b'personal data:name': b'raju',
    b'professional data:designation': b'manager'
})
table.put(
    b'2', {
        b'personal data:name': b'renzo',
        b'personal data:age': b'24',
        b'professional data:university': b'poliba'
    })

# Stampa di tutti i dati della tabella
for key, data in table.scan():
    print(key, data)

# Deleting the table
# Before we need to disable it
table_name = to_bytes(b'emp')
tables = set(connection.tables())
if table_name in tables:
    connection.delete_table(table_name, disable=True)
    tables.remove(table_name)