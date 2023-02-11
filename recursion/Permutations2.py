def sol(pointer,arr,storage):
    if pointer >=len(arr):
        storage.append(list(arr))

    for i in range(pointer,len(arr)):
        arr[pointer],arr[i]=arr[i],arr[pointer]
        sol(pointer+1,arr,storage)
        arr[pointer],arr[i]=arr[i],arr[pointer]
    

nums = [1,2,3]
storage=[]
sol(0,nums,storage)
print(storage)