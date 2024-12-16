class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:

        if p==0:
            return 0
        nums.sort()
        def isValid(Treshold):

            i,cnt=0,0
            while i<len(nums)-1:
                if (nums[i+1]-nums[i])<=Treshold:
                    cnt+=1
                    i+=2
                else:
                    i+=1
                if cnt==p:
                    return True
            return False
        l,r=0,10**9
        res=0
        while l<=r:
            m=l+(r-l)//2

            if isValid(m):
                res=m
                r=m-1
            else:
                l=m+1
        return res




        