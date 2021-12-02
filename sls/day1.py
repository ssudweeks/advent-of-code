# Day 1 Puzzle 1
import os
import statistics

sample_input = [ 
    199,200,208,210,200,207,240,269,260,263
]

my_file = open(os.path.join(os.getcwd(), 'sls', 'input', 'day1', 'input.txt'), "r")
content = my_file.readlines()
my_map = map(lambda x: int(x.rstrip()), content)
scott_input = list(my_map)


def count_increases(list):
    counter = 0
    increased = 0
    while (counter < len(list) -1):
        if list[counter] < list[counter + 1]:
            increased = increased + 1
        counter = counter + 1
    return increased

def count_increases_by_3_avg(list):
    counter = 0
    increased = 0
    while (counter < len(list) -3):
        group_a = statistics.mean([
                list[counter],
                list[counter + 1],
                list[counter + 2]
                ])
        group_b = statistics.mean([
                list[counter + 1],
                list[counter + 2],
                list[counter + 3]
                ])
        if group_a < group_b:
            increased = increased + 1
        counter = counter + 1
    return increased

print(f'Sample Increased: {count_increases(sample_input)}')
print(f"Scott's input Increased: {count_increases(scott_input)}")

print(f'Sample average Increased: {count_increases_by_3_avg(sample_input)}')
print(f"Scott's input Increased: {count_increases_by_3_avg(scott_input)}")
