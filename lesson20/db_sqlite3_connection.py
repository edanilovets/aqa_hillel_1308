import sqlite3

connection = sqlite3.connect('school2.db')

try:

    print("Connected to the database successfully!")

    cursor = connection.cursor()
    # cursor.execute("SELECT version();")

    record = cursor.fetchone()
    print("You are connected to - ", record)

except (Exception, sqlite3.Error) as error:
    print("Error while connecting to DB", error)

finally:
    if connection:
        cursor.close()
        connection.close()
        print("DB connection is closed")