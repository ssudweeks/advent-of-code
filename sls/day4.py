import helpers.input as input

scott_input = input.read_input(4)

sample_input = [
'7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1',
'',
'22 13 17 11  0',
' 8  2 23  4 24',
'21  9 14 16  7',
' 6 10  3 18  5',
' 1 12 20 15 19',
'',
' 3 15  0  2 22',
' 9 18 13 17  5',
'19  8  7 25 23',
'20 11 10 24  4',
'14 21 16 12  6',
'',
'14 21 17 24  4',
'10 16 15  9 19',
'18  8 23 26 20',
'22 11 13  6  5',
' 2  0 12  3  7',
]

def seperate_input_boards(input):
    calls = input.pop(0)
    input.pop(0)
    boards = []

    board = []
    for x in range(len(input)):
        row = input[x]
        if row == '':
            boards.append(board)
            board = []
            continue
        else:
            board.append(input[x])
    boards.append(board)
    
    return calls, boards

def convert_to_playing_board(input):
    playing_board = []
    for r in range(len(input)):
        cells = input[r].split(' ')
        playing_board.append([[x, 0] for x in cells if x != ''])
    return playing_board

def mark_board(playing_board, call):
    for r in range(len(playing_board)):
        for c in range(len(playing_board[r])):
            if playing_board[r][c][0] == call:
                playing_board[r][c][1] = 1

def transpose_board(playing_board):
    return [[row[c] for row in playing_board] for c in range(len(playing_board[0]))]

def check_for_win_row(playing_board):
    for r in range(len(playing_board)):
        row_win = True
        c = 0
        while (row_win and c < len(playing_board[r])):
        #for c in range(len(playing_board[r])):
            if playing_board[r][c][1] == 0:
                row_win = False
            c = c + 1
        if row_win == True:
            return playing_board[r]

def call_bingo(board_number, winning_board, call):
    sum = 0
    for r in winning_board:
        for c in r:
            if c[1] == 0:
                sum = sum + int(c[0])
    proof = sum * int(call)
    print(f"BINGO<{proof}>! Board:{board_number}, call:{call}")
    exit()

def find_first_winning_board(calls, playing_boards, transposed_boards):
    for call in calls.split(','):
        for x in range(len(playing_boards)):
            mark_board(playing_boards[x], call)
            mark_board(transposed_boards[x], call)
            winning_row = check_for_win_row(playing_boards[x])
            if winning_row is not None:
                return x, playing_boards[x], call
            winning_row = check_for_win_row(transposed_boards[x])
            if winning_row is not None:
                return x, playing_boards[x], call

def find_last_winning_board(calls, playing_boards, transposed_boards):
    counter = 0
    while len(playing_boards) > 0:
        board_position, last_winning_board, final_call = find_first_winning_board(calls, playing_boards, transposed_boards)
        playing_boards.pop(board_position)
        transposed_boards.pop(board_position)
        counter = counter + 1
    return counter - 1, last_winning_board, final_call

calls, boards = seperate_input_boards(scott_input)
playing_boards = []
transposed_boards = []

for x in range(len(boards)):
    playing_boards.append(convert_to_playing_board(boards[x]))
    transposed_boards.append(transpose_board(playing_boards[x]))
    
#board_number, winning_board, final_call = find_first_winning_board(calls, playing_boards, transposed_boards)
#call_bingo(board_number, winning_board, final_call)

# 27936 is too high
#15456 is not the correct number
board_number, losing_board, final_call = find_last_winning_board(calls, playing_boards, transposed_boards)
call_bingo(board_number, losing_board, final_call)