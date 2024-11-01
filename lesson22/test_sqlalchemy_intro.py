from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
import pytest

DATABASE_URL = "postgresql+psycopg2://danilovets:12345@localhost/school3"

Base = declarative_base()

class Faculty(Base):
    __tablename__ = "faculty"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(200), nullable=False)
    students = relationship('Student', back_populates='faculty')

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(200))
    age = Column(Integer)
    faculty_id = Column(Integer, ForeignKey("faculty.id", ondelete='SET NULL'))
    faculty = relationship('Faculty', back_populates='students')

    def __repr__(self):
        return f"Student(name={self.name}, age={self.age})"


@pytest.fixture()
def setup_db():
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

def test_create_new_student(setup_db):
    session = setup_db
    new_student = Student(name="John", age=26)
    session.add(new_student)
    session.commit()
    # SELECT COUNT() FROM students;
    assert session.query(Student).filter(Student.name == "John").count() == 1