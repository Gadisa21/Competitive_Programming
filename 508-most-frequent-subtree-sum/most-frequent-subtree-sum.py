# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        sum_frequency = defaultdict(int)
        
        def calculate_subtree_sum(node):
            if not node:
                return 0
            left_sum = calculate_subtree_sum(node.left)
            right_sum = calculate_subtree_sum(node.right)
            
            current_sum = node.val + left_sum + right_sum
            
            sum_frequency[current_sum] += 1
            
            return current_sum
        
        calculate_subtree_sum(root)
        
        max_frequency = max(sum_frequency.values())
        
        result = [s for s, freq in sum_frequency.items() if freq == max_frequency]
        
        return result