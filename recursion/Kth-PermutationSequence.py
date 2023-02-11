class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        k=k
        def sol(ind,arr,n):
            nonlocal k
            if ind>=n:
                print(arr)
                k-=1
                if k==0:
                    print(''.join(arr))
                    return True
                return 
            for i in range(ind,n):
                swap(arr,ind,i)
                if sol(ind+1,arr,n)==True : return True
                swap(arr,ind,i)


        def swap(arr,i,j):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
        
        ind=0
        arr=[str(i) for i in range(1,n+1)]
        n=len(arr)
        sol(ind,arr,n)

obj=Solution()
obj.getPermutation(9,236956)
