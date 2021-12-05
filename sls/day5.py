import helpers.input as input

scott_input = input.read_input(5)

sample_input = [
    '0,9 -> 5,9',
    '8,0 -> 0,8',
    '9,4 -> 3,4',
    '2,2 -> 2,1',
    '7,0 -> 7,4',
    '6,4 -> 2,0',
    '0,9 -> 2,9',
    '3,4 -> 1,4',
    '0,0 -> 8,8',
    '5,5 -> 8,2'
]

def get_lines_data(input):
    lines = []
    for record in input:
        cordinates = record.split(' -> ')
        x1 = cordinates[0].split(',')[0]
        y1 = cordinates[0].split(',')[1]
        x2 = cordinates[1].split(',')[0]
        y2 = cordinates[1].split(',')[1]
        lines.append([[x1,y1], [x2,y2]])
    return lines

def get_max_x(line_data):
    max = 0
    for line in line_data:
        for cordinate in line:
            if int(cordinate[0]) > max:
                max = int(cordinate[0])
    return max


def get_max_y(line_data):
    max = 0
    for line in line_data:
        for cordinate in line:
            if int(cordinate[1]) > max:
                max = int(cordinate[1])
    return max

def build_board(max_x, max_y):
    board = []
    for y in range(max_y + 1):
        line = []
        for x in range(max_x + 1):
            line.append('.')
        board.append(line)
    return board

# For visiualation 
# X is second dimension, left to right (column)
# Y is first dimension, up to down (rows)
def draw_lines(line_data, board):
    for line in line_data:
        x1 = int(line[0][0])
        y1 = int(line[0][1])
        x2 = int(line[1][0])
        y2 = int(line[1][1])
        if (x1 == x2):#this determines horisontal line
            if y1 < y2:
                for y in range(y1, y2 + 1):
                    if board[y][x1] == '.':
                        board[y][x1] = '1'
                    else:
                        board[y][x1] = str(int(board[y][x1]) + 1)
            else:
                for y in range(y2, y1 + 1):
                    if board[y][x1] == '.':
                        board[y][x1] = '1'
                    else:
                        board[y][x1] = str(int(board[y][x1]) + 1)
        if (y1 == y2):#this determines vertical line
            if x1 < x2:
                for x in range(x1, x2 + 1):
                    if board[y1][x] == '.':
                        board[y1][x] = '1'
                    else:
                        board[y1][x] = str(int(board[y1][x]) + 1)
            else:
                for x in range(x2, x1 + 1):
                    if board[y1][x] == '.':
                        board[y1][x] = '1'
                    else:
                        board[y1][x] = str(int(board[y1][x]) + 1)

def draw_diagonal_lines(line_data, board):
    for line in line_data:
        x1 = int(line[0][0])
        y1 = int(line[0][1])
        x2 = int(line[1][0])
        y2 = int(line[1][1])
        if x1 != x2 and y1 != y2 :#this determines diagonal line
            if y1 > y2:
                y_movement = -1
                distance = y1 - y2
            else:
                y_movement = 1
                distance = y2 - y1
            if x1 > x2:
                x_movement = -1
                distance = x1 - x2
            else:
                x_movement = 1
                distance = x2 - x1
            count = 0
            while count < distance + 1:
                if board[y1 + count * y_movement][x1 + count * x_movement] == '.':
                    board[y1 + count * y_movement][x1 + count * x_movement] = '1'
                else:
                    board[y1 + count * y_movement][x1 + count * x_movement] = str(int(board[y1 + count * y_movement][x1 + count * x_movement]) + 1)
                count = count + 1
      

def count_overlapping_lines(board):
    ct = 0
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == '.':
                continue
            if int(board[y][x]) > 1:
                ct = ct + 1
    return ct

#line_data = get_lines_data(sample_input)
line_data = get_lines_data(scott_input)
max_x = get_max_x(line_data)
max_y = get_max_y(line_data)
board = build_board(max_x, max_y)

draw_lines(line_data, board)
draw_diagonal_lines(line_data, board)
#for row in board:
#    print(row)

print(count_overlapping_lines(board))