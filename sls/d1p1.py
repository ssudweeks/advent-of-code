# Day 1 Puzzle 1
import os

sample_input = [ 
    199,200,208,210,200,207,240,269,260,263
]

my_file = open(os.path.join(os.getcwd(), 'sls', 'input', 'day1', 'input.txt'), "r")
content = my_file.readlines()
my_map = map(lambda x: int(x.rstrip()), content)
scott_input = list(my_map)


def count_increases(list):
    count = 0
    increased = 0
    decreased = 0
    while (count < len(list) -1):
        if list[count] < list[count + 1]:
            increased = increased + 1
        else:
            decreased = decreased + 1
        count = count + 1
    return increased

print(f'Sample Increased: {count_increases(sample_input)}')
print(f"Scott's input Increased: {count_increases(scott_input)}")
