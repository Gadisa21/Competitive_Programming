# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph=defaultdict(list)

        def dfs(node,parent):

            graph[node.val].append(parent.val)
            if node.right:
                graph[node.val].append(node.right.val)
                dfs(node.right,node)
            if node.left:
                graph[node.val].append(node.left.val)
                dfs(node.left,node)
 
        if root.left:
            graph[root.val].append(root.left.val)
            dfs(root.left,root)
        if root.right:
            graph[root.val].append(root.right.val)
            dfs(root.right,root)
        
        que=deque()
        visited=set()
        que.append((target.val,0))
        visited.add(target.val)
        while que:
            node,length=que[-1]
            if length==k:
                ans=[]
                for node,l in que:
                    ans.append(node)
                return ans
            for i in range(len(que)):
                node,length=que.popleft()
                for neighbour in graph[node]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        que.append((neighbour,length+1))
        return []
        

       

        