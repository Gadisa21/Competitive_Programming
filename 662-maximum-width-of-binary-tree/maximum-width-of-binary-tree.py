# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        que=deque([(root,1)])

        max_w=0

        while que:
            
            l,r=0,0
            for i in range(len(que)):
                node,n=que.popleft()
                start=n-1
                start*=2
                start+=1

                if node.left:
                    que.append((node.left,start))
                    if not l:
                        l=start
                    elif l:
                        r=start
                if node.right:
                    que.append((node.right,start+1)) 
                    if not l:
                        l=start+1
                    elif l:
                        r=start+1
            max_w=max(max_w,r-l+1)  
        return max_w