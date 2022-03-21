#!/usr/bin/env python3

from time import time
from turtle import color
from matplotlib import units
import numpy as np
import cv2
import heapq as hq
from math import cos, radians, sin, sqrt
import matplotlib.pyplot as plt

def in_obstacle(x,y):
    inCircle = False
    inHexagon = False
    inQuad = False

    #To check the point is in circle or not
    y_c = 185
    x_c = 300
    r = 40
    if (((x - x_c)*(x - x_c)) + ((y - y_c)*(y - y_c)) <= (r*r)):
        inCircle =  True
    else:
        inCircle =  False
    
    #To check the point is in Hexagon or not
    if x <= 235 and x >= 165 and (74*x - 175*y + 8825 >=0) and (74*x + 175*y - 38425 <=0) and (74*x - 175*y - 3425 <=0) and (74*x + 175*y - 26175 >=0):
        inHexagon = True
    else:
        inHexagon = False
    
    #To check the point is in Quad or not
    if ((25*x - 79*y + 13715 >= 0) and (6*x - 7*y + 780 <= 0) and (85*x + 69*y - 15825 >= 0)) or ((85*x + 69*y -15825>=0) and (16*x + 5*y - 2180<=0) and (25*x - 79*y + 13715 >=0)):
        inQuad =  True 
    else:
        inQuad = False
    
    if(inQuad or inCircle or inHexagon):
        return True
    else:
        return False

def in_clearance(x,y):
    inCircle = False
    inHexagon = False
    inQuad = False
    inboundry = False
    #To check the point is in circle or not
    y_c = 185
    x_c = 300
    r = 55
    if (((x - x_c)*(x - x_c)) + ((y - y_c)*(y - y_c)) <= (r*r)):
        inCircle =  True
    else:
        inCircle =  False
    
    #To check the point is in Hexagon or not
    if x <= 250 and x >= 150 and (74*x - 175*y + 11675 >=0) and (74*x + 175*y - 41275 <=0) and (74*x - 175*y - 6275 <=0) and (74*x + 175*y - 23324 >=0):
        inHexagon = True
    else:
        inHexagon = False
    
    #To check the point is in Quad or not
    if ((25*x - 79*y + 14957 >= 0) and (6*x - 7*y + 641 <= 0) and (85*x + 69*y - 14182 >= 0)) or ((85*x + 69*y -14182>=0) and (16*x + 5*y - 2431<=0) and (25*x - 79*y + 14957 >=0)):
        inQuad =  True 
    else:
        inQuad = False
    
    if x <= 15 or x >= 385 or y <= 15 or y >= 235:
        inboundry = True
    else:
        inboundry = False

    if(inQuad or inCircle or inHexagon or inboundry):
        return True
    else:
        return False


def ActionMoveLeft30(Node_State_i,step_size):
    New_Node_State_i = np.copy(Node_State_i)
    New_Node_State_i[0] = Node_State_i[0] + round(step_size*cos(radians(Node_State_i[2] + 30)))
    New_Node_State_i[1] = Node_State_i[1] + round(step_size*sin(radians(Node_State_i[2] + 30)))
    New_Node_State_i[2] = Node_State_i[2] + 30
    if in_clearance(New_Node_State_i[0],New_Node_State_i[1]):
        return False,False
    else:
        return True,tuple(New_Node_State_i)

def ActionMoveLeft60(Node_State_i,step_size):
    New_Node_State_i = np.copy(Node_State_i)
    New_Node_State_i[0] = Node_State_i[0] + round(step_size*cos(radians(Node_State_i[2] + 60)))
    New_Node_State_i[1] = Node_State_i[1] + round(step_size*sin(radians(Node_State_i[2] + 60)))
    New_Node_State_i[2] = Node_State_i[2] + 60
    if in_clearance(New_Node_State_i[0],New_Node_State_i[1]):
        return False,False
    else:
        return True,tuple(New_Node_State_i)

def ActionMoveForward(Node_State_i,step_size):
    New_Node_State_i = np.copy(Node_State_i)
    New_Node_State_i[0] = Node_State_i[0] + round(step_size*cos(radians(Node_State_i[2])))
    New_Node_State_i[1] = Node_State_i[1] + round(step_size*sin(radians(Node_State_i[2])))
    New_Node_State_i[2] = Node_State_i[2]
    if in_clearance(New_Node_State_i[0],New_Node_State_i[1]):
        return False,False
    else:
        return True,tuple(New_Node_State_i)

def ActionMoveRight30(Node_State_i,step_size):
    New_Node_State_i = np.copy(Node_State_i)
    New_Node_State_i[0] = Node_State_i[0] + round(step_size*cos(radians(Node_State_i[2] - 30)))
    New_Node_State_i[1] = Node_State_i[1] + round(step_size*sin(radians(Node_State_i[2] - 30)))
    New_Node_State_i[2] = Node_State_i[2] - 30
    if in_clearance(New_Node_State_i[0],New_Node_State_i[1]):
        return False,False
    else:
        return True,tuple(New_Node_State_i)

def ActionMoveRight60(Node_State_i,step_size):
    New_Node_State_i = np.copy(Node_State_i)
    New_Node_State_i[0] = Node_State_i[0] + round(step_size*cos(radians(Node_State_i[2] - 60)))
    New_Node_State_i[1] = Node_State_i[1] + round(step_size*sin(radians(Node_State_i[2] - 60)))
    New_Node_State_i[2] = Node_State_i[2] - 60
    if in_clearance(New_Node_State_i[0],New_Node_State_i[1]):
        return False,False
    else:
        return True,tuple(New_Node_State_i)

def distance(Node1,Node2):
    return round(sqrt((Node1[0]-Node2[0])**2 + (Node1[1]-Node2[1])**2))

def in_Goal_Threshold(Current_Node, Goal_Node):
    r = 5
    
    if (Goal_Node[0]-Current_Node[0])**2 + (Goal_Node[1]-Current_Node[1])**2 <= r**2:
        return True
    else:
        return False

# This function returns the index of a given node in open list
def find_index(Node_State_i,open_list):
    for i in range(len(open_list)):
        if open_list[i][1] == Node_State_i:
            return i
    return False

def generate_path(closed_list,path_dict):
    i = closed_list[-1][3]
    node_path = [closed_list[-1][1]]
    while i > 0:
        node_path.append(path_dict[i][0])
        i = path_dict[i][1]
    node_path.reverse()
    return node_path

while True:
    initial_x = int(input("Enter x coordinate of initial node in the range of 0-399: "))
    initial_y = int(input("Enter y coordinate of initial node in the range of 0-249: ")) 
    intial_angle = int(input("Enter Initial Angle: "))
    if in_clearance(initial_x,initial_y):
        print("The initial coordinates entered are in obstacle space. Please enter again.")
        continue
    else:
        while True:
            goal_x = int(input("Enter x coordinate of goal node in the range of 0-399: "))
            goal_y = int(input("Enter y coordinate of goal node in the range of 0-249: "))
            goal_angle = int(input("Enter Goal Angle: "))
            if in_clearance(goal_x,goal_y):
                print("The goal coordinates entered are in obstacle space. Please enter again.")
                continue
            else:
                break
        break

step_size = int(input("Enter step size: "))
initial_node = (initial_x,initial_y,intial_angle)
goal_node = (goal_x,goal_y,goal_angle)

# (tc,node,node_id,parent_id,c2c,c2g)
open_list = [[distance(initial_node,goal_node),initial_node,1,0,0,distance(initial_node,goal_node)]]
open_list_set = {initial_node}
hq.heapify(open_list)

closed_list = []
closed_list_set = set()
node_num = 1            # Variable used for Node index
path_dict = {}
itr = 1

viz_matrix = np.zeros((400,250,3),np.uint8)  # Visualization Matrix
nodes = [[initial_node]]    # List used to store the nodes explored in each iteration
# for i in range(400):
#     for j in range(250):
#         if in_clearance(i,j):
#             viz_matrix[i][j] = (255,255,255)
for i in range(400):
    for j in range(250):
        if in_obstacle(i,j):
            viz_matrix[i][j] = (255,0,0)

plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)
ax.imshow(cv2.flip(cv2.transpose(viz_matrix),0))
fig.canvas.draw()
fig.canvas.flush_events()

start_time = time()
while True:
    # itr = itr + 1
    Curr_Node = hq.heappop(open_list)
    Node_State_i = Curr_Node[1]
    open_list_set.remove(Node_State_i)
    Node_Index_i = Curr_Node[2]
    Node_c2c_i = Curr_Node[4]
    Node_c2g_i = Curr_Node[5]
    Node_Parent_Index_i = Curr_Node[3]
    Curr_Nodes = []
    print(Node_State_i) 

    if in_Goal_Threshold(Node_State_i,goal_node) and Node_State_i[2] - goal_angle <=45:
        closed_list.append(Curr_Node)
        closed_list_set.add(Node_State_i)
        path_dict[Node_Index_i] = [Node_State_i,Node_Parent_Index_i]
        break

    possible,New_Node_State_i = ActionMoveLeft60(Node_State_i,step_size)
    if possible and New_Node_State_i not in closed_list_set:
        New_Node_c2c_i = Node_c2c_i + 1
        New_Node_c2g_i = distance(New_Node_State_i,goal_node)
        New_Node_tc_i = New_Node_c2c_i + New_Node_c2g_i
        ax.plot((Node_State_i[0],New_Node_State_i[0]),(249-Node_State_i[1],249-New_Node_State_i[1]),'w')
        fig.canvas.draw()
        fig.canvas.flush_events()
        if New_Node_State_i in open_list_set:
            idx = find_index(New_Node_State_i,open_list)
            if New_Node_tc_i < open_list[idx][0]:
                open_list[idx][0] = New_Node_tc_i
                open_list[idx][3] = Node_Index_i
                open_list[idx][4] = New_Node_c2c_i
                open_list[idx][5] = New_Node_c2g_i
                hq.heapify(open_list)
        else:
            node_num = node_num + 1
            hq.heappush(open_list,[New_Node_tc_i,New_Node_State_i,node_num,Node_Index_i,New_Node_c2c_i,New_Node_c2g_i])
            hq.heapify(open_list)
            open_list_set.add(New_Node_State_i)
            Curr_Nodes.append(New_Node_State_i)
    
    possible,New_Node_State_i = ActionMoveLeft30(Node_State_i,step_size)
    if possible and New_Node_State_i not in closed_list_set:
        New_Node_c2c_i = Node_c2c_i + 1
        New_Node_c2g_i = distance(New_Node_State_i,goal_node)
        New_Node_tc_i = New_Node_c2c_i + New_Node_c2g_i
        ax.plot((Node_State_i[0],New_Node_State_i[0]),(249-Node_State_i[1],249-New_Node_State_i[1]),'w')
        fig.canvas.draw()
        fig.canvas.flush_events()
        if New_Node_State_i in open_list_set:
            idx = find_index(New_Node_State_i,open_list)
            if New_Node_tc_i < open_list[idx][0]:
                open_list[idx][0] = New_Node_tc_i
                open_list[idx][3] = Node_Index_i
                open_list[idx][4] = New_Node_c2c_i
                open_list[idx][5] = New_Node_c2g_i
                hq.heapify(open_list)
        else:
            node_num = node_num + 1
            hq.heappush(open_list,[New_Node_tc_i,New_Node_State_i,node_num,Node_Index_i,New_Node_c2c_i,New_Node_c2g_i])
            hq.heapify(open_list)
            open_list_set.add(New_Node_State_i)
            Curr_Nodes.append(New_Node_State_i)
    
    possible,New_Node_State_i = ActionMoveForward(Node_State_i,step_size)
    if possible and New_Node_State_i not in closed_list_set:
        New_Node_c2c_i = Node_c2c_i + 1
        New_Node_c2g_i = distance(New_Node_State_i,goal_node)
        New_Node_tc_i = New_Node_c2c_i + New_Node_c2g_i
        ax.plot((Node_State_i[0],New_Node_State_i[0]),(249-Node_State_i[1],249-New_Node_State_i[1]),'w')
        fig.canvas.draw()
        fig.canvas.flush_events()
        if New_Node_State_i in open_list_set:
            idx = find_index(New_Node_State_i,open_list)
            if New_Node_tc_i < open_list[idx][0]:
                open_list[idx][0] = New_Node_tc_i
                open_list[idx][3] = Node_Index_i
                open_list[idx][4] = New_Node_c2c_i
                open_list[idx][5] = New_Node_c2g_i
                hq.heapify(open_list)
        else:
            node_num = node_num + 1
            hq.heappush(open_list,[New_Node_tc_i,New_Node_State_i,node_num,Node_Index_i,New_Node_c2c_i,New_Node_c2g_i])
            hq.heapify(open_list)
            open_list_set.add(New_Node_State_i)
            Curr_Nodes.append(New_Node_State_i)
    
    possible,New_Node_State_i = ActionMoveRight30(Node_State_i,step_size)
    if possible and New_Node_State_i not in closed_list_set:
        New_Node_c2c_i = Node_c2c_i + 1
        New_Node_c2g_i = distance(New_Node_State_i,goal_node)
        New_Node_tc_i = New_Node_c2c_i + New_Node_c2g_i
        ax.plot((Node_State_i[0],New_Node_State_i[0]),(249-Node_State_i[1],249-New_Node_State_i[1]),'w')
        fig.canvas.draw()
        fig.canvas.flush_events()
        if New_Node_State_i in open_list_set:
            idx = find_index(New_Node_State_i,open_list)
            if New_Node_tc_i < open_list[idx][0]:
                open_list[idx][0] = New_Node_tc_i
                open_list[idx][3] = Node_Index_i
                open_list[idx][4] = New_Node_c2c_i
                open_list[idx][5] = New_Node_c2g_i
                hq.heapify(open_list)
        else:
            node_num = node_num + 1
            hq.heappush(open_list,[New_Node_tc_i,New_Node_State_i,node_num,Node_Index_i,New_Node_c2c_i,New_Node_c2g_i])
            hq.heapify(open_list)
            open_list_set.add(New_Node_State_i)
            Curr_Nodes.append(New_Node_State_i)
    
    possible,New_Node_State_i = ActionMoveRight60(Node_State_i,step_size)
    if possible and New_Node_State_i not in closed_list_set:
        New_Node_c2c_i = Node_c2c_i + 1
        New_Node_c2g_i = distance(New_Node_State_i,goal_node)
        New_Node_tc_i = New_Node_c2c_i + New_Node_c2g_i
        ax.plot((Node_State_i[0],New_Node_State_i[0]),(249-Node_State_i[1],249-New_Node_State_i[1]),'w')
        fig.canvas.draw()
        fig.canvas.flush_events()
        if New_Node_State_i in open_list_set:
            idx = find_index(New_Node_State_i,open_list)
            if New_Node_tc_i < open_list[idx][0]:
                open_list[idx][0] = New_Node_tc_i
                open_list[idx][3] = Node_Index_i
                open_list[idx][4] = New_Node_c2c_i
                open_list[idx][5] = New_Node_c2g_i
                hq.heapify(open_list)
        else:
            node_num = node_num + 1
            hq.heappush(open_list,[New_Node_tc_i,New_Node_State_i,node_num,Node_Index_i,New_Node_c2c_i,New_Node_c2g_i])
            hq.heapify(open_list)
            open_list_set.add(New_Node_State_i)
            Curr_Nodes.append(New_Node_State_i)
    
    nodes.append(Curr_Nodes)
    if len(open_list) == 0:
        print("No Solution Found")
        break
    else:
        closed_list.append(Curr_Node)
        closed_list_set.add(Node_State_i)
        path_dict[Node_Index_i] = [Node_State_i,Node_Parent_Index_i]
    
    # for i in nodes:
    #     for j in i:
    #         viz_matrix[j[0]][j[1]] = (0,0,255)
        # cv2.resize(cv2.flip(cv2.transpose(viz_matrix),0),(1280,720))
        # cv2.imshow('visualization',cv2.flip(cv2.transpose(viz_matrix),0))  # Exploration
        # cv2.waitKey(1)
    
    # if itr > 10:
    #     break

end_time = time()
node_path = generate_path(closed_list,path_dict)
print(node_path) 
print(end_time-start_time)
# cv2.imshow('visualization',cv2.flip(cv2.transpose(viz_matrix),0))
# cv2.waitKey(0)

# for i in nodes:
#     for j in i:
#        viz_matrix[j[0]][j[1]] = (0,0,255)
#     cv2.resize(cv2.flip(cv2.transpose(viz_matrix),0),(1280,720))
#     cv2.imshow('visualization',cv2.flip(cv2.transpose(viz_matrix),0))  # Exploration
#     cv2.waitKey(1)

# for i in node_path:
#     viz_matrix[i[0]][i[1]] = (0,255,0)

# img = cv2.flip(cv2.transpose(viz_matrix),0)

# plt.imshow(img)

for i in range(len(node_path)-1):
    # s = (node_path[i][1],249-node_path[i][0])
    s = (node_path[i][0],249-node_path[i][1])
    # n = (node_path[i+1][1],249-node_path[i+1][0])
    n = (node_path[i+1][0],249-node_path[i+1][1])
    print(s)
    print(n)
    # img = cv2.arrowedLine(cv2.flip(cv2.transpose(viz_matrix),0),s,n,color=(255,255,255),thickness=9)
    # plt.quiver(s[0],s[1],n[0],n[1],color='r')
    ax.plot((s[0],n[0]),(s[1],n[1]),'g')
    fig.canvas.draw()
    fig.canvas.flush_events()
    
    


# img2 = cv2.resize(img,(1280,720))
# cv2.imshow('visualization',img2)       # Final Path
# cv2.waitKey(0)

# plt.imshow(img)
# plt.show()
plt.pause(2)
fig.savefig("step5")