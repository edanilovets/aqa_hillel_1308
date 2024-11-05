from pathlib import Path

def create_lesson(lesson_number):
    current_dir = Path.cwd()
    lesson_dir = current_dir / f"lesson{lesson_number}"
    lesson_dir.mkdir()
    print(f"New dir is created: {lesson_dir}")
    # create lesson file
    lesson_file = lesson_dir / f"lesson{lesson_number}.py"
    lesson_file.touch()
    return lesson_dir, lesson_file

if __name__ == "__main__":
    create_lesson(23)
    # lesson_file.unlink()
    # print("Deleted file", lesson_file)
    # lesson_dir.rmdir()
    # print("Deleted folder", lesson_dir)
