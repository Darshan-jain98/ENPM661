import numpy as np
import cv2
from time import time
from random import seed
from random import randint

print("Welcome to Path finder")
print("The obstacles will be in dark color shade and the final path will be highlighted in white color")
#function to check if the point is in obstacle or not
def In_obstacle(row,col):
    inCircle = False
    inHexagon = False
    inQuad = False
    
    #To check the point is in circle or not
    row_c = 65
    col_c = 300
    r = 40
    if (((col - col_c)*(col - col_c)) + ((row - row_c)*(row - row_c)) <= (r*r)):
        inCircle = True
    else:
        inCircle = False
    
    #To check the point is in Hexagon or not
    if col <= 235 and col >= 165 and (5053*col + 8750*row -1969425 >=0) and (5053*col - 8750*row - 51775 <=0) and (2014*col +3500*row - 1069235 <=0) and (2014*col - 3500*row + 263635 >=0):
        inHexagon =True
    else:
        inHexagon =False
    
    #To check the point is in Quad or not
    if ((25*col + 79*row -6035>=0) and (6*col + 7*row -970<=0) and (85*col - 69*row + 1425 >=0)) or ((25*col + 79*row -6035>=0) and (16*col - 5*row - 930<=0) and (85*col - 69*row + 1425 >=0)):
        inQuad = True
    else:
        inQuad = False
        

    if(inQuad or inCircle or inHexagon):
        return True
    else:
        return False

#Function to move the node to left
def Move_left(node):
    if (node[1] !=0 ):
        if (not In_obstacle(node[0],node[1]-1)):
            new_node = np.copy(node)
            new_node[1] = node[1] - 1
            return True,tuple(new_node)
        else:
            return False,node
    else:
        return False,node

#Function to move the node to Right
def Move_right(node):
    if (node[1] !=399 ):
        if (not In_obstacle(node[0],node[1]+1)):
            new_node = np.copy(node)
            new_node[1] = node[1] + 1
            return True,tuple(new_node)
        else:
            return False,node
    else:
        return False,node

#Function to move the node to up
def Move_up(node):
    if(node[0] !=0):
        if (not In_obstacle(node[0] - 1, node[1])):
            new_node = np.copy(node)
            new_node[0] = node[0] - 1
            return True, tuple(new_node)
        else:
            return False,node
    else:
        return False,node

#Function to move the node to down
def Move_down(node):
    if(node[0] !=249):
        if (not In_obstacle(node[0] + 1, node[1])):
            new_node = np.copy(node)
            new_node[0] = node[0] + 1
            return True, tuple(new_node)
        else:
            return False,node
    else:
        return False,node

#Function to move the node to up left
def Move_upleft(node):
    if(node[0] !=0 and node[1] !=0):
        if(not In_obstacle(node[0]-1, node[1]-1)):
            new_node = np.copy(node)
            new_node[0] = node[0] - 1
            new_node[1] = node[1] - 1
            return True,tuple(new_node)
        else:
            return False,node
    else:
        return False,node

#Function to move the node to up right
def Move_upright(node):
    if(node[0] != 0 and node[1] !=  399):
        if(not In_obstacle(node[0]-1, node[1]+1)):
            new_node = np.copy(node)
            new_node[0] = node[0] - 1
            new_node[1] = node[1] + 1
            return True,tuple(new_node)
        else:
            return False, node
    else:
        return False,node

#Function to move the node to down left
def Move_downleft(node):
    if (node[0] != 249 and node[1] != 0):
        if(not In_obstacle(node[0]+1, node[1]-1)):
            new_node = np.copy(node)
            new_node[0] = node[0] + 1
            new_node[1] = node[1] - 1
            return True, tuple(new_node)
        else:
            return False, node
    else:
        return False, node

#Function to move the node to down right
def Move_downright(node):
    if(node[0] != 249 and node[1] != 399):
        if(not In_obstacle(node[0]+1,node[0]+1)):
            new_node = np.copy(node)
            new_node[0] = node[0] + 1
            new_node[1] = node[1] + 1
            return True, tuple(new_node)
        else:
            return False, node
    else:
        return False, node
   
#continues loop to take correct input for initial and goal node from user
while True:
    print("All the values should be between (0,399) for x and (0, 249) for y with origin at bottom right corner")
    initial_x = int(input("Enter x coordinate of initial node: "))
    initial_y = int(input("Enter y coordinate of initial node: ")) 
    Initial_row = 249 - initial_y
    Initial_col = initial_x
    goal_x = int(input("Enter x coordinate of goal node: "))
    goal_y = int(input("Enter y coordinate of goal node: "))
    Goal_row = 249 - goal_y
    Goal_col = goal_x
    if not In_obstacle(Initial_row,Initial_col):
        if not In_obstacle(Goal_row,Goal_col):
            break
    print("Enter valid input for initail and final position")


print("------------------")
print("Goal_row   Goal_col")
print(Goal_row,"         ", Goal_col)
print("------------------")

#dictionary to store the data for each node
# open_list = {(row,col): (self_index, parent_index, cost)}
# close_list = {(row,col): (self_index, parent_index, cost)}
open_list = {}
close_list = {}


#cost to move in diagnol and straight
cost_diagnol = 1.4
cost_straight = 1
open_list[(Initial_row,Initial_col)] = [1,0,0]
goal_node = (Goal_row,Goal_col)
node_count = 1
current_node = [Initial_row,Initial_col]
start_time = time()

print("Path finder has started")
# The main loop that generates the path
while True:
    # Function to pull the node with minimum cost from the open_list
    min_cost = np.inf
    for key,value in open_list.items():
        if open_list[key][2] <= min_cost:
            min_cost = open_list[key][2]
            current_node= list(key)

    current_index = open_list[tuple(current_node)][0]
    current_parent_index = open_list[tuple(current_node)][1]
    current_c2c = open_list[tuple(current_node)][2]
    data = open_list.pop(tuple(current_node))
    if (not In_obstacle(current_node[0],current_node[1])):
        close_list[(tuple(current_node))] = data
    if current_node[0] == goal_node[0] and current_node[1] == goal_node[1]:
        close_list[(current_node[0],current_node[1])] = data
        break
    
    #The following part of code sets the new node and appends it in open_list if not present or update its cost if present
    Poss,New_node = Move_left(current_node)
    if Poss:
        if not (New_node in close_list):
            if (New_node in open_list):
                if open_list[New_node][2] > round(current_c2c+cost_straight,2):
                    open_list[New_node][2] = round(current_c2c+cost_straight,2)
                    open_list[New_node][1] = current_index
            else:
                open_list[New_node] = [node_count,current_index,round(current_c2c+cost_straight,2)]
                node_count = node_count + 1

    Poss,New_node = Move_upleft(current_node)
    if Poss:
        if not (New_node in close_list):
            if (New_node in open_list):
                if open_list[New_node][2] > round(current_c2c+cost_diagnol,2):
                    open_list[New_node][2] = round(current_c2c+cost_diagnol,2)
                    open_list[New_node][1] = current_index
            else:
                node_count = node_count + 1
                open_list[New_node] = [node_count,current_index,round(current_c2c+cost_diagnol,2)]
    
    Poss,New_node = Move_up(current_node)
    if Poss:
        if not (New_node in close_list):
            if (New_node in open_list):
                if open_list[New_node][2] > round(current_c2c+cost_straight,2):
                    open_list[New_node][2] = round(current_c2c+cost_straight,2)
                    open_list[New_node][1] = current_index
            else:
                node_count = node_count + 1
                open_list[New_node] = [node_count,current_index,round(current_c2c+cost_straight,2)]
                
    Poss,New_node = Move_upright(current_node)
    if Poss:
        if not (New_node in close_list):
            if (New_node in open_list):
                if open_list[New_node][2] > round(current_c2c+cost_diagnol,2):
                    open_list[New_node][2] = round(current_c2c+cost_diagnol,2)
                    open_list[New_node][1] = current_index
            else:
                node_count = node_count + 1
                open_list[New_node] = [node_count,current_index,round(current_c2c+cost_diagnol,2)]
           
    Poss,New_node = Move_right(current_node)
    if Poss:
        if not (New_node in close_list):
            if (New_node in open_list):
                if open_list[New_node][2] > round(current_c2c+cost_straight,2):
                    open_list[New_node][2] = round(current_c2c+cost_straight,2)
                    open_list[New_node][1] = current_index
            else:
                node_count = node_count + 1
                open_list[New_node] = [node_count,current_index,round(current_c2c+cost_straight,2)]

    Poss,New_node = Move_downright(current_node)
    if Poss:
        if not (New_node in close_list):
            if (New_node in open_list):
                if open_list[New_node][2] > round(current_c2c+cost_diagnol,2):
                    open_list[New_node][2] = round(current_c2c+cost_diagnol,2)
                    open_list[New_node][1] = current_index
            else:
                node_count = node_count + 1
                open_list[New_node] = [node_count,current_index,round(current_c2c+cost_diagnol,2)]

    Poss,New_node = Move_down(current_node)
    if Poss:
        if not (New_node in close_list):
            if (New_node in open_list):
                if open_list[New_node][2] > round(current_c2c+cost_straight,2):
                    open_list[New_node][2] = round(current_c2c+cost_straight,2)
                    open_list[New_node][1] = current_index
            else:
                node_count = node_count + 1
                open_list[New_node] = [node_count,current_index,round(current_c2c+cost_straight,2)]
    
    Poss,New_node = Move_downleft(current_node)
    if Poss:
        if not (New_node in close_list):
            if (New_node in open_list):
                if open_list[New_node][2] > round(current_c2c+cost_diagnol,2):
                    open_list[New_node][2] = round(current_c2c+cost_diagnol,2)
                    open_list[New_node][1] = current_index
            else:
                node_count = node_count + 1
                open_list[New_node] = [node_count,current_index,round(current_c2c+cost_diagnol,2)]

    if(not bool(open_list)):
        print("solution not found")
        break
print("Path has been found know back tracking will start")

#The back_track part
close_lst = list(close_list.items())
back_track = [close_lst[-1][0]]
parent = close_lst[-1][1][1]

while parent !=0:
    for i in range(len(close_lst)):
        if close_lst[i][1][0] == parent:
            back_track.append(close_lst[i][0])
            parent = close_lst[i][1][1]
            break
print("Back tracking done now visualization will start")
end_time = time()
print("Time Taken to find a path and back Track it is: ",end_time-start_time)

# The visualization part
viz_matrix = np.zeros((250,400,3),np.uint8)
for i in range(250):
    for j in range(400):
        if In_obstacle(i,j):
            viz_matrix[i][j] = (randint(50,150),randint(100,150),randint(100,150))

cv2.imshow("img", viz_matrix)
cv2.waitKey(50)

for i in range(len(close_lst)):
    viz_matrix[close_lst[i][0][0],close_lst[i][0][1]] = (randint(100,150),randint(100,150),randint(50,100))
    cv2.imshow("img", viz_matrix)
    cv2.waitKey(1)

for i in range(len(back_track)):
    viz_matrix[back_track[i][0],back_track[i][1]] = (255,255,255)
    cv2.imshow("img", viz_matrix)
    cv2.waitKey(50)
cv2.waitKey(0)
print("Visualization done")
print("THANK YOU")