# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy=ListNode()
        curr=head
        temp=dummy
        while curr.next:
            temp_sum=0
            curr=curr.next
            while curr.val!=0:
                temp_sum+=curr.val
                curr=curr.next
            temp.next=ListNode(temp_sum)
            temp=temp.next
        return dummy.next
        