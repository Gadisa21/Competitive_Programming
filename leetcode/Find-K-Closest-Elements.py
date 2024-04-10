class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        l,r=0,len(arr)-1
        ans=[]

        while l<=r:
            mid =l+(r-l)//2
            if arr[mid]==x:
                if mid==0:
                    return arr[:k]
                elif mid==len(arr)-1:
                    return arr[-k:]
                else:
                    left=mid
                    right=mid+1
                    arr.extend([float("-inf"),float("inf")])
                    while len(ans)!=k:
                        if abs(arr[left]-x)<=abs(arr[right]-x):
                            ans.append(arr[left])
                            left-=1
                        else:
                            ans.append(arr[right])
                            right+=1
                    return sorted(ans)
            elif arr[mid]<x:
                l=mid+1
            else:
                r=mid-1
        if l==0:
            return arr[:k]
        elif r==len(arr)-1:
            return arr[-k:]
        else:
            left=r
            right=l
            arr.extend([float("-inf"),float("inf")])
            while len(ans)!=k:
                if abs(arr[left]-x)<=abs(arr[right]-x):
                    ans.append(arr[left])
                    left-=1
                else:
                    ans.append(arr[right])
                    right+=1
            return sorted(ans)
        






        
    
         
        