import numpy as np
import cv2
import matplotlib as mpp

def  inCircle(row,col):
    inCircle = False
    row_c = 65
    col_c = 300
    r = 45
    if (((col - col_c)*(col - col_c)) + ((row - row_c)*(row - row_c)) <= (r*r)):
        return True
    else:
        return False
# 1969425
# 51775
# 1069235
# 263635
def inHex(row,col):
    if col <= 235 and col >= 165 and (5053*col + 8750*row - 1969425 >=0) and (5053*col - 8750*row - 51775 <=0) and (2014*col +3500*row - 1069235 <=0) and (2014*col - 3500*row + 263635 >=0):
        return True
    else:
        return False

def inQuad(row,col):
    if ((25*col + 79*row -6035>=0) and (6*col + 7*row -970<=0) and (85*col - 69*row + 1425 >=0)) or ((25*col + 79*row -6035>=0) and (16*col - 5*row - 930<=0) and (85*col - 69*row + 1425 >=0)):
        return True 
    else:
        return False
    

viz_matrix = np.zeros((250,400,3),np.uint8)
for i in range(250):
    for j in range(400):
        if (inQuad(i,j)):
            viz_matrix[i][j] = (0,255,255)
# print(inHex(200,100) or inCircle(200,100) or inQuad(200,100))
# for i in range(190,210):
#     for j in range(90,110):
#         viz_matrix[i][j] = (255,255,255)
cv2.imshow('imgn',viz_matrix)
cv2.waitKey(0) 