##################################################################################
# Lesson13: working with files, pathlib

##################################################################################

# r - read
# w - write
# a - append
# r+ - read and write
# w+ - write and read
# a+ - append and read

# Writing in file
sql_query = """
SELECT * FROM users;
"""
with open('example1.txt', mode='a') as f:
    # print(type(f))
    # print(dir(f))
    f.write("Hello world\n")
    f.write("Hello world\n")
    f.write("Hello world\n")
    f.write(sql_query)

lines = [
  "Hello world 1",
  "Hello world 2",
  "Hello world 3\n",
  "Hello world 4\n",
]
with open('example2.txt', 'w') as f:
    # print(type(f))
    # print(dir(f))
    f.writelines(lines)

# Reading from file
with open('example1.txt', 'r') as f:
    content = f.read()
    print(content)

with open('example1.txt', 'r') as f:
    content = f.readlines()
    print(content)

##################################################################################
# r+ - read and write
# w+ - write and read
# a+ - append and read

with open('example3.txt', mode='w+') as f:
    f.write("Hello world\n")
    f.write("Hello world\n")

with open('example3.txt', mode='a+') as f:
    f.write("Append Hello world\n")
    f.write("Append Hello world\n")

##################################################################################
def read_ntn_line(file_path, line_number):
    with open(file_path, mode='r+') as f:
        for line_n, line_data in enumerate(f, start=1):
            if line_n == line_number:
                return line_data

line = read_ntn_line('data/some_data.txt', 5)
print(line)
##################################################################################
# Encoding
with open('example3.txt', mode='r', encoding="utf-8") as f:
    content = f.read()
    print(content)

spanish = "Hola, Mundo!\nBienvenidos al mundo de la codificación en ISO-8859-1.\n¡Adiós!"
with open('example4_spanish.txt', mode='w', encoding="ISO-8859-1") as f:
    f.write(spanish)

with open('example4_spanish.txt', mode='r', encoding="ISO-8859-1") as f:
    content = f.read()

