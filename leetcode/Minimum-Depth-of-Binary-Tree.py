# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        def min_depth(node):
            if not node:
                return 0
            
            left=min_depth(node.left)
            right=min_depth(node.right)
            if left!=0 and right!=0:
                return min(left,right) +1
            elif left==0:
                return right +1
            else:
                return left +1


            
        if not root:
            return 0
        return min_depth(root)
        