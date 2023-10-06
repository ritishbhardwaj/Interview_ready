def sol(ind,ds:list,target,arr,storage):
    
    if target==0 :
        if ds not in storage:
            storage.append(list(ds))
        return
    # if arr[ind]>target:
    #     return
    for i in range(ind,len(arr)):
        if arr[i]==arr[i-1] and i>ind: continue
        if arr[i] >target:
            break
        ds.append(arr[i])
        sol(i+1,ds,target-arr[i],arr,storage)
        ds.remove(arr[i])
        sol(i+1,ds,target,arr,storage)

candidates =  [10,1,2,7,6,1,5]
target = 8
storage=[]
ds=[]
sol(0,ds,target,sorted(candidates),storage)
print(storage)
# print(sum([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))