import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='mehul1234'
)

cursorObject = dataBase.cursor()

# Check if the database exists
cursorObject.execute("SHOW DATABASES")
databases = [db[0] for db in cursorObject.fetchall()]

if 'pupu' not in databases:
    # Create database if it doesn't exist
    cursorObject.execute("CREATE DATABASE pupu")
    print("Database 'pupu' created!")
else:
    print("Database 'pupu' already exists!")

dataBase.close()