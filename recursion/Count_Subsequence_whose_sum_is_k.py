def sol(ind,arr,s,k):
    if ind>=len(arr):
        if s==k:
            return 1
        return 0

    s+=arr[ind]
    l=sol(ind+1,arr,s,k)
    s-=arr[ind]
    r=sol(ind+1,arr,s,k)
    return l+r

a=[1,2,1]
sum=0
k=2
ans=sol(0,a,sum,k)
print(ans)