import psycopg2
# import sqlite3

dbname = 'school2'
user = 'postgres'
password = '12345'
host = 'localhost'  # 127.0.0.1
port = '5432'

try:
    connection = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
    print("Connected to the database successfully!")

    cursor = connection.cursor()
    # BEGIN;
    insert_into_students = """
    INSERT INTO students (name, age)
    VALUES
    ('Andrii', 99),
    ('Sergiy', 88);
    """
    cursor.execute(insert_into_students)
    # COMMIT;
    connection.commit()
    select_from_students = """
    SELECT * FROM students;
    """
    cursor.execute(select_from_students)

    records = cursor.fetchall()
    print("Records: ", records)

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgresSQL", error)

finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")