# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        total_length = 0
        current = head
        while current:
            total_length += 1
            current = current.next

        part_size = total_length // k
        extra_nodes = total_length % k
        
        result = []
        current = head
        for i in range(k):
            part_head = current
            current_part_size = part_size + (1 if i < extra_nodes else 0)
            
            for j in range(current_part_size - 1):
                if current:
                    current = current.next
            
            if current:
                next_part = current.next
                current.next = None
                current = next_part
            
            result.append(part_head)
        
        return result