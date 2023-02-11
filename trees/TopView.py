from dataclasses import dataclass

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @dataclass
# class Pair():
#     row:int   
#     node: TreeNode
class Pair():
    def __init__(self,row,node):
        self.row=row
        self.node=node

def sol(root):
    queue=[]
    row=0
    queue.append(Pair(row,root))
    hashmap={}
    while queue!=[]:
        r=queue.pop(0)
        Node=r.node
        R=r.row
        if R not in hashmap:
            hashmap[R]=Node.val
        
        if Node.left != None:
            queue.append(Pair(R-1,Node.left))
        if Node.right!=None:
            queue.append(Pair(R+1,Node.right))
    ans=[]    
    for i in sorted(hashmap):
        ans.append(hashmap[i])

    print(ans)




root=TreeNode(1)
root.left=TreeNode(2)
root.left.left=TreeNode(4)
root.left.right=TreeNode(6)
root.right=TreeNode(3)
root.right.right=TreeNode(7)
root.right.left=TreeNode(5)


sol(root)

