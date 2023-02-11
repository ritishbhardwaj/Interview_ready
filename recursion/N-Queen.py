from  typing import *
def isSafe(row,col,board,n):
    duplicate_reference_row=row
    duplicate_reference_col=col

    while row>=0 and col>=0:
        if board[col][row]=='Q': return False
        row-=1
        col-=1
    
    row=duplicate_reference_row
    col=duplicate_reference_col
    while col>=0:
        if board[col][row]=='Q': return False
        col-=1
    
    row=duplicate_reference_row
    col=duplicate_reference_col
    while row<n and col>=0:
        if board[col][row]=='Q': return False
        row+=1
        col-=1
    
    return True
from copy import *
def nqueen(col:int ,board:List[List] ,queen: int,ds:list, n: int):
    if col>=n:
        # b=deepcopy(board)

        ds.append([''.join(row) for row in board])
        return
    
    for row in range(0,n):
        if isSafe(row,col,board,n):
            board[col][row]='Q'
            # print(board)
            nqueen(col+1,board,queen,ds,n)
            board[col][row]='.'


col=0
number_of_queen=4
board=[['.']*number_of_queen for j in range(number_of_queen)]
# print(board)
ds=[]
length=len(board)
nqueen(col,board,number_of_queen,ds,length)
print(ds)