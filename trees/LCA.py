# from Print_Root_To_Node import sol2 as S
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#===============approach 1 path vali========
# def sol(root,x,y):
#     a1,a2=[],[]
#     S(root,a1,x)
#     S(root,a2,y)
#     n= len(a1) if len(a1)>len(a2) else len(a2)
#     for i in range(n):
#         if a1[i]==a2[i]:
#             continue
#         else:
#             print(a1[i-1])
#             break

#=============:== approach 2 efficient way =============
def sol3(root,x,y):
    if root==None or root.val==x or root.val==y:
        return root
    
    lca1=sol3(root.left,x,y)
    lca2=sol3(root.right,x,y)

    if lca1==None:
        return lca2
    elif lca2==None:
        return lca1
    else:
        return root


root=TreeNode(3)
root.right=TreeNode(1)
root.left=TreeNode(5)
root.left.left=TreeNode(6)
root.left.right=TreeNode(2)
root.right.right=TreeNode(8)
root.left.right.left=TreeNode(7)
root.right.left=TreeNode(0)
root.left.right.right=TreeNode(4)

x=7
y=4
# sol(root,x,y)

ans2=sol3(root,x,y)
print(ans2.val,'<----sol3')