def ispossible(arr:list,atleastDistance:int, totalCows:int):
    #pehli cow parhi hui hai arr[0] coordinate pe
    #aur agar mai doosri cow rakhne jaau kisi aur coordinate pe to uske hisaab se ye last one vali cow hogi
    lastCowCoordinate=arr[0]
    total_numberOfCows=1

    for i in range(1,len(arr)):

        if arr[i]-lastCowCoordinate >=atleastDistance:
            total_numberOfCows+=1
            lastCowCoordinate=arr[i]
        
        if total_numberOfCows>=totalCows:
            return True
    return False

def aggressiveCows(stalls, k):
    # Write your code here.
    stalls.sort()
    low=1
    high=stalls[-1]-stalls[0]

    ans=-1

    while low<=high:
        mid=(low+high)//2   # mid means the atleast distance between the two consecutive cows

        if ispossible(stalls,mid,k)==True:
            ans=mid
            low=mid+1
        else:
            high=mid-1

    return high,ans


print(aggressiveCows([0, 3 ,4 ,7 ,10, 9],4))
print(aggressiveCows([4,2,1,3,6],2))