# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if not node:
                return 0
            
            
            resLeft=dfs(node.left)
            
            if resLeft==-1:
                return -1
            resRight=dfs(node.right)

            if resRight==-1:
                return -1
            
            if abs(resLeft-resRight)>1:
                return -1
            return max(resLeft,resRight) + 1
        if not root:
            return True
        return dfs(root)!=-1
            
            
    
            
        