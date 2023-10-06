'''-> Given an array of numbers which are sorted find the largest subarray such that the difference between abs(maximum-minimum)<=K 

Observation :- abs[1-1] <= abs[1-2] <=abs[1-3] <=...abs[1-N]
'''


def max_view(arr:list,k):
    n=len(arr)
    i=j=0
    small=arr[i]
    greater=arr[j]
    cnt=0
    lastangle=arr[-1]
    totallimit=lastangle+k
    for k in arr:
        newangle=k+360
        if newangle<=totallimit:
            arr.append(newangle)
        else:
            break

    while j<n-1:

        #calculations
        diff=greater-small

        if diff<=k:
            cnt=max(cnt,j-i+1)
            j+=1
            greater=arr[j]
        else:

            while i<n and diff > k:
                i+=1
                small=arr[i]
                diff=greater-small
    
    print(cnt)




max_view([1,9,20,25,60,165,355],30)

ArrOf_buildings_position_at_different_angles=[5,9,20,22,28,35,60,350,358,359,360,361]
angleOfView=30
max_view(ArrOf_buildings_position_at_different_angles,angleOfView)

arr=[1,10,23,65,165,270,359]
k=30
max_view(arr,k)