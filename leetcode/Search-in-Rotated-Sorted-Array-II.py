class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        l,r=0,len(nums)-1

        while l<=r:
            mid = l + (r-l)//2
            
            if nums[mid]==target or nums[l]==target or target==nums[r]:

                return True
            if nums[l]<nums[mid]:
                if nums[mid]<target or target<nums[l]:
                    l=mid+1
                else:
                    r=mid-1
            else:
                if nums[l]==nums[mid]==nums[r] :
                    r-=1
                    l+=1
                elif nums[l]==nums[mid]:
                    l=mid+1
                elif nums[r]==nums[mid]:
                    r=mid-1
                else:
                    r-=1
                    l+=1
                
        return False

                


        
        