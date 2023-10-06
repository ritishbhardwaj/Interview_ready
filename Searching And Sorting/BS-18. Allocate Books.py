def findPages(arr: [int], n: int, m: int) -> int:
    if m>n:
        return -1
    
    low,high=min(arr),sum(arr)

    while low<=high:
        mid=(low+high)//2
        

print(findPages([12,34,67,90],4,2))
print(findPages([25,46,28,49,24],5,4))