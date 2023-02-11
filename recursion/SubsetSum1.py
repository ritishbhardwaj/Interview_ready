def sol(ind,n,arr,s,storage):
    if ind >= n:
        storage.append(int(s))
        return
    s+=arr[ind] 
    sol(ind+1,n,arr,s,storage)
    s-=arr[ind]
    sol(ind+1,n,arr,s,storage)


N = 5
arr= [2 ,5, 8,11,13]
initial_sum=0
storage=[]
sol(0,N,list(arr),initial_sum,storage)
s=sorted(storage)
print(s)