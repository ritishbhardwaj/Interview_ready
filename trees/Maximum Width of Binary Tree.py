from typing import *
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Pair():
    def __init__(self,level:int,node:TreeNode):
        self.first=level
        self.second=node
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue=[]
        queue.append([Pair(0,root)])
        width=0
        # left=0
        # right=0
        while queue!=[[]]:
            sub_q=[]
            left=queue[0][0].first
            right=queue[0][len(queue[0])-1].first
            width=max(width,right-left+1)
            for q in queue[0]:
                R=q.second
                val=q.first
                i=val-left
                if R.left!=None:
                    sub_q.append(Pair(2*i+1,R.left))
                if R.right!=None:
                    sub_q.append(Pair(2*i+2,R.right))
            queue.pop(0)

            queue.append(sub_q)

        print(width)
            
                
            


root=TreeNode(3)
root.right=TreeNode(1)
root.left=TreeNode(5)
root.left.left=TreeNode(6)
root.left.right=TreeNode(2)
root.right.right=TreeNode(8)
root.left.right.left=TreeNode(7)
root.right.left=TreeNode(0)
root.left.right.right=TreeNode(4)

obj=Solution()
obj.widthOfBinaryTree(root)