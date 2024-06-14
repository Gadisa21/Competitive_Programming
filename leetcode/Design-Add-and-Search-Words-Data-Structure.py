class TrieNode:

    def __init__(self):
        self.children=[None for _ in range(26)]
        self.is_end=False

class WordDictionary:

    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        curr=self.root

        for ch in word:
            indx=ord(ch)-97

            if not curr.children[indx]:
                curr.children[indx]=TrieNode()
            curr=curr.children[indx]
        curr.is_end=True
        

    def search(self, word: str) -> bool:

        def dfs(node,i):

            for j in range(i,len(word)):
                w=word[j]

                if w==".":
                    for t in range(26):
                        if not node.children[t]:
                            continue
                        if  dfs(node.children[t],j+1):
                            return True
                    return False
                else:
                    indx=ord(w)-97
                    if not node.children[indx]:
                        return False
                    node=node.children[indx]
            return node.is_end
        return dfs(self.root,0)


   


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)