from functools import lru_cache

@lru_cache
def sol(ds,nums,storage,freq,n):
    if len(ds)==n:
        storage.append(list(ds))
        return
    for i in range(n):
        if freq[i]==0:
            freq[i]=1
            ds.append(nums[i])
            sol(ds,nums,storage,freq,n)
            ds.remove(nums[i])
            freq[i]=0


nums = [1,2,3,4,5,6,7,8,24]
ds=[]
storage=[]
freq=[0 for i in range(len(nums))]

n=len(nums)
sol(ds,nums,storage,freq,n)
print(storage)
# from itertools import permutations
# a=(permutations(nums))
# for i in a:
#     print(i)
