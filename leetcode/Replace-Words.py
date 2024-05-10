class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = TrieNode()
        for word in dictionary:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end_of_word = True

        def find_root(word):
            node = root
            prefix = ""
            for char in word:
                if char not in node.children:
                    return word
                node = node.children[char]
                prefix += char
                if node.is_end_of_word:
                    return prefix
            return word

        words = sentence.split()
        replaced_words = [find_root(word) for word in words]
        return " ".join(replaced_words)
