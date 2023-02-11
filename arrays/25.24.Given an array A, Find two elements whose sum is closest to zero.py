import sys
def Solution(arr):
    arr=sorted(arr)
    l=0
    r=len(arr)-1
    closest_sum=sys.maxsize
    while l<r:
        curr_sum=arr[l]+arr[r]
        if abs(curr_sum)<abs(closest_sum):
            closest_sum=curr_sum
            min_l_index=l
            min_r_index=r
        if curr_sum>=0:
            r-=1
        if curr_sum<0 :
            l+=2

    print("sum:",arr[min_l_index]+arr[min_r_index],"& elements:",arr[min_l_index],arr[min_r_index], "respective indeces are:",min_l_index,min_r_index)


arr=[-2,9,6,1,-5,3,7,-6,15,-15,66]
# arr=[0,59,-9,69,-79,84]
Solution(arr)