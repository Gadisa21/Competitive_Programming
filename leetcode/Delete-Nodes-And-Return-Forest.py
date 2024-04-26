# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans=[]
        to_delete=set(to_delete)

        def dfs(node,isRoot):
            if not node:
                return None
            
            if node.val in to_delete:
                dfs(node.left,True)
                dfs(node.right,True)
            else:
                if node.left:
                    if node.left.val in to_delete:
                        dfs(node.left,False)
                        node.left=None
                    else:
                        dfs(node.left,False)
                if node.right:
                    if node.right.val in to_delete:
                        dfs(node.right,False)
                        node.right=None
                    else:
                        dfs(node.right,False)
                if isRoot:
                    ans.append(node)
        dfs(root,True)
        return ans
            
  
                




        