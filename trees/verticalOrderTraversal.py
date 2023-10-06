from dataclasses import dataclass

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

@dataclass
class Pair():
    x:int         # x means level
    y:int         # y means rows where root points to intersection of 0 level and left of it are negative val and right of it will be positive val
    node: TreeNode

class Solution:
    def verticalTraversal(self, root):        
        hashmap={}
        final_ans=[]
        queue=[]
        coordinate_x=0
        coordinate_y=0

        def traversal(root,x,y):
            nonlocal hashmap,queue
            if root==None:
                return
            queue.append(Pair(x,y,root))
            l=traversal(root.left,x+1,y-1)
            r=traversal(root.right,x+1,y+1)
                   

        traversal(root,coordinate_x,coordinate_y)
        print(queue)
        sub_ans=[]
        for pair in queue:
            if pair.y not in hashmap:
                hashmap[pair.y]=[(pair.x,pair.node.val)]
            else:
                hashmap[pair.y].append((pair.x,pair.node.val))
        hashmap_keys=sorted(hashmap)
        print(hashmap_keys," KEYS")
        print(hashmap)
        #sorting values according to question
        for k in hashmap_keys:
            hashmap[k]=sorted(hashmap[k])
        print(hashmap)
        for i in sorted(hashmap):
            val=hashmap[i]
            for j in val:
                sub_ans.append(j[1])
            final_ans.append(sub_ans)    
            sub_ans=[]
            
        print(final_ans)

        

root=TreeNode(1)
root.left=TreeNode(2)
root.left.left=TreeNode(4)
root.left.right=TreeNode(6)
root.right=TreeNode(3)
root.right.right=TreeNode(7)
root.right.left=TreeNode(5)

obj=Solution()
obj.verticalTraversal(root)
# p=Pair(1,root)
