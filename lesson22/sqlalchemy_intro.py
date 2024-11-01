from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, case, func
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

DATABASE_URL = "postgresql+psycopg2://danilovets:12345@localhost/school3"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# SQL for table 1
# CREATE TABLE faculty (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(200) NOT NULL
# );
class Faculty(Base):
    __tablename__ = "faculty"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(200), nullable=False)
    students = relationship('Student', back_populates='faculty')

    def __repr__(self):
        return f"Faculty(name={self.name}, id={self.id}"

# SQL for table 2
# CREATE TABLE students (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100),
#     age INTEGER,
#     faculty_id INTEGER REFERENCES faculty(id) ON DELETE SET NULL
# );
class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(200))
    age = Column(Integer)
    faculty_id = Column(Integer, ForeignKey("faculty.id", ondelete='SET NULL'))
    faculty = relationship('Faculty', back_populates='students')

    def __repr__(self):
        return f"Student(name={self.name}, age={self.age})"

Base.metadata.create_all(engine)

# CRUD operations #########################################################
# Insert using ORM

# INSERT INTO faculty (name)
# VALUES
# ('Software Engineering 2'),
# ('Math 2'),
# ('Biology 2');

# faculty1 = Faculty(name="Software Engineering")
# faculty2 = Faculty(name="Math")
# faculty3 = Faculty(name="Biology")
# session.add_all([faculty1, faculty2, faculty3])
# session.commit()

# INSERT INTO students (name, age, faculty_id)
# VALUES
# ('Alice', 20, 1),
# ('Bob', 21, 1),
# ('Eugene', 25, 2),
# ('Anna', 25, 3);

# s1 = Student(name="Alice", age=20, faculty=faculty1)
# s2 = Student(name="Bob", age=21, faculty=faculty1)
# s3 = Student(name="Eugene", age=25, faculty=faculty2)
# s4 = Student(name="Anna", age=25, faculty=faculty3)
# s5 = Student(name="Anna", age=26)
# session.add_all([s1, s2, s3, s4, s5])
# session.commit()

# Read
# SELECT students.name, faculty.name
# FROM students
# JOIN faculty ON students.faculty_id = faculty.id;

results = session.query(Student.name.label("student"), Faculty.name.label("faculty")) \
          .join(Faculty, Student.faculty_id == Faculty.id) \
          .all()

for student, faculty in results:
    print(f"Student: {student}, faculty: {faculty}")
# print(results)

print("-" * 100)

# Update
# UPDATE students SET age = 30 WHERE name = 'Alice';

student_to_update = session.query(Student).filter(Student.name == 'Alice').first()
print(student_to_update)
if student_to_update:
    student_to_update.age = 40
    session.commit()

# Delete
# DELETE FROM students WHERE name = 'Alice';
student_to_delete = session.query(Student).filter(Student.name == 'Alice').first()
if student_to_delete:
    session.delete(student_to_delete)
    session.commit()

print("-" * 100)
# Select
john = session.query(Student).filter(Student.name == "Eugene").first()
print(john.faculty.name)
print(john.faculty.id)


# More examples #########################################################
print("-" * 100)
# SQL example 1
# SELECT name, age FROM students WHERE faculty_id IS NULL;
# SELECT name, age FROM students WHERE name LIKE %@gmail%;
results = session.query(Student).filter(Student.faculty_id.is_(None)).all()
# results = session.query(Student).filter(Student.faculty_id.like("%gmail%")).all()
print(results)

print("-" * 100)

# SQL example 2, faculties without students
# SELECT faculty.name FROM faculty JOIN faculty.id = students.faculty_id;
results = session.query(Faculty) \
          .outerjoin(Student, Student.faculty_id == Faculty.id) \
          .filter(Student.id.is_(None)) \
          .all()

print(results)

print("-" * 100)
# SQL example 4
# SELECT name
# CASE
#    WHEN age <= 18 THEN 'Minor'
#    ELSE 'Adult'
# END AS age_status
# FROM students;
results = session.query(Student.name, case(
    (Student.age < 18, 'Minor'),
    else_='Adult'
).label('age_status')).all()
for student, status in results:
    print(f"Student {student}, age status: {status}")

print("-" * 100)
# SQL example 5, subqueries (nested query)
# SELECT name, age
# FROM students
# WHERE age > (SELECT AVG(age) FROM students);
avg_age_subquery = session.query(func.avg(Student.age)).scalar_subquery()
results = session.query(Student).filter(Student.age > avg_age_subquery).all()
for student in results:
    print(f"Student: {student.name}, age: {student.age}")

