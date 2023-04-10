def sol():
    pass

n=5
grid=[["" for i in range((n*2)-1)] for i in range(n)]
# print(grid)
num=1
flag=False
for row in range(n):
    for col in range((row*2)+1):
        if row%2!=0:
            if col%2!=0:
                grid[row][(row*2)-col]="*"
                
            else:
                grid[row][(row*2)-col]=num
                num+=1

        else:
            if col%2!=0:
                grid[row][col]="*"
            else:
                grid[row][col]=num
                num+=1
# print(grid)
for i in range(len(grid)):
    print()
    for j in grid[i]:
        if j=="":
            break
        print(j,end=" ")
    