class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:

        def get_mapped_val(num):
            mapped_val="".join(str(mapping[int(digit)]) for digit in str(num))
            return int(mapped_val)
        ans=sorted(nums,key=get_mapped_val)
        return ans
        