class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        if not nums:
            return ranges
        
        start = nums[0]
        end = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] == end + 1:
                end = nums[i]
            else:
                if start == end:
                    ranges.append(f"{start}")
                else:
                    ranges.append(f"{start}->{end}")
                start = nums[i]
                end = nums[i]
        
        if start == end:
            ranges.append(f"{start}")
        else:
            ranges.append(f"{start}->{end}")
        
        return ranges
