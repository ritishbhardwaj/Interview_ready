from collections import Counter
#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n): 
        Sn=((n+1)*n)//2
        Sn2=((n)*(n+1)*(2*n+1))//6
        
        l_s=0   #linear sum
        s_s=0   #square sum
        for i in range(len(arr)):
            l_s+=arr[i]
            s_s+=(arr[i]**2)
        
        x_y=l_s-Sn
        x2_y2=s_s-Sn2
        
        x__y=(x2_y2)//(x_y)
        
        rep=(x_y+x__y)//2
        mis=x__y - rep
        
        return (rep,mis)