import psycopg2

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
    select_from_students = """
    SELECT students.name AS student, faculty.name AS faculty
    FROM students
    JOIN faculty ON students.faculty_id = faculty.id;
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