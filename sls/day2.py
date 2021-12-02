import helpers.input as input


sample_input = [ 
    'forward 5',
    'down 5',
    'forward 8',
    'up 3',
    'down 8',
    'forward 2'
]
scott_input = input.read_input(2)

def process_course(commands):
    distance = 0
    depth = 0
    for command in commands:
        value = int(command.split(' ')[1])
        if command.startswith('forward'):
            distance = distance + value
        if command.startswith('down'):
            depth = depth + value
        if command.startswith('up'):
            depth = depth - value

    return distance, depth

def process_course_properly(commands):
    distance = 0
    depth = 0
    aim = 0
    for command in commands:
        value = int(command.split(' ')[1])
        if command.startswith('forward'):
            distance = distance + value
            depth = depth + aim * value
        if command.startswith('down'):
            aim = aim + value
        if command.startswith('up'):
            aim = aim - value
    return distance, depth

distance, depth = process_course(sample_input)
print('Sample result:', distance * depth)
distance, depth = process_course(scott_input)
print("Scott's result:", distance * depth)


distance, depth = process_course_properly(sample_input)
print('Sample proper result:', distance * depth)
distance, depth = process_course_properly(scott_input)
print("Scott's result:", distance * depth)

