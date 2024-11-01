from pony.orm import Database
from pony.orm import Required, Set, Optional

db = Database(provider='postgres', user='danilovets', password='12345', host='localhost', database='school4')

class Faculty(db.Entity):
    name = Required(str)
    students = Optional('Student')

class Student(db.Entity):
    name = Required(str)
    age = Optional(int)
    faculty = Optional("Faculty")

db.generate_mapping(create_tables=True)