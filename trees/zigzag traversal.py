import queue
q1=queue.Queue(maxsize=100)        # maxsize is optional

# methods of Queues are .empty()   .full()   .put()   .get()  .qsize()

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zigzag_traversal(root):
    q=[]
    flag=0   # it means left to right
    q.append(root)
    final_ans=[]
    # print(q[0])
    while q != []:

        size=len(q)
        ans=[0]*size
        # if flag==1:
        #     pointer=size-1
        # else:
        #     pointer=0
        for i in range(size):
            r=q.pop(0)
            if flag==0:
                ans[i]=r.val
            else:
                ans[size-1-i]=r.val
            if r.left != None :
                q.append(r.left)
            if r.right!=None:
                q.append(r.right)
        final_ans.append(ans)
        if flag == 0:
            flag=1
        else:
            flag=0
    print(final_ans)

root=TreeNode(3)
root.left=TreeNode(9)
root.right=TreeNode(20)
root.right.left=TreeNode(15)
root.right.right=TreeNode(7)

zigzag_traversal(root)
