from pathlib import Path

path = "/Users/danilovets/Personal/Hillel/aqa_hillel_1308/lesson13"
# path.split('/')

def sep():
    print("-" * 100)

current_dir = Path.cwd()
some_directory = Path("lesson13/data")
print(some_directory.name)
print(some_directory.absolute())

sep()
parent_dir = current_dir.parent
sep()
##########################################################################
for folder in parent_dir.iterdir():
    if folder.is_dir():
        print(folder.name)
        print(folder.absolute())

sep()
##########################################################################


