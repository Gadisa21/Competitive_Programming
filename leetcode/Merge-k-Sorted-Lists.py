# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        

        minHeap=[]

        for linked in lists:
            curr=linked
            while curr:
                minHeap.append(curr.val)
                curr=curr.next
        heapq.heapify(minHeap)
        if len(minHeap)==0:
            return 
            
        root=ListNode(heapq.heappop(minHeap))
        curr=root

        while minHeap:
            curr.next=ListNode(heapq.heappop(minHeap))
            curr=curr.next
        return root
        


        
        



        