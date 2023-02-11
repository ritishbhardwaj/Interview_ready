import sys
def sol(ind,k,arr):
    if ind==0: return 0

    maxsteps=sys.maxsize
    for j in range(1,k+1):
        if ind>j:
            jump=sol(ind-j,k,arr)+abs(arr[ind]-arr[ind-j])
            maxsteps=min(maxsteps,jump)
    print(maxsteps)
    # return maxsteps

h=[30,10,60,10,60,50,60,20,40]
n=len(h)
k=5
sol(n-1,k,h)
# print(ans)