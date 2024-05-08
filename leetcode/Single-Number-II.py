class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        ans=0

        for i in range(32):
            cnt=0
            for num in nums:
                cnt += (num >> i) & 1  
            if cnt % 3 != 0:  
                ans |= 1 << i  
        return ans if ans < 2**31 else ans - 2**32

        

        