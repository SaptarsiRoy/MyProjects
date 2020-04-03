import random
import time
import os

#function to display the board
def display(x):
    os.system("cls")
    print("\n\n\n")
    print("{} | {} | {}".format(x[6], x[7], x[8]))
    print("----------")
    print("{} | {} | {}".format(x[3], x[4], x[5]))
    print("----------")
    print("{} | {} | {}".format(x[0], x[1], x[2]))
    print("\n\n\n")


#function for player input and assignment
def player_input():
    while(True):
        print("Enter 'X' or 'O':")
        marker = input()
        if marker == 'X' or marker == 'O':
            if marker == 'X':
                return ("X", "O")
            else:
                return ("O","X")
        else:
            print("Wrong input!!!\n")



#function for checking if won
def win_check(board, marker):
    if board[0] == marker and board[1] == marker and board[2] == marker:
        return True
    elif board[3] == marker and board[4] == marker and board[5] == marker:
        return True
    elif board[6] == marker and board[7] == marker and board[8] == marker:
        return True
    elif board[0] == marker and board[3] == marker and board[6] == marker:
        return True
    elif board[1] == marker and board[4] == marker and board[7] == marker:
        return True
    elif board[2] == marker and board[5] == marker and board[8] == marker:
        return True
    elif board[0] == marker and board[4] == marker and board[8] == marker:
        return True
    elif board[6] == marker and board[4] == marker and board[2] == marker:
        return True
    else:
        return False


#function for randomly deciding which player to go choose_first
def choose_first():
    if random.randint(1,2) == 1:
        return 'Player 1'
    else:
        return 'Player 2'


#function to check if a free space is available
def space_check(board, position):
    return board[position] == ' '


#function to check if board is full or not
def full_board_check(board):
    return  ' ' not in board



#function to input player choice from 1-9
def player_choice(board):
    position = ' '
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input("Enter position:"))
    return position



#function to ask if they would play again
def replay():
    print("Do you want to play again?(y/n):")
    rep = input().lower()
    return rep == 'y'



#integrate all the above functions
while(True):
    print("---------------------\n\n")
    print("Welcome to TIC TAC TOE\n\n")
    print("---------------------\n\n")
    board = [" "] * 10
    display(board)
    turn = choose_first()
    m1, m2 = player_input()
    print("{} will go first\n".format(turn))
    play = input("Are you ready to play?(y/n):")
    start = (play == 'y')
    while start:
        if turn == 'Player 1':
            print("It's player 1's turn\n")
            pos = player_choice(board)
            board[pos - 1] = m1
            display(board)
            print("It's player 2's turn\n")
            pos = player_choice(board)
            board[pos - 1] = m2
            display(board)
        else:
            print("It's player 2's turn\n")
            pos = player_choice(board)
            board[pos - 1] = m2
            display(board)
            print("It's player 1's turn\n")
            pos = player_choice(board)
            board[pos - 1] = m1
            display(board)
        if win_check(board, m1):
            print("Player 1 has own\n\n")
            break
        elif win_check(board, m2):
            print("Player 2 has own\n\n")
            break
        elif full_board_check(board):
            print("It's a Draw\n\n")
            break
        else:
            pass
    if not replay():
        break
