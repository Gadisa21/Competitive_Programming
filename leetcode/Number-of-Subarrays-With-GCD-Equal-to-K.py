class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        if len(nums)==1:
            return 0 if nums[0]!=k else 1
        def gcd(a,b):
            if b==0:
                return a
            return gcd(b,a%b)
        l=0
        
        ans=0
        for i in range(len(nums)):
            curr_gcd=0
            for j in range(i,len(nums)):
                curr_gcd=gcd(curr_gcd,nums[j])
                if curr_gcd==k:
                    ans+=1
                elif curr_gcd<k:
                    break
        return ans


        