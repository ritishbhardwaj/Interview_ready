class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right
count=0 
class Solution:
    count=0
    def isSumProperty(self, root):
        counts=0
               
        def sol(root):
            nonlocal counts
            if root==None:return 0         
            children_sum=0
            if root.left!=None and root.right!=None:
                children_sum=root.left.data + root.right.data
            elif root.left!=None and root.right==None:
                children_sum=root.left.data
            elif root.left==None and root.right!=None:
                children_sum=root.right.data
            else:
                return 0
            
            sol(root.left)
            sol(root.right)
            
            if root.data==children_sum:
                Solution.count+=1
                print(Solution.count,'lvl')
               
        sol(root)
        # print(count)
        print(Solution.count)

root=TreeNode(40)
root.right=TreeNode(20)
root.left=TreeNode(20)
root.left.left=TreeNode(2)
root.left.right=TreeNode(5)
root.right.right=TreeNode(10)
root.right.left=TreeNode(10)

obj=Solution()
obj.isSumProperty(root)
