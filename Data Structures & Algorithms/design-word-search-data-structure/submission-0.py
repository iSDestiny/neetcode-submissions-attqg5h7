class TrieNode:
    def __init__(self, isEnd: bool = False):
        self.isEnd = isEnd
        self.children = {}

class WordDictionary:

    # Space: O(t)
    def __init__(self):
        self.root = TrieNode()

    # Time: O(n)
    def addWord(self, word: str) -> None:
        current = self.root
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
        current.isEnd = True

    # Time: O(n)
    def search(self, word: str) -> bool:
        def dfs(current: TrieNode, i: int) -> bool:
            if i == len(word):
                return current.isEnd
            c = word[i]
            if c != ".":
                if c not in current.children:
                    return False
                return dfs(current.children[c], i+1)
            for k in current.children:
                if dfs(current.children[k], i+1):
                    return True
            return False
        
        return dfs(self.root, 0)
