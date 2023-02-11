class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#====================== MY Solution================
def sol(root,ds,Node):
    if root==None:
        return
    
    ds.append(root.val)
    sol(root.left,ds,Node)
    sol(root.right,ds,Node)
    if ds[-1]==Node:
        return ds
    else:
        ds.pop()
        return

#========================= Striver's Solution ==============
def sol2(root,ds,Node):
    if root==None:
        return False
    ds.append(root.val)
    if root.val==Node:
        return True

    if sol2(root.left,ds,Node) or sol2(root.right,ds,Node):
        return True
    
    ds.pop()
    return False



root=TreeNode(1)
root.left=TreeNode(2)
root.left.left=TreeNode(4)
root.left.right=TreeNode(6)
root.right=TreeNode(3)
root.right.right=TreeNode(7)
root.right.left=TreeNode(5)
root.right.left.right=TreeNode(10)
root.right.left.left=TreeNode(8)
root.right.left.left.right=TreeNode(9)
root.right.left.left.right.right=TreeNode(11)

ds=[]
Node=1
ans=sol(root,ds,Node)
print(ans,end=" ")
print(ds)
ds2=[]
ans2=sol2(root,ds2,Node)
print(ans2,ds2)
