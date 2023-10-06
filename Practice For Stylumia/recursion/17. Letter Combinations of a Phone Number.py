from typing import *
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        

        letters={
            2:["a","b","c"],
            3:["d","e","f"],
            4:["g","h","i"],
            5:["j","k","l"],
            6:["m","n","o"],
            7:["p","q","r","s"],
            8:["t","u","v"],
            9:["w","x","y","z"]
        }
        final_ans=[]
        def sol(ind,ds,number):
            nonlocal final_ans
            
            #base case
            if ind>=len(number):
                temp=""+ds
                final_ans.append(temp)
                return
            
            l=letters[int(number[ind])]
            for i in range(len(l)):
                # ds=ds+l[i]
                sol(ind+1,ds+l[i],number)
                



        ds=""
        sol(0,ds,digits)
        print(final_ans)
        return final_ans

obj=Solution()
print(obj.letterCombinations(digits = "237"))