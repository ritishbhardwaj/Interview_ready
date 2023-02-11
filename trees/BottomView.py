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
    d={}
    queue.append(Pair(0,root))
    while queue:
        r=queue.pop(0)
        Node=r.node
        value=r.node.val
        R=r.row

        if R in d:
            d.update({R:value})
        else:
            d[R]=value
        
        if Node.left!=None:
            queue.append(Pair(R-1,Node.left))
        if Node.right!=None:
            queue.append(Pair(R+1,Node.right))

    ans=[]
    for i in sorted(d):
        ans.append(d[i])

    print(ans)
    return ans


root=TreeNode(1)
root.left=TreeNode(2)
root.left.left=TreeNode(4)
root.left.right=TreeNode(6)
root.right=TreeNode(3)
root.right.right=TreeNode(7)
root.right.left=TreeNode(5)


sol(root)