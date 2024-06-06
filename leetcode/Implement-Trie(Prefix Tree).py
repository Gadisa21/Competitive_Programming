class TrieNode:

    def __init__(self):
        self.children=[None for _ in range(26)]
        self.is_end=False
class Trie:

    def __init__(self):
        self.root=TrieNode()
        

    def insert(self, word: str) -> None:
        curr=self.root

        for ch in word:

            if curr.children[ord(ch)-97]==None:
                curr.children[ord(ch)-97]=TrieNode()
            curr=curr.children[ord(ch)-97]
        curr.is_end=True
    
        

    def search(self, word: str) -> bool:

        curr=self.root
        for ch in word:
            indx=ord(ch)-97

            if not curr.children[indx]:
                return False
            curr=curr.children[indx]
        return curr.is_end
        


    def startsWith(self, prefix: str) -> bool:
        curr=self.root

        for ch in prefix:
            indx=ord(ch)-97

            if not curr.children[indx]:
                return False
            curr=curr.children[indx]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)