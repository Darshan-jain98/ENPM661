from pickle import GLOBAL
import numpy as np


Goal_node = []
Start_node = []
back_track = []

#Function to check the location of Blank tile
def Blank_tile_locator(node):
    grid = np.reshape(node,(3,3))
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 0:
                row = i
                col = j
    
    return([row,col])

#Function to move the blank tile left 
def Move_left(node):
    row = Blank_tile_locator(node)[0]
    col = Blank_tile_locator(node)[1]
    if col != 0:
        node[row][col-1],node[row][col] = node[row][col],node[row][col-1]
        return node
    else:
        return node

#Function to move the blank tile right
def Move_right(node):
    row = Blank_tile_locator(node)[0]
    col = Blank_tile_locator(node)[1]
    if col != 2:
        node[row][col],node[row][col+1] = node[row][col+1],node[row][col]
        return node
    else:
        return node

#Function to move the blank tile up
def Move_up(node):
    row = Blank_tile_locator(node)[0]
    col = Blank_tile_locator(node)[1]
    if row != 0:
        node[row-1][col],node[row][col] = node[row][col],node[row-1][col]
        return node
    else:
        return node

#Function to move the blank tile down
def Move_down(node):
    row = Blank_tile_locator(node)[0]
    col = Blank_tile_locator(node)[1]
    if row != 2:
        node[row+1][col],node[row][col] = node[row][col],node[row+1][col]
        return node
    else:
        return node

