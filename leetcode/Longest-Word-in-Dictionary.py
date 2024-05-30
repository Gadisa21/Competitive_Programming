class TrieNode:

    def __init__(self):
        self.children=[None]*26
        self.is_end=False




class Solution:

    def __init__(self):
        self.root=TrieNode()
    
    def insert(self,word):

        curr=self.root

        for ch  in word:

            indx=ord(ch)-97
            if not curr.children[indx]:
                curr.children[indx]=TrieNode()
            curr=curr.children[indx]
        curr.is_end=True
    def find(self,word):

        curr=self.root
        for ch in word:
            indx=ord(ch)-97
            curr=curr.children[indx]

            if not curr.is_end:
                return False
            

        return True 




    def longestWord(self, words: List[str]) -> str:

        ans=""

        for word in words:
            self.insert(word)

        for word in words:
            if self.find(word):
                if len(ans)<len(word):
                    ans=word
                elif len(ans)==len(word):
                    ans= word if word<ans else ans
        return ans



        
        
        
        