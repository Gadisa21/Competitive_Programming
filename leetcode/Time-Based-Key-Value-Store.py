class TimeMap:

    def __init__(self):
        self.hash=defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        if self.hash[key]==[]:
            return ""
        else:
            if self.hash[key][-1][-1]<=timestamp:
                return self.hash[key][-1][0]
            else:
                i=len(self.hash[key])-1
                while i>=0 and self.hash[key][i][-1]>timestamp:
                    i-=1
                if i<0:
                    return ""
                else:
                    return self.hash[key][i][0]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)