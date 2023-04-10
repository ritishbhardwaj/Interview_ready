from typing import *
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q=[]
        q.append((beginWord,1))
        s=set(wordList)
        if beginWord in s:
            s.remove(beginWord)
            

        while q:
            query=q.pop(0)
            word=query[0]
            steps=query[1]
            print(word)

            if word==endWord:
                return steps
            n_word=list(word)
            for i in range(len(word)):
                original=n_word[i]
                for j in range(ord("a"),ord("z")+1):
                    
                    n_word[i]=chr(j)

                    if "".join(n_word) in s:
                        s.remove("".join(n_word))
                        q.append(("".join(n_word),steps+1))
                
                n_word[i]=original
        
        return 0


obj=Solution()
print(obj.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]))