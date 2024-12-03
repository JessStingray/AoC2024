import re

def mul(substr):
    digits = substr.lstrip('mul(').rstrip(')').split(',')
    return int(digits[0]) * int(digits[1])

with open("input.txt") as file:
    list = re.findall('mul\(\d+,\d+\)|do\(\)|don\'t\(\)', file.read())
    result = 0
    current_mode = True
    for item in list:
        if item == "do()":
            current_mode = True
        elif item == "don't()":
            current_mode = False
        else:
            if current_mode:
                result += mul(item)
    print(result)