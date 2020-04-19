import time
import random
import os

# ----------- Global Variable -------------

# AI global variable
from typing import List

otro = [0, 0]
count = 0
posx = [0]

# Game Board
board = [
    "-", "-", "-",
    "-", "-", "-",
    "-", "-", "-"
]

# If game is still going
game_still_going = True

# User Choosing X or O
current_player = None


# Multiplayer mode
def player():
    is_input_valid = True
    while is_input_valid:
        checks_player = input("What do you want to choose? (X/O) ")
        checks_player = checks_player.upper()

        if checks_player == "X" or checks_player == "O":
            is_input_valid = False
            return checks_player.upper()

        else:
            print("INVALID INPUT!!!")


# Display Board
def display_board():
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + '')
    print('---|---|---')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + '')
    print("---|---|---")
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + "\n")


# Play a game of Tic Tac Toe
def multi():
    global current_player

    time.sleep(0.5)
    current_player = player()
    time.sleep(0.5)
    display_board()
    time.sleep(0.5)

    # while game is still going
    while game_still_going:
        # handle a single turn of an arbitary player
        handle_turn(current_player)

        # check if the game has ended
        check_for_winner()
        check_if_tie()

        # Flip to the other player
        flip_player()

    # The game has ended
    if winner == "X" or winner == "O":
        print(winner + " won!")

    else:
        print("Tie.")


# Handle a single turn of an arbitary player
def handle_turn( player ):
    print(player + "'s turn.")
    time.sleep(0.2)
    err = True

    while err:
        position = input("Choose a position from 1-9: ")

        # Checks if input is valid or not
        if position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            err = True
            print("Invalid Input!!")
            time.sleep(0.5)
            print("Please,")

        # Checks if the position was empty or not
        elif board[int(position) - 1] != "-":
            err = True
            print("You can't go there.Try Again!")

        else:
            err = False

    position = int(position) - 1
    board[position] = player

    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():
    # Setting up global variable
    global winner

    # check row
    row_winner = check_row()

    # check column
    column_winner = check_column()

    # check diagonals
    diagonal_winner = check_diag()

    if row_winner or column_winner or diagonal_winner:
        winner = row_winner or column_winner or diagonal_winner

    else:
        # There was no win.
        winner = None

    return


def check_row():
    # Setting up global variable
    global game_still_going

    # Checking if all row have same value
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"

    if row1 or row2 or row3:
        game_still_going = False

    # Return the winner
    if row1:
        return board[0]
    if row2:
        return board[3]
    if row3:
        return board[6]

    return


def check_column():
    # Setting up global variable
    global game_still_going

    # Checking if all column have same value
    column1 = board[0] == board[3] == board[6] != "-"
    column2 = board[1] == board[4] == board[7] != "-"
    column3 = board[2] == board[5] == board[8] != "-"
    if column1 or column2 or column3:
        game_still_going = False

    # Return the winner
    if column1:
        return board[0]
    if column2:
        return board[1]
    if column3:
        return board[2]
    return


def check_diag():
    global game_still_going

    diag1 = board[0] == board[4] == board[8] != "-"
    diag2 = board[2] == board[4] == board[6] != "-"

    if diag1 or diag2:
        game_still_going = False
        return board[4]
    return


def check_if_tie():
    global game_still_going

    if "-" not in board:
        game_still_going = False

    return


# Flip the tuen of player
def flip_player():
    # Global variable we need
    global current_player

    # If the current player was x, then change it to o
    if current_player == "X":
        current_player = "O"

    # If the current player was o, then change it to x
    elif current_player == "O":
        current_player = "X"

    return


# Singleplayer Mode

def solo():
    def tabla():
        print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + '')
        print('---|---|---')
        print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + '')
        print("---|---|---")
        print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + "\n")

    pi = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    op1 = [1, 2, 3, 4, 6, 7, 8, 9]
    op2 = [5]
    op3 = [1, 3, 7, 9]
    op4 = [2, 4, 6, 8]

    rchai = [1, 3, 5, 7, 9]

    # Formas de ganar
    # horizontal
    wh1 = [1, 2, 3]
    vh1 = [1, 2, 3]
    wh2 = [4, 5, 6]
    vh2 = [4, 5, 6]
    wh3 = [7, 8, 9]
    vh3 = [7, 8, 9]
    Wh1 = [1, 2, 3]
    Wh2 = [4, 5, 6]
    Wh3 = [7, 8, 9]
    # vertical
    wv1 = [1, 4, 7]
    vv1 = [1, 4, 7]
    wv2 = [2, 5, 8]
    vv2 = [2, 5, 8]
    wv3 = [3, 6, 9]
    vv3 = [3, 6, 9]
    Wv1 = [1, 4, 7]
    Wv2 = [2, 5, 8]
    Wv3 = [3, 6, 9]
    # diagonal
    wd1 = [1, 5, 9]
    vd1 = [1, 5, 9]
    wd2 = [3, 5, 7]
    vd2 = [3, 5, 7]
    Wd1 = [1, 5, 9]
    Wd2 = [3, 5, 7]

    # Cuando gana la AI
    def win():
        if wh1.count("O") == 3:
            print("AI wins")
            quit()
        elif wh2.count("O") == 3:
            print("AI wins")
            quit()
        elif wh3.count("O") == 3:
            print("AI wins")
            quit()
        elif wv1.count("O") == 3:
            print("AI wins")
            quit()
        elif wv2.count("O") == 3:
            print("AI wins")
            quit()
        elif wv3.count("O") == 3:
            print("AI wins")
            quit()
        elif wd1.count("O") == 3:
            print("AI wins")
            quit()
        elif wd2.count("O") == 3:
            print("AI wins")
            quit()

    # Poner una X o una O
    def borrar( pos, a ):
        global count
        global otro
        if pos in wh1:
            wh1.remove(pos)
            vh1.remove(pos)
            wh1.append(a)
        if pos in wh2:
            wh2.remove(pos)
            vh2.remove(pos)
            wh2.append(a)
        if pos in wh3:
            wh3.remove(pos)
            vh3.remove(pos)
            wh3.append(a)
        if pos in wv1:
            wv1.remove(pos)
            vv1.remove(pos)
            wv1.append(a)
        if pos in wv2:
            wv2.remove(pos)
            vv2.remove(pos)
            wv2.append(a)
        if pos in wv3:
            wv3.remove(pos)
            vv3.remove(pos)
            wv3.append(a)
        if pos in wd1:
            wd1.remove(pos)
            vd1.remove(pos)
            wd1.append(a)
        if pos in wd2:
            wd2.remove(pos)
            vd2.remove(pos)
            wd2.append(a)
        count += 1
        if count == 9:
            print("It's a draw!")
            quit()

    # Movimiento de la AI
    def movai( pos ):
        posstr = str(pos)
        board.pop(pos - 1)
        pi.remove(posstr)
        board.insert(pos - 1, "O")
        pi.append("F")
        tabla()
        borrar(pos, "O")

    # MOVIMIENTOS
    # Primer movimiento del jugador
    def me1():
        
        err = True
        while err:
            position = input("Choose a position from 1-9: ")

            # Checks if input is valid or not
            if position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                err = True
                print("Invalid Input!!")
                time.sleep(0.5)
                print("Please,")

            # Checks if the position was empty or not
            elif board[int(position) - 1] != "-":
                err = True
                print("You can't go there.Try Again!")

            else:
                err = False
        position = int(position)
        while True:
            if str(position) in pi:
                board.pop(position - 1)
                pi.pop(position - 1)
                pi.append("F")
                board.insert(position - 1, "X")
                otro.pop(0)
                otro.insert(0, position)
                posx.append(position)
                posx.pop(0)
                print("\n")
                tabla()
                borrar(position, "X")
                break
            else:
                print('Error')
                position = int(input("Position: "))
        print("AI is thinking...")
        time.sleep(1)
        if position in op1:
            position = 5
            movai(position)
        elif position in op2:
            position = 1
            movai(position)

    def me():
        win()
        
        err = True
        while err:
            position = input("Choose a position from 1-9: ")

            # Checks if input is valid or not
            if position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                err = True
                print("Invalid Input!!")
                time.sleep(0.5)
                print("Please,")

            # Checks if the position was empty or not
            elif board[int(position) - 1] != "-":
                err = True
                print("You can't go there.Try Again!")

            else:
                err = False
        position = int(position)
        while True:
            if str(position) in pi:
                board.pop(position - 1)
                posstr = position
                pi.remove(str(posstr))
                if count == 2 or count == 3:
                    otro.pop(1)
                    otro.insert(1, position)
                pi.append("F")
                board.insert(position - 1, "X")
                print("\n")
                tabla()
                borrar(position, "X")
                posx.append(position)
                break
            else:
                print("You can't go there.Try Again!")
                position = int(input("Position: "))
        print("AI is thinking...")
        time.sleep(1)
        ai()

    def ai():
        pos = int(pi[0])
        if count == 0:
            pos = random.choice(rchai)
        elif (wh1.count("O") == 2) and len(vh1) == 1:
            pos = wh1[0]
        elif (wh2.count("O") == 2) and len(vh2) == 1:
            pos = wh2[0]
        elif (wh3.count("O") == 2) and len(vh3) == 1:
            pos = wh3[0]
        elif (wv1.count("O") == 2) and len(vv1) == 1:
            pos = wv1[0]
        elif (wv2.count("O") == 2) and len(vv2) == 1:
            pos = wv2[0]
        elif (wv3.count("O") == 2) and len(vv3) == 1:
            pos = wv3[0]
        elif (wd1.count("O") == 2) and len(vd1) == 1:
            pos = wd1[0]
        elif (wd2.count("O") == 2) and len(vd2) == 1:
            pos = wd2[0]
        else:
            if (wh1.count("X") == 2) and len(vh1) == 1:
                pos = wh1[0]
            elif (wh2.count("X") == 2) and len(vh2) == 1:
                pos = wh2[0]
            elif (wh3.count("X") == 2) and len(vh3) == 1:
                pos = wh3[0]
            elif (wv1.count("X") == 2) and len(vv1) == 1:
                pos = wv1[0]
            elif (wv2.count("X") == 2) and len(vv2) == 1:
                pos = wv2[0]
            elif (wv3.count("X") == 2) and len(vv3) == 1:
                pos = wv3[0]
            elif (wd1.count("X") == 2) and len(vd1) == 1:
                pos = wd1[0]
            elif (wd2.count("X") == 2) and len(vd2) == 1:
                pos = wd2[0]
            else:
                if f == 1 and count == 4:
                    if (('1' not in pi) and ('8' not in pi)) or (('9' not in pi) and ('4' not in pi)):
                        if board[6] == '-':
                            pos = 7
                    elif (('6' not in pi) and ('1' not in pi)) or (('9' not in pi) and ('2' not in pi)):
                        if board[2] == '-':
                            pos = 3
                    elif (('7' not in pi) and ('2' not in pi)) or (('3' not in pi) and ('4' not in pi)):
                        if board[0] == '-':
                            pos = 1
                    elif (('7' not in pi) and ('6' not in pi)) or (('3' not in pi) and ('8' not in pi)):
                        if board[8] == '-':
                            pos = 9
                    else:
                        if board[4] == '-':
                            pos = 5
                        elif board[2] == '-':
                            pos = 3
                        elif board[6] == '-':
                            pos = 7
                        else:
                            pos = int(pi[0])
                elif count == 3:
                    if (otro[0] == 1 and otro[1] == 8) or (otro[0] == 8 and otro[1] == 1):
                        pos = 7
                    elif (otro[0] == 1 and otro[1] == 6) or (otro[0] == 6 and otro[1] == 1):
                        pos = 3
                    elif (otro[0] == 7 and otro[1] == 2) or (otro[0] == 2 and otro[1] == 7):
                        pos = 1
                    elif (otro[0] == 7 and otro[1] == 6) or (otro[0] == 6 and otro[1] == 7):
                        pos = 9
                    elif (otro[0] == 9 and otro[1] == 2) or (otro[0] == 2 and otro[1] == 9):
                        pos = 3
                    elif (otro[0] == 9 and otro[1] == 4) or (otro[0] == 4 and otro[1] == 9):
                        pos = 7
                    elif (otro[0] == 3 and otro[1] == 4) or (otro[0] == 4 and otro[1] == 3):
                        pos = 1
                    elif (otro[0] == 3 and otro[1] == 8) or (otro[0] == 8 and otro[1] == 3):
                        pos = 9
                    elif (posx[0] in op3) and (posx[1] in op3):
                        if board[1] == '-':
                            pos = 2
                        elif board[3] == '-':
                            pos = 4
                    else:
                        if board[4] == '-':
                            pos = 5
                        elif board[2] == '-':
                            pos = 3
                        elif board[6] == '-':
                            pos = 7
                        else:
                            pos = int(pi[0])
                elif count == 2:
                    if posx[1] == 2 or posx[1] == 4:
                        pos = 9
                    elif posx[1] == 6 or posx[1] == 8:
                        pos = 1
                    elif board[4] == "X":
                        if board[0] == 'O':
                            pos = 9
                        elif board[2] == 'O':
                            pos = 7
                        elif board[6] == 'O':
                            pos = 3
                        elif board[8] == 'O':
                            pos = 1
                    else:
                        pos = 2
                else:
                    if board[4] == '-':
                        pos = 5
                    elif board[2] == '-':
                        pos = 3
                    elif board[6] == '-':
                        pos = 7
                    else:
                        pos = int(pi[0])
        movai(pos)

    f = 0
    while True:
        print("Who first? \n 1) Me\n 2) AI\n")
        arranca = input()
        print(" ")
        if arranca == "1":
            me1()
            me()
            me()
            me()
            me()
            break
        elif arranca == "2":
            f = 1
            ai()
            me()
            me()
            me()
            me()
            break
        else:
            time.sleep(0.5)
            print("INVALID INPUT!")
            print("Please try again!")
            time.sleep(1)


print("-------------------TIC TAC TOE---------------------")
time.sleep(0.5)
print("\n             Let' start the game.\n")
time.sleep(1)
print("The positions that will be used in this game are here:")
print(" 1 | 2 | 3 ")
print("---|---|---")
print(" 4 | 5 | 6 ")
print("---|---|---")
print(" 7 | 8 | 9 \n")
time.sleep(0.8)
turu = True
while turu:
    mode = input("In which mode do you want to play?\n 1) Solo Mode\n 2) Multiplayer Mode\n\n")
    if mode == "1":
        time.sleep(0.2)
        print("...\n")
        time.sleep(0.9)
        solo()
        turu = False
    elif mode == "2":
        time.sleep(0.2)
        print("...")
        time.sleep(0.9)
        multi()
        turu = False
    else:
        time.sleep(0.5)
        print("INVALID INPUT!")
        print("Please try again!")
        time.sleep(1)
