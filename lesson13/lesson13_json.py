from pathlib import Path
import json

# data = {
#     "name": "John",
#     "age": 30,
#     "city": "New York",
#     "is_working": None
# }
#
data_path_file = Path('data/data.json').absolute()
#
# with open(data_path_file, 'w') as file:
#     json.dump(data, file, indent=4)


with open(data_path_file, 'r') as file:
    data = json.load(file)

print(data)

json_string = '{"name": "John", "age": 30, "city": "New York"}'
data = json.loads(json_string)
print(data)

data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

json_string = json.dumps(data)
print(json_string)
