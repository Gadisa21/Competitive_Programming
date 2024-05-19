"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        self.res=[]

        def dfs(node):
            if not node:
                return 
            
            for n in node.children:
                dfs(n)
                self.res.append(n.val)
            
        dfs(root)
        if  root:

            self.res.append(root.val)

        return self.res

        