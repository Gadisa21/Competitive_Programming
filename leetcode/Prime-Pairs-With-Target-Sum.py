class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        prime=[True for _ in range(n+1)]
        prime[0]=prime[1]=False
        temp=n

        ans=[]
        d=2
        while d*d<=n:
            j=d*d
            while j<=n:
                if prime[j]:
                    prime[j]=False
                j+=d
            d+=1
        prime_num=[index  for index,value in enumerate(prime) if value ]
        l,r=0,len(prime_num)-1   
        while l<=r:
            total=prime_num[l]+prime_num[r]
            if total>temp:
                r-=1
            elif total==temp:
                ans.append([prime_num[l],prime_num[r]])
                l+=1
                r-=1
            else:
                l+=1
        return ans
            

        