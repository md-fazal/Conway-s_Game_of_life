from random import random
from time import sleep
import os
import copy


def random_board_state(height, width):
    """ 
        Creates a board of dimensions width x height in which all elements are initialized to zero
        int -> List
    """

    board = [[0 for i in range(width)] for j in range(height)]

    for i in range(height):
        for j in range(width):
            prob = random()
            if prob >= 0.5:
                board[i][j] = 1
    return board

def render(state):
    """
        Takes the current state of the board and prints it on the terminal
        List -> O/P
    """

    height = len(state)
    width  = len(state[0])

    for i in range(height):
        print("|", end="")
        for j in range(width):
            if state[i][j] == 1:
                print("# ", end="")
            else:
                print("  ", end="")
        print("|")

def next_state(state, i, j, sum):
    """
        generates the next state for an element
        changes list by reference
        list <-> list
    """
    if state[i][j] == 1 and (sum == 0 or sum == 1):
        state[i][j] = 0
    elif state[i][j] == 1 and ( sum == 2 or sum == 3):
        state[i][j] = 1
    elif state[i][j] == 1 and sum > 3:
        state[i][j] = 0
    elif state[i][j] == 0 and sum == 3:
        state[i][j] = 1

def valid_index(x, y, width, height):
    """
    returns true if x and y are in bounds else false
    ints -> bool
    """

    if x < 0 or y < 0:
        return False
    elif x >= height or y >= width:
        return False
     
    return True

def next_board_state(state):
    """
        Generates the next state of the board according to the four rules of Game of Life
        list -> list
    """

    S = copy.deepcopy(state)
    height = len(state)
    width  = len(state[0])

    for i in range(height):
        for j in range(width):
            if valid_index(i-1, j-1, width, height):
                A = state[i - 1][j - 1]
            else:
                A = 0

            if valid_index(i-1, j, width, height):
                B = state[i - 1][j]
            else:
                B = 0

            if valid_index(i-1, j+1, width, height):
                C = state[i - 1][j + 1]
            else:
                C = 0

            if valid_index(i, j-1, width, height):
                D = state[i][j - 1]
            else:
                D = 0

            if valid_index(i, j+1, width, height):
                F = state[i][j + 1]
            else:
                F = 0
            
            if valid_index(i+1, j-1, width, height):
                G = state[i + 1][j - 1]
            else:
                G = 0

            if valid_index(i+1, j, width, height):
                H = state[i + 1][j]
            else:
                H = 0

            if valid_index(i+1, j+1, width, height):
                I = state[i + 1][j + 1]
            else:
                I = 0

            sum = A + B + C + D + F + G + H + I
            
            next_state(S, i, j, sum)
    return S
    

w, h = int(input("Enter width:")), int(input("Enter Height:"))
os.system("cls")
B = random_board_state(h, w)

while True:
    render(B)
    B = next_board_state(B)
    sleep(0.05)
    os.system("cls")