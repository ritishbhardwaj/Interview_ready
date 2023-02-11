

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def boundary_traversal(root,ans):
    ans=ans
    rans=[]
    if root == None:
        return ans
    else:
        ans.append(root.val)
    
    def left_nodes(root):
        nonlocal ans
        if root == None : return
        if root.left== None and root.right==None: return
        ans.append(root.val)
        l=left_nodes(root.left)
        if root.left==None: 
            r=left_nodes(root.right)


    def leaf_nodes(root):
        nonlocal ans
        if root == None: return 
        l=leaf_nodes(root.left)
        value=root.val
        if root.left==None and root.right==None:
            ans.append(value)
        r=leaf_nodes(root.right)

    def right_nodes(root):
        nonlocal ans,rans
        if root == None : return 
        if root.left==None and root.right== None: return
        rans.append(root.val)
        r=right_nodes(root.right)
        if root.right==None:
            r=right_nodes(root.left)
        # else:
        #     r=right_nodes(root.right)

    left_nodes(root.left)
    right_nodes(root.right)
    leaf_nodes(root)

    for i in range(len(rans)-1,-1,-1):
        ans.append(rans[i])

    print(ans,rans)


root=TreeNode(1)
# root.right=TreeNode(7)
# root.right.right=TreeNode(8)
# root.right.right.right=TreeNode(21)
# root.right.right.left=TreeNode(9)
# root.right.right.left.right=TreeNode(11)
# root.right.right.left.left=TreeNode(10)
# root.left=TreeNode(2)
# root.left.left=TreeNode(3)
# root.left.left.right=TreeNode(4)
# root.left.left.right.left=TreeNode(5)
# root.left.left.right.right=TreeNode(6)
# root.left.left.right.right.left=TreeNode(21)

ans=[]

boundary_traversal(root,ans)

print(ans)

# print(eval([1,2,[3,4,[5]]]))