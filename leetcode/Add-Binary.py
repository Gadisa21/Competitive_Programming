class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        result=int(a,2)+int(b,2)

        return bin(result).split("0b")[-1]