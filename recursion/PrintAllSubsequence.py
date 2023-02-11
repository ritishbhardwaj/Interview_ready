final=[]    # to store all occurances
def sol(ind,ds,arr):
    global final
    if ind>=len(arr):
        print(ds)
        final.append(list(ds))
        return
    ds.append(arr[ind])
    sol(ind+1,ds,arr)
    ds.remove(arr[ind])
    sol(ind+1,ds,arr)

arr=[3,1,2]
storage=[]

sol(0,storage,arr)
print(final)