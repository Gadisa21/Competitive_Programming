class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def max_subsequence(nums: List[int], length: int) -> List[int]:
            
            stack = []
            drop = len(nums) - length
            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:length]

        def merge(nums1: List[int], nums2: List[int]) -> List[int]:
            
            merged = []
            while nums1 or nums2:
                if nums1 > nums2:
                    merged.append(nums1.pop(0))
                else:
                    merged.append(nums2.pop(0))
            return merged

        best = []
        for i in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            subseq1 = max_subsequence(nums1, i)
            subseq2 = max_subsequence(nums2, k - i)
            candidate = merge(subseq1, subseq2)
            best = max(best, candidate)
        return best
        
