from typing import *
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q=[]
        secondary_q=[]
        q.append((beginWord,1))
        secondary_q.append((beginWord,1))
        s=set(wordList)
        if beginWord in s:
            s.remove(beginWord)
        final_answe=[]

        def getList(arr):
            ans=[]
            ans.append(arr[0][0])
            ini=1
            for i in arr[1:len(arr)-1]:
                a=i[1]
                if ini+1==i[1]:
                    ans.append(i[0])
                    ini+=1
            ans.append(arr[-1][0])
            return ans

        while q:
            query=q.pop(0)
            word=query[0]
            steps=query[1]
            print(word)
            # print(secondary_q)
            if word==endWord:
                ans=getList(secondary_q)
                final_answe.append(ans)
            
            n_word=list(word)
            for i in range(len(word)):
                original=n_word[i]
                for j in range(ord("a"),ord("z")+1):
                    
                    n_word[i]=chr(j)

                    if "".join(n_word) in s:
                        s.remove("".join(n_word))
                        q.append(("".join(n_word),steps+1))
                        secondary_q.append(("".join(n_word),steps+1))
                
                n_word[i]=original
        print(secondary_q)
        print(final_answe)
        return 0
    
obj=Solution()
print(obj.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]))
