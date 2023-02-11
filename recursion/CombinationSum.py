def sol(ind,arr,ds,target,s,storage):
    if ind>=len(arr):
        if  target==0:
            # print(ds)
            storage.append(list(ds))
        return
    if arr[ind]<=target:
        ds.append(arr[ind])
        s+=arr[ind]
        sol(ind,arr,ds,target-arr[ind],s,storage)
        ds.remove(arr[ind])
        s-=arr[ind]
    sol(ind+1,arr,ds,target,s,storage)

candidates = [2,3,6,4,1,7]
target = 7
sum=0
storage=[]
sol(0,candidates,[],target,sum,storage)
print(storage)
'''
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.'''