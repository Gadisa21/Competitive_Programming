class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:

        for i,interval in enumerate(intervals):
            interval.append(i)
        
        
        nums=sorted(intervals)
        def s_r(start,end):
            index=-1
            l,r=0,len(nums)-1
            while l<=r:
                mid=l+(r-l)//2
                if nums[mid][0]==start:
                    l=mid+1
                elif nums[mid][0]>=end:
                    index=nums[mid][-1]
                    r=mid-1
                    
                else:
                    l=mid+1
            return index
        ans=[]
        for start,end,i in intervals:
            if start==end:
                ans.append(i)
            else:
                ans.append(s_r(start,end))
        return ans