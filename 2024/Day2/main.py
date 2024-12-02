# Directionality
increasing = False
currently_safe = None
safe_count = 0
unsafe_count = 0
def in_range(input, a, b):
    return True if input >= a and input <= b else False

with open('input.txt') as file:
    line_no = 0
    for line in file:
        line_no += 1
        line_ints = line.split(' ')
        line_ints = [int(i) for i in line_ints]
        increasing = True if line_ints[0] < line_ints[1] else False
        currently_safe = True
        i = 1
        sort_asc, sort_desc = sorted(line_ints), sorted(line_ints, reverse=True)
        if line_ints not in (sort_asc, sort_desc):
            currently_safe = False
        while i < len(line_ints) and currently_safe:
            prev = line_ints[i - 1]
            curr = line_ints[i]
            if not in_range(abs(prev - curr), 1, 3) or prev == curr:
                currently_safe = False

            i += 1
        if currently_safe:
            safe_count += 1
        else:
            unsafe_count +=1
print(safe_count, unsafe_count)

