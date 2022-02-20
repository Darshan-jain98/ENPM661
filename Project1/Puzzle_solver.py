import numpy as np
import time
start_time = time.time()
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
    N_N = np.copy(node)
    row = Blank_tile_locator(node)[0]
    col = Blank_tile_locator(node)[1]
    if col != 0:
        N_N[row][col-1],N_N[row][col] = N_N[row][col],N_N[row][col-1]
        return True,N_N
    else:
        return False,node

#Function to move the blank tile right
def Move_right(node):
    N_N = np.copy(node)
    row = Blank_tile_locator(node)[0]
    col = Blank_tile_locator(node)[1]
    if col != 2:
        N_N[row][col],N_N[row][col+1] = N_N[row][col+1],N_N[row][col]
        return True,N_N
    else:
        return False,node

#Function to move the blank tile up
def Move_up(node):
    N_N = np.copy(node)
    row = Blank_tile_locator(node)[0]
    col = Blank_tile_locator(node)[1]
    if row != 0:
        N_N[row-1][col],N_N[row][col] = N_N[row][col],N_N[row-1][col]
        return True,N_N
    else:
        return False,node

#Function to move the blank tile down
def Move_down(node):
    N_N = np.copy(node)
    row = Blank_tile_locator(node)[0]
    col = Blank_tile_locator(node)[1]
    if row != 2:
        N_N[row+1][col],N_N[row][col] = N_N[row][col],N_N[row+1][col]
        return True,N_N
    else:
        return False,node

#Function to check if the following case is solvable or not
def Parity_checker(node):
    Parity_count = 0
    for i in range(9):
        for j in range(i+1,9):
            if node[i] !=0 and node[j] !=0 and node[i]>node[j]:
                Parity_count +=1
    if (Parity_count%2 == 0):
        return True
    else:
        return False

#function to convert Given Matrix in to list form according to row 
def Mat_2_listr(Mat):
    lst = []
    n,m = np.shape(Mat)
    for i in range(n):
        for j in range(m):
            lst.append(Mat[i][j])
    return lst

#function to convert Given Matrix in to list form according to column
def Mat_2_listc(Mat):
    lst = []
    n,m = np.shape(Mat)
    for i in range(n):
        for j in range(m):
            lst.append(Mat[j][i])
    return lst

#function to check if the node is already visited or not
def checker(node):
    for i in range(len(visited_node)):
        if np.array_equal(node,visited_node[i][0]):
            return True
    return False

#variables to be used in function
# s = np.array([[4,1,3],[7,2,5],[0,8,6]])
start = np.array([[1,5,2],[4,0,3],[7,8,6]])
goal = np.array([[1,2,3],[4,5,6],[7,8,0]])
visited_node = []
back_track = []
D_S = ([[start,0,0]])
child = 1

# to see if the following instance is solvable or not
solvable = Parity_checker(Mat_2_listr(start))
# Main while loop that generate the solution
while True:
    # print(child)
    if (solvable == False):
        print("The following instance is not solvable")
        exit()
    else:
        node = D_S.pop(0)
        node_state = node[0]
        self_index = node[1]
        parent_index = node[2]
        if not checker(node_state):
            visited_node.append([node_state,self_index,parent_index])
        
#For moving the blank tile left        
        poss,l_move = Move_left(node_state)
        if poss:
            if np.array_equal(goal,l_move):
                visited_node.append([l_move,self_index,parent_index])
                break
        if poss:
            if not checker(l_move):
                D_S.append([l_move,child,self_index])
                child+=1
        
#For moving the blank tile right        
        poss,r_move = Move_right(node_state)
        if poss:
            if np.array_equal(goal,r_move):
                visited_node.append([r_move,self_index,parent_index])
                break
        if poss:
            if not checker(r_move):
                D_S.append([r_move,child,self_index])
                child+=1

#For moving the blank tile up
        poss,u_move = Move_up(node_state)
        if poss:
            if np.array_equal(goal,u_move):
                visited_node.append([u_move,self_index,parent_index])
                break
        if poss:
            if not checker(u_move):
                D_S.append([u_move,child,self_index])
                child+=1
#For moving the blank tile down
        poss,d_move = Move_down(node_state)
        if poss:
            if np.array_equal(goal,d_move):
                visited_node.append([d_move,self_index,parent_index])
                break
        if poss:
            if not checker(d_move):
                D_S.append([d_move,child,self_index])
                child+=1


# print(len(visited_node))
lst_ele = visited_node[-1]
back_track.append(lst_ele[0])
parent_ele = lst_ele[2]
while parent_ele !=0:
    for i in range(len(visited_node)):
        if visited_node[i][1] == parent_ele:
            node = visited_node[i]
            break
    back_track.append(node[0])
    parent_ele = node[2]
back_track.append(start)
back_track.reverse()
# print(len(back_track))
end_time = time.time()
print(end_time - start_time)

#Editing the nodePart file to contain the state of path to goal
with open("Project1/nodePath.txt", "r+") as f:
    f.truncate(0)
    for i in range(len(back_track)):
        lst = Mat_2_listc(back_track[i])
        str_lst = ""
        for j in lst:
            str_lst = str_lst + str(j) + " "
        f.write(str_lst) 
        # print(str_lst)
        f.write("\n")
    f.close

#Editing the Nodes file to contain the state of all nodes
with open("Project1/Nodes.txt", "r+") as f:
    f.truncate(0)
    for i in range(len(visited_node)):
        lst = Mat_2_listc(visited_node[i][0])
        str_lst = ""
        for j in lst:
            str_lst = str_lst + str(j) + " "
        f.write(str_lst) 
        f.write("\n")
    f.close

#Editing the NodesInfo file to contain the parent and child relationship of all the nodes
with open("Project1/NodesInfo.txt", "r+") as f:
    f.truncate(0)
    str_lst = "Node Index   Parent Node"
    f.write(str_lst) 
    f.write("\n")
    for i in range(len(visited_node)):
        str_lst = str(visited_node[i][1]) + "               " + str(visited_node[i][2])
        f.write(str_lst) 
        f.write("\n")
    f.close




