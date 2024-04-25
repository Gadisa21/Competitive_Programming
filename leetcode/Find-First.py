class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def lower(start,end):
            ans=end
            end-=1
            while start<=end:
                mid=start+(end-start)//2
                if nums[mid]==target:
                    ans=mid
                    end-=1
                elif nums[mid]<target:
                    start=mid+1
                else:
                    end=mid-1
            return ans
                    
        

        def higher(start,end):
            ans=start
            start+=1
            while start<=end:
                mid=start+(end-start)//2
                if nums[mid]==target:
                    ans=mid
                    start=mid+1
                elif nums[mid]<target:
                    start=mid+1
                else:
                    end=mid-1
            return ans

        l,r=0,len(nums)-1
        while l<=r:
            mid=l+(r-l)//2
            if nums[mid]==target:
                return [lower(l,mid),higher(mid,r)]
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        return [-1,-1]
        