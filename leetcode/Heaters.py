class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:

        def mindistance(house,heaters):
            distance=float("inf")
            l,r=0,len(heaters)-1

            while l<=r:
                mid=l+(r-l)//2

                distance=min(distance,abs(heaters[mid]-house))
                if heaters[mid]<house:
                    l=mid+1
                else:
                    r=mid-1
            return distance
        radius=0
        heaters.sort()
        for house in houses:
            radius=max(radius,mindistance(house,heaters))
        return radius
        