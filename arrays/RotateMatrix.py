from math import *
from collections import *
from sys import *
from os import *

def rotateMatrix(mat, n, m):
    
    if type(mat[0])==list:
        l= n if n<m else m    
        for i in range(l//2):
            working(i,n,m,mat)
            n-=1
            m-=1

    
    for j in mat:
        print(j)


def working(stPoint,row,col,grid):
    
    temp1=grid[stPoint][stPoint]

    r=stPoint  
    c=col
    for i in range(1,c):
        temp2=grid[r][i]
        grid[r][i]=temp1
        temp1=temp2

    r=row
    c=col-1
    for i in range(stPoint+1,r):
        temp2=grid[i][c]
        grid[i][c]=temp1
        temp1=temp2
    
    r=row
    c=col-1
    for i in range(c-1,stPoint-1,-1):
        temp2=grid[r-1][i]
        grid[r-1][i]=temp1
        temp1=temp2

    r=row-1
    c=stPoint
    for i in range(r-1,stPoint-1,-1):
        temp2=grid[i][c]
        grid[i][c]=temp1
        temp1=temp2


n=4 
m=4
mat=[[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12],
[13, 14, 15, 16]]
# rotateMatrix(mat,n,m)

n=1
m=4
mat=[5 ,6 ,7 ,8]
# rotateMatrix(mat,n,m)

n=4 
m=1
mat=[[5],[7]
,[3],
[2]]
# rotateMatrix(mat,n,m)

n=2
m=4
mat=[[1,2,3,4],[5,6,7,8]]
# rotateMatrix(mat,n,m)

n=8
m=8
mat=[[-12, 14, 5, 1, -7, 18, -4, 13 ],
[-7, 12, -4, 12, -14, 15, -11, 16 ],
[19, 16, -4, 16, -20, -15, -19, -19] ,
[9 ,-8 ,1 ,-17 ,13, 12, -9, 20] ,
[2 ,7 ,6, 0, 12, -15, -4, 8] ,
[-14 ,6 ,20, -11, 18, 11, 0 ,14] ,
[-12, -9, 6 ,7 ,-8 ,-5, 8, 14 ],
[-8, 9, -19, 12, -7, -15, 11, -14]]
rotateMatrix(mat,n,m)

'''-7 -12 14 5 1 -7 18 -4 
    19 16 12 -4 12 -14 15 13 
    9 -8 1 -4 16 -20 -11 16 
    2 7 6 0 -17 -15 -19 -19 
    -14 6 20 12 13 12 -9 20 
    -12 -9 -11 18 11 -15 -4 8 
    -8 6 7 -8 -5 8 0 14 
    9 -19 12 -7 -15 11 -14 14 
'''