
left_list = []
right_list = []

# Load input from file

with open('input.txt') as file:
    for line in file:
        line_tup = line.split('   ') # Copy paste the gap
        left_list.append(int(line_tup[0]))
        right_list.append(int(line_tup[1]))

'''
"Pair up the smallest number in the left list with the smallest number in the right list, 
then the second-smallest left number with the second-smallest right number, and so on."

This is just sorting two arrays. 
'''
left_list.sort()
right_list.sort()

distance = 0
i = 0
while i < len(left_list):
    distance += abs(left_list[i] - right_list[i])
    i += 1

print(distance)

