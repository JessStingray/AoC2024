import re

def mul(substr):
    digits = substr.lstrip('mul(').rstrip(')').split(',')
    return int(digits[0]) * int(digits[1])

with open("input.txt") as file:
    list = re.findall('mul\(\d+,\d+\)', file.read())
    result = 0
    for item in list:
        result += mul(item)
    print(result)