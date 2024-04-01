# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        visited=set()
        myset=set()
        que=deque()
        que.append(root)
        while que:
            node=que.popleft()
            visited.add(node)
            myset.add(node.val)
            if node.left and node.left not in visited:
                que.append(node.left)
            if node.right and node.right not in visited:
                que.append(node.right)
        return len(myset)==1
                


        