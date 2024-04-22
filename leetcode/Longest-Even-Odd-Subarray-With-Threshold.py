class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:

        max_len=float("-inf")
        left=0
        
        status=-1
        for i in range(len(nums)):

            if status==-1:
                if nums[i]%2==0 and nums[i]<=threshold:
                    left=i
                    status=0
                    max_len=max(max_len,i-left+1)

            elif status==0 and nums[i]%2==1 and nums[i]<=threshold:
                max_len=max(max_len,i-left+1)
                status=1
            elif status ==1 and nums[i]%2==0 and nums[i]<=threshold:
                max_len=max(max_len,i-left+1)
                status=0
            else:
                if nums[i]%2==0 and nums[i]<=threshold:
                    status=0
                    left=i
                    max_len=max(max_len,i-left+1)
                else:
                    status=-1
        return max_len if max_len!=float("-inf") else 0




        