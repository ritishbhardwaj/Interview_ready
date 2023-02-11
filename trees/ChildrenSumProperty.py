class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sol(root: TreeNode):
    if root==None: return 

    children_sum=0
    if root.left!=None and root.right!=None:
        children_sum=root.left.val + root.right.val
    elif root.left!=None and root.right==None:
        children_sum=root.left.val
    elif root.left==None and root.right!=None:
        children_sum=root.right.val
    else:
        return
    flag=False
    if children_sum<root.val:
        root.left.val=root.val
        root.right.val=root.val
        flag=True

    sol(root.left)
    sol(root.right)
    # if flag==True:
    root.val=root.left.val + root.right.val
    print(root.val)
     

root=TreeNode(40)
root.right=TreeNode(20)
root.left=TreeNode(10)
root.left.left=TreeNode(2)
root.left.right=TreeNode(5)
root.right.right=TreeNode(40)
# root.left.right.left=TreeNode(7)
root.right.left=TreeNode(30)
# root.left.right.right=TreeNode(4)


sol(root)