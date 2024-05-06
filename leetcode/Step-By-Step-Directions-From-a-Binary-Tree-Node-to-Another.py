# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        self.pathS=[]
        self.pathE=[]
        def find(node,path):
            if not node:
                return 
            if node.val==startValue:
                self.pathS=path[:]
                
            if node.val==destValue:
                self.pathE=path[:]
            if self.pathS and self.pathE:
                return    
            
            path.append("L")
            find(node.left,path)
            
            path.pop()
            path.append("R")
            find(node.right,path)
            path.pop()
        find(root,[])
        
        
        i,j=0,0
        while i<len(self.pathS) and j<len(self.pathE):
            if self.pathS[i]!=self.pathE[j]:
                break
            i+=1
            j+=1
        return ("U"*(len(self.pathS)-i) + "".join(self.pathE[j:]))
        

        
        
       
        
       

      

