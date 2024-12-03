# Directionality
increasing = False
currently_safe = None
safe_count = 0
unsafe_count = 0
def in_range(input, a, b):
    return True if input >= a and input <= b else False

def is_safe(line_ints):
    currently_safe = True
    sort_asc, sort_desc = sorted(line_ints), sorted(line_ints, reverse=True)
    if line_ints not in (sort_asc, sort_desc):
        currently_safe = False
    i = 1
    while i < len(line_ints) and currently_safe:
        prev = line_ints[i - 1]
        curr = line_ints[i]
        if not in_range(abs(prev - curr), 1, 3) or prev == curr:
            currently_safe = False
        i += 1

    return currently_safe

with open('input.txt') as file:
    line_no = 0
    for line in file:
        line_no += 1
        line_ints = line.split(' ')
        line_ints = [int(i) for i in line_ints]

        i = 1
        currently_safe = is_safe(line_ints)

        if currently_safe:
            safe_count += 1
        else:
            # Problem dampener
            if any([is_safe(line_ints[:i] + line_ints[i + 1:]) for i in range(len(line_ints))]):
                safe_count += 1
                continue
            unsafe_count +=1

print(safe_count, unsafe_count)

