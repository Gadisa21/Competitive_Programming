# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        

        def dfs(node,s):
            if not node:
                return s
            if not node.left and not node.right:
                s.append(node.val)
                return s
            
            
            s=dfs(node.left,s)

            s=dfs(node.right,s)

            return s
            
        
        return dfs(root1,[])==dfs(root2,[])
            
            


        