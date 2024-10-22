import psycopg2

dbname = 'school2'
user = 'postgres'
password = '12345'
host = 'localhost'  # 127.0.0.1
port = '5432'

class SqlDbConnector:
    def __init__(self, dbname, user, password, host="localhost", port="5432"):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = None

    def connect(self):
        """Enables connection..."""
        try:
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgresSQL", error)

    def execute_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        return cursor

    def fetch_all(self, query):
        cursor = self.execute_query(query)
        results = cursor.fetchall()
        cursor.close()
        return results

    def close(self):
        if self.connection:
            self.connection.close()
            print("PostgresSQL connection is closed")

    # context manager - with
    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


if __name__ == '__main__':
    with SqlDbConnector(dbname, user, password, host, port) as db:
        select_from_students = """
        SELECT students.name AS student, faculty.name AS faculty
        FROM students
        JOIN faculty ON students.faculty_id = faculty.id;
        """
        records = db.fetch_all(select_from_students)
        print("Records: ", records)
