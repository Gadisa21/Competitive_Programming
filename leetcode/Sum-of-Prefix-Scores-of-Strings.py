class TrieNode:
    def __init__(self):
        self.children= defaultdict(TrieNode)
        self.path=0

class Solution:

    def __init__(self):
        self.root=TrieNode()
    
    def insert(self,w):
        cur=self.root
        for ch in w:
            indx=ord(ch)-97
            cur=cur.children[indx]
            cur.path+=1

    def sumPrefixScores(self, words: List[str]) -> List[int]:

        for ch in words:
            self.insert(ch)
        ans=[0]*len(words)
        for i ,ch in enumerate(words):
            score=0
            cur=self.root
            for c in ch:
                indx=ord(c)-97
                cur=cur.children[indx]
                score+=cur.path
            ans[i]=score
        return ans
        