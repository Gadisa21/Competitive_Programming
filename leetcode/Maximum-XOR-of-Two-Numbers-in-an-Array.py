
class TrieNode:
    def __init__(self):
        self.children=[None,None]

class Solution:

    def __init__(self):
        self.root=TrieNode()

    def insert(self,num):
        curr=self.root

        for i in range(31,-1,-1):
            bit=(num>>i)&1
            if not curr.children[bit]:
                curr.children[bit]=TrieNode()
            curr=curr.children[bit]
    def find_max_xor(self,num):
        curr=self.root
        xor_num=0
        for i in range(31,-1,-1):
            bit=(num>>i)&1
            toggled_bit=bit^1

            if curr.children[toggled_bit]:
                xor_num=xor_num<<1 | 1
                curr=curr.children[toggled_bit]
            else:
                xor_num=xor_num<<1 | 0
                curr=curr.children[bit]
        return xor_num

            
    def findMaximumXOR(self, nums: List[int]) -> int:

        for num in nums:
            self.insert(num)
        
        max_val=0

        for num in nums:
            max_val=max(max_val,self.find_max_xor(num))
        return max_val


        