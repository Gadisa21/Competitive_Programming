class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        l,r=0,position[-1]-position[0]

        def can_place(max_dis):
            cur=position[0]
            ball=1

            for p in range(1,len(position)):

                if position[p] -cur >=max_dis:
                    cur=position[p]
                    ball+=1
                if ball==m:
                    return True
            return False

        ans=1
        while l<=r:
            mid=(r+l)//2

            if can_place(mid):
                l=mid+1
                ans=max(ans,mid)
            else:
                r=mid-1
        return ans
