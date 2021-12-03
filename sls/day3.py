import helpers.input as input

scott_input = input.read_input(3)

sample_input = [
    '00100',
    '11110',
    '10110',
    '10111',
    '10101',
    '01111',
    '00111',
    '11100',
    '10000',
    '11001',
    '00010',
    '01010',
]


def transpose_input(input):
    result = [[row[i] for row in input ] for i in range(len(input[0]))]
    return result


def most_occuring(input):
    result = ''
    for row in input:
        zero = 0
        one = 0
        for c in row:
            if c == '0':
                zero = zero + 1
            else:
                one = one + 1
        if zero > one:
            result = f'{result}0'
        else:
            result = f'{result}1'
    return result


def least_occuring(input):
    result = ''
    for row in input:
        zero = 0
        one = 0
        for c in row:
            if c == '0':
                zero = zero + 1
            else:
                one = one + 1
        if zero > one:
            result = f'{result}1'
        else:
            result = f'{result}0'
    return result

def most_occuring_progressive(input):
    matches = input
    for x in range(len(input[0])):
        frequent_bits = most_occuring(transpose_input(matches))
        matches = filter_matches_at_position(matches, frequent_bits, x)
        if len(matches) == 1:
            return matches[0]

def least_occuring_progressive(input):
    matches = input
    for x in range(len(input[0])):
        frequent_bits = least_occuring(transpose_input(matches))
        matches = filter_matches_at_position(matches, frequent_bits, x)
        if len(matches) == 1:
            return matches[0]
    
def filter_matches_at_position(input, frequent_bits, match_position):
    matches = []
    for x in range(len(input)):
        if input[x][match_position] == frequent_bits[match_position]:
            matches.append(input[x])
    return matches

transposed_input = transpose_input(sample_input)
gamma_rate = most_occuring(transposed_input)
epislon_rate = least_occuring(transposed_input)
print(gamma_rate)
print(epislon_rate)
print(int(gamma_rate, 2) * int(epislon_rate,2))

transposed_input = transpose_input(scott_input)
gamma_rate = most_occuring(transposed_input)
epislon_rate = least_occuring(transposed_input)
print(gamma_rate)
print(epislon_rate)
print(int(gamma_rate, 2) * int(epislon_rate,2))


o2reading = most_occuring_progressive(sample_input)
c02reading = least_occuring_progressive(sample_input)
print(o2reading)
print(c02reading)
print(int(o2reading, 2) * int(c02reading, 2))


o2reading = most_occuring_progressive(scott_input)
c02reading = least_occuring_progressive(scott_input)
print(o2reading)
print(c02reading)
print(int(o2reading, 2) * int(c02reading, 2))