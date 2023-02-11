from typing import *
class Solution:
    count=0
    def totalNQueens(self, n: int) -> int:
        # global count
        def nqueen(col:int , board:List[List] , queen:int , ds:list , n:int , leftR:List , upperBD:List , lowerBD: list):
            # nonlocal count
            if col>=n:
                # b=deepcopy(board)
                Solution.count+=1
                ds.append([''.join(row) for row in board])
                return
            
            for row in range(0,n):
                if leftR[row]==0 and upperBD[n-1+col-row]==0 and lowerBD[row+col]==0:
                    board[row][col]='Q'
                    leftR[row]=1
                    upperBD[n-1+col-row]=1
                    lowerBD[row+col]=1
                    nqueen(col+1, board , queen , ds, n , leftR, upperBD, lowerBD)
                    board[row][col]='.'
                    leftR[row]=0
                    upperBD[n-1+col-row]=0
                    lowerBD[row+col]=0

            
        col=0
        number_of_queen=n
        board=[['.']*number_of_queen for j in range(number_of_queen)]
        # print(board)
        ds=[]
        leftcheck=[0]*number_of_queen
        upper_backDiagnol_check=[0]*(2*number_of_queen-1)
        lower_backDiagnol_check=[0]*(2*number_of_queen-1)
        length=len(board)
        nqueen(col,board,number_of_queen,ds,length,leftcheck,upper_backDiagnol_check,lower_backDiagnol_check)
        print(ds)
        return Solution.count

obj=Solution()
ans=obj.totalNQueens(1)
print(ans)