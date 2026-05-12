class TrieNode:
    def __init__(self, char: str, isEndChar: bool):
        self.char = char
        self.children = {}
        self.isEndChar = isEndChar
#     

class PrefixTree:
    def __init__(self):
        self.root = TrieNode("", False)

    # Time: O(n) where n is the size of the word
    def insert(self, word: str) -> None:
        if not word:
            return
        currentNode = self.root
        for i in range(len(word)):
            c = word[i]
            if c not in currentNode.children:
                currentNode.children[c] = TrieNode(c, i == len(word) - 1)
            currentNode = currentNode.children[c]
        currentNode.isEndChar = True

    def search(self, word: str) -> bool:
        currentNode = self.root
        for i in range(len(word)):
            c = word[i]
            if c not in currentNode.children:
                return False
            currentNode = currentNode.children[c]
        return currentNode.isEndChar

    def startsWith(self, prefix: str) -> bool:
        currentNode = self.root
        for i in range(len(prefix)):
            c = prefix[i]
            if c not in currentNode.children:
                return False
            currentNode = currentNode.children[c]
        return True