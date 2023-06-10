cnt=0
# cook your dish here
def sol(arr,dp,ind,nextind,cont):
    global cnt
    if ind==len(arr)-1 or nextind==len(arr)-1:
        subxor=str(arr[ind]^arr[nextind])
        # if subxor==subxor[::-1]:
        #     print(subxor)
        #     # print("yes")
        #     cnt+=1
        return
    takexor=str(arr[ind]^arr[nextind])
    if takexor==takexor[::-1]:
        # print("yes")
        # print(takexor)
        cnt+=1 
    take=sol(arr,dp,ind,nextind+1,cont)
    
    # nottake=sol(arr,dp,ind+1,nextind+1,cont)
    nottakexor=str(arr[ind+1]^arr[nextind+1])
    if nottakexor== nottakexor[::-1]:
        # print("yes")
        # print(nottakexor)
        cnt+=1 
    nottake=sol(arr,dp,ind+1,nextind+1,cont)

    
def count_palindrome_pairs(arr):
    count = 0
    n = len(arr)

    for i in range(n):
        for j in range(i, n):
            xor = arr[i] ^ arr[j]
            xor_str = bin(xor)[2:]  # Convert the XOR to binary representation
            if xor_str == xor_str[::-1]:
                count += 1

    return count


t=1
while t:
    t-= 1 
    n=4
    arr=[13 ,27 ,12, 26]
    dp=[[-1 for i in range(n)] for j in range(n)]
    sol(arr,dp,0,0,cnt)
    # ans=count_palindrome_pairs(arr)
    print(cnt)
    # print(ans)
    