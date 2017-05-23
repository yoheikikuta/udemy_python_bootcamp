#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import random
from IPython.display import clear_output

def display_board(board=[1,2,3,4,5,6,7,8,9]):
    '''
    input:
        board: list representing the board configuration
    output:
        show the current board
    '''
    clear_output()
    print(" {} | {} | {} ".format(board[0],board[1],board[2]))
    print("- - - - - - -")
    print(" {} | {} | {} ".format(board[3],board[4],board[5]))
    print("- - - - - - -")
    print(" {} | {} | {} ".format(board[6],board[7],board[8]))

def player_input():
    '''Choose the markers for each player'''
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        print("\nSelect your maker X or O.")
        time.sleep(0.1)
        marker = input()
        clear_output()
    if marker == 'X':
        return ('X', 'O')
    elif marker == 'O':
        return ('O', 'X')

def place_marker(board, marker, position):
    '''
    input:
        board: list representing the board configuration
        marker: the marker type will be placed on the board
        marker: the position on the board where the marker will be placed
    output:
        board: updated board
    '''
    board[int(position)-1] = marker
    return board

def win_check(board,marker):
    '''
    input:
        board: list representing the board configuration
        marker: the target marker to be checked if wins or not
    output:
        Boolean whether the target marker wins
    '''
    if (board[0] == board[1] == board[2] == marker) or (board[3] == board[4] == board[5] == marker) or (board[6] == board[7] == board[8] == marker):
        return True
    elif (board[0] == board[3] == board[6] == marker) or (board[1] == board[4] == board[7] == marker) or (board[2] == board[5] == board[8] == marker):
        return True
    elif (board[0] == board[4] == board[8] == marker) or (board[2] == board[4] == board[6] == marker):
        return True
    else:
        return False

def choose_first():
    '''Randomly select player 1 or 2'''
    player = random.randint(1,2)
    print("\nPlayer {} is the first player.".format(player))

def space_check(board, position):
    '''
    input:
        board: list representing the board configuration
        position: the position to be checked the validity
    output:
        Boolean whether the board is filled with the markers
    '''
    if ( board[position-1] != 'X' ) and ( board[position-1] != 'O' ):
        return True
    else:
        return False

def full_board_check(board):
    '''
    input:
        board: list representing the board configuration
    output:
        Boolean whether the board is filled with the markers
    '''
    unique_set = set(board)
    if len(unique_set) == 2:
        return True
    else:
        return False

def player_choice(board):
    '''
    input:
        board: list representing the board configuration
    output:
        position: the position where the marker will be replaced
    '''
    def _type_check(var):
        return var in ['1','2','3','4','5','6','7','8','9']

    print("\nPlease choice the position (from 1 to 9) you will place the marker.")
    time.sleep(0.1)
    position = input()

    #type check
    while not _type_check(position):
        clear_output()
        print("\nPlease choice the position (from 1 to 9) you will place the marker.")
        time.sleep(0.1)
        position = input()

    #space check
    while not space_check(board, int(position)):
        clear_output()
        print("\nPlease choice a available position.")
        time.sleep(0.1)
        position = input()

        while not _type_check(position):
            clear_output()
            print("\nPlease choice the position (from 1 to 9) you will place the marker.")
            time.sleep(0.1)
            position = input()

    return position

def replay():
    '''Check wheter the game will be replayed or not'''
    print("\nType YES if you retry the game!")
    time.sleep(0.1)
    flg = input()
    if flg == 'YES':
        return True
    else:
        return False


if __name__ == '__main__':
    print('Welcome to Tic Tac Toe!')
    
    while True:
        # Set the game up here
        choose_first()
        markers = player_input()
        
        # Set initial board
        board = [1,2,3,4,5,6,7,8,9]
        display_board(board)

        # Start the game
        game_on = True
        while game_on:
            #Player 1 Turn
            position = player_choice(board)
            place_marker(board,markers[0],position)
            display_board(board)
            if win_check(board,markers[0]):
                print("\nWin {} side!!".format(markers[0]))
                break
            if full_board_check(board):
                print("\nThe game is draw!")
                break
            #Player2's turn.
            position = player_choice(board)
            place_marker(board,markers[1],position)
            display_board(board)
            if win_check(board,markers[1]):
                print("\nWin {} side!!".format(markers[1]))
                break
            if full_board_check(board):
                print("\nThe game is draw!")
                break

        time.sleep(0.1)
        # Replay check
        if not replay():
            break
