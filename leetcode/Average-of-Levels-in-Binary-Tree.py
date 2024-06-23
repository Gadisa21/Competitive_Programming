# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        ans=[]
        que=deque()
        que.append(root)
        while que:
            n=len(que)
            total=0
            for i in range(n):
                node=que.popleft()
                total+=node.val
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            ans.append(total/n)
        return ans
                

        
        