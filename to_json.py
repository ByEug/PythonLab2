import json


def to_json(obj):
    if isinstance(obj, bool):
        obj = str(obj).lower()
    elif isinstance(obj, (int, float)):
        obj = str(obj)
    elif isinstance(obj, type(None)):
        obj = "null"
    elif isinstance(obj, str):
        obj = '"' + obj + '"'
    elif isinstance(obj, (tuple, list)):
        buffer = "["
        for item in obj:
            item = to_json(item)
            if buffer == "[":
                buffer = buffer + item
            else:
                buffer = buffer + ', ' + item
        buffer = buffer + "]"
        obj = buffer
    elif isinstance(obj, dict):
        buffer = "{"
        for key in obj:
            buffer_key = to_json(key)
            buffer_value = to_json(obj[key])
            if buffer == "{":
                buffer = buffer + buffer_key + ": " + buffer_value
            else:
                buffer = buffer + ", " + buffer_key + ": " + buffer_value
        buffer = buffer + "}"
        obj = buffer
    return obj


int_checker = 15
float_checker = 35.2
bool_checker = True
bool_checker_f = False
none_checker = None
str_checker = "hello"
tuple_checker = ("apple", "bananas")
list_checker = ["apple", "bananas"]
dict_checker = {"name": "John", "age": 30}

print(json.dumps(dict_checker))
print(json.dumps(list_checker))
print(json.dumps(tuple_checker))
print(json.dumps(str_checker))
print(json.dumps(int_checker))
print(json.dumps(float_checker))
print(json.dumps(bool_checker))
print(json.dumps(bool_checker_f))
print(json.dumps(none_checker) + '\n')

print(to_json(dict_checker))
print(to_json(list_checker))
print(to_json(tuple_checker))
print(to_json(str_checker))
print(to_json(int_checker))
print(to_json(float_checker))
print(to_json(bool_checker))
print(to_json(bool_checker_f))
print(to_json(none_checker))
