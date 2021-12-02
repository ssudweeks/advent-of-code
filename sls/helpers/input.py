import os


def read_input(day_number):
    my_file = open(os.path.join(os.getcwd(), 'sls', 'input', f'day{day_number}', 'input.txt'), "r")
    content = my_file.readlines()
    my_map = map(lambda x: x.rstrip(), content)
    scott_input = list(my_map)
    return scott_input