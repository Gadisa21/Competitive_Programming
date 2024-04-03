class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def rec(left,right):
            if left==right:
                return [nums[left]]
            mid=left+(right-left)//2
            nums_left=rec(left,mid)
            nums_right=rec(mid+1,right)
            nums_left.append(float("inf"))
            nums_right.append(float("inf"))
            i=0
            j=0
            ans=[]
            while i<len(nums_left) and j<len(nums_right):
                if nums_left[i]<nums_right[j]:
                    ans.append(nums_left[i])
                    i+=1
                else:
                    if nums_right[j]==float("inf"):
                        break
                    else:
                        ans.append(nums_right[j])
                        j+=1
            return ans
        return rec(0,len(nums)-1)

        