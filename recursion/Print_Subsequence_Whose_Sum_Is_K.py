collection=[]
def sol(ind,ds,arr,s,k):        

    if ind>=len(arr):
        if s==k:
            print(ds)
            collection.append(list(ds))
        return 
    ds.append(arr[ind])
    s+=arr[ind]
    sol(ind+1,ds,arr,s,k)
    ds.remove(arr[ind])
    s-=arr[ind]
    sol(ind+1,ds,arr,s,k)


a=[1,2,1]
sum=0
k=2
sol(0,[],a,sum,k)
print(collection)