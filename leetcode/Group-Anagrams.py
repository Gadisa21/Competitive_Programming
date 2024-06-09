class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dic=defaultdict(list)
        

        for word in strs:
            temp=list(word)
            temp.sort()
            dic[tuple(temp)].append(word)
        ans=[]

        for val in dic.values():
            ans.append(val)
        return ans
        