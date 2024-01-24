class Solution(object):
    def longestSubarray(self, nums):
        if 0 not in nums:
            return len(nums)-1
        count_dic={1:0,0:0}
        l=0
        res=float("-inf")
        for r in range(len(nums)):
            count_dic[nums[r]]+=1
            while count_dic[0]>1:
                count_dic[nums[l]]-=1
                l+=1
            res=max(res,r-l+1 if 0 not in nums[l:r+1] else r-l)
        return res


        