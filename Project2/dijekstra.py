import numpy as np
import cv2
import matplotlib as mpp

def In_obstacle(row,col):
    inCircle = False
    inHexagon = False
    inQuad = False
    
    #To check the point is in circle or not
    xc = 300
    yc = 250-185
    r = 40
    if (col - xc)*(col - xc) + (row - yc)*(row - yc) <= r*r:
        inCircle =  True
    else:
        inCircle =  False
    
    #To check the point is in Hexagon or not
    if col <= 235 and col >= 165:
        if row <= 0.577*col + 24.94 and row >= 0.577*col - 55.89:
            if row <= -0.577*col + 255.89 and row >= -0.577*col + 175.05:
                inHexagon =  True
            else:
                inHexagon =  False
        else:
            inHexagon =  False
    else:
        inHexagon =  False
    
    #To check the point is in Quad or not
    if row <= 0.316*col + 173.66:
        if row >= -1.231*col + 229.255:
            if row >= 0.857*col + 111.44 or (row <= 0.857*col + 111.44 and row <= -3.2*col + 436):
                inQuad =  True
            else:
                inQuad =  False
        else:
            inQuad =  False
    else:
        inQuad =  False

    if(inQuad or inCircle or inHexagon):
        return True
    else:
        return False

def Move_left(node):
    if (node[1] !=0 ):
        if (not In_obstacle(node[0],node[1]-1)):
            new_node = np.copy(node)
            new_node[1] = node[1] - 1
            return False,new_node
        else:
            return False,node
    else:
        return False,node

def Move_right(node):
    if (node[1] !=399 ):
        if (not In_obstacle(node[0],node[1]+1)):
            new_node = np.copy(node)
            new_node[1] = node[1] + 1
            return False,new_node
        else:
            return False,node
    else:
        return False,node
        
def Move_up(node):
    if(node[0] !=0):
        if (not In_obstacle(node[0] - 1, node[1])):
            new_node = np.copy(node)
            new_node[0] = node[0] - 1
            return True, new_node
        else:
            return False,node
    else:
        return False,node

def Move_down(node):
    if(node[0] !=249):
        if (not In_obstacle(node[0] + 1, node[1])):
            new_node = np.copy(node)
            new_node[0] = node[0] + 1
            return True, new_node
        else:
            return False,node
    else:
        return False,node

# initial_x = int(input("Enter x coordinate of initial node: "))
# initial_y = int(input("Enter y coordinate of initial node: ")) 
# Initial_row = 250 - initial_y
# Initial_col = initial_x
# goal_x = int(input("Enter x coordinate of goal node: "))
# goal_y = int(input("Enter y coordinate of goal node: "))
# Goal_row = 250 - goal_y
# Goal_col = goal_x

viz_matrix = np.zeros((250,400,3),np.uint8)
for i in range(250):
    for j in range(400):
        if In_obstacle(i,j):
            viz_matrix[249 - i][j] = (0,255,255)
print(In_obstacle(0,0))

# cv2.imshow('img',viz_matrix)
# cv2.waitKey(0)