import sqlite3 as s3

### 1-to-M relationships
create_table_faculty = """
CREATE TABLE faculty (
    id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL UNIQUE
);
"""

create_table_students = """
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INTEGER,
    faculty_id INTEGER REFERENCES faculty(id) ON DELETE SET NULL
);
"""

### N-to-M relationships
create_table_courses = """
CREATE TABLE courses (
    id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    instructor VARCHAR(100)
);
"""

insert_into_table_courses = """
INSERT INTO courses (name, instructor)
VALUES
('Math 101', 'Dr. Jones'),
('History 102', 'Dr. Smith'),
('Biology 103', 'Dr. Jones2');
"""


create_table_enrollments = """
CREATE TABLE enrollments (
    student_id INTEGER REFERENCES students(id) ON DELETE CASCADE,
    courses_id INTEGER REFERENCES courses(id) ON DELETE CASCADE,
    enrollment_date DATE NOT NULL,
    PRIMARY KEY (student_id, courses_id)
);
"""

insert_into_table_enrollments = """
INSERT INTO enrollments (student_id, courses_id, enrollment_date)
VALUES
(1, 1, '2024-09-01'),
(1, 2, '2024-09-01'),
(2, 1, '2024-09-02'),
(2, 2, '2024-09-01');
"""

insert_into_table_faculty = """
INSERT INTO faculty (name)
VALUES
('Software Engineering'),
('Math'),
('Biology');
"""

insert_into_table_faculty1 = """
INSERT INTO faculty (name)
VALUES
('Chemistry'),
('Physics'),
('Football');
"""

insert_into_table_students = """
INSERT INTO students (name, age, faculty_id)
VALUES
('Alice', 17, 1),
('Bob', 17, 1),
('Eugene', 18, 2),
('Anna', 16, 3);
"""

insert_into_table_students_no_faculty = """
INSERT INTO students (name, age)
VALUES
('Andrii', 23),
('Sergiy', 24);
"""

select_from_students0 = """
SELECT * FROM students;
"""

select_from_students1 = """
SELECT students.name AS student, faculty.name AS faculty
FROM students
JOIN faculty ON students.faculty_id = faculty.id;
"""

select_from_students2 = """
SELECT courses.name AS course, COUNT(enrollments.student_id) AS students_count
FROM courses
LEFT JOIN enrollments ON courses.id = enrollments.courses_id
GROUP BY courses.name;
"""


update_students = """
UPDATE students SET grade = '2nd course' WHERE name = 'Bob';
"""

delete_students = """
DELETE FROM students WHERE id = 1;
"""

