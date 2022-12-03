
def initialize_board(height, length):
    board = [["-" for i in range(length)] for j in range(height)]

    return board


def print_board(board):

    reverse_board = board[::-1]

    for i in reverse_board:
        for j in i:

            print(j, end=" ")
        print()
    return


def insert_chip(board, col, chip_type):

    for i in range(len(board)):

        if board[i][col] != "x" and board[i][col] != "o":

            board[i][col] = chip_type
            row = i

            return board, row


def check_if_winner(board, col, row, chip_type):

    count = 0
    count2 = 0

    for i in range(len(board)):

        if board[i][col] == chip_type:
            count += 1
        else:
            count = 0
        if count == 4:

            return 4

    for j in range(len(board[0])):

        if board[row][j] == chip_type:
            count2 += 1
        else:
            count2 = 0
        if count2 == 4:

            return 4

    return


def main():
    height = 0
    length = 0
    game_over = 'no'
    turns = 0

    while height < 4:
        print("What would you like the height of the board to be?")
        height = int(input())
    while length < 4:
        print("What would you like the length of the board to be?")
        length = int(input())

    turn_draw = height * length


    board = initialize_board(height, length)
    print_board(board)
    print()
    print('Player 1: x')
    print('Player 2: o')
    print()

    while game_over == 'no':
        print('Player 1: Which column would you like to choose?')
        col = int(input())
        board, row = insert_chip(board, col, 'x')
        print_board(board)
        winner = check_if_winner(board, col, row, 'x')
        turns += 1
        if winner == 4:
            print('Player 1 won the game!')

            break
        if turns == turn_draw:
            print('Draw. Nobody wins.')
            break

        print('Player 2: Which column would you like to choose?')
        col = int(input())
        board, row = insert_chip(board, col, 'o')
        print_board(board)
        winner = check_if_winner(board, col, row, 'o')
        turns += 1
        if winner == 4:
            print('Player 2 won the game!')
            break
        if turns == turn_draw:
            print('Draw. Nobody wins.')
            break


if __name__ == '__main__':
    main()

