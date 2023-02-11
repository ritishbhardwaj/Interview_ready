def sol(ind,arr,s,ds,storage):
    if ind>=len(arr):
        storage.append(list(ds))
        return 
    for i in range(ind,len(arr)):
        ds.append(arr[i])
        sol(i+1,arr,s,ds,storage)
        ds.remove(arr[i])

nums = [1,2,2]
initial_sum=0
storage=[[]]
ds=[]
sol(0,nums,initial_sum,ds,storage)
print(storage)