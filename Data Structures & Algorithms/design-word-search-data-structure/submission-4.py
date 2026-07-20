class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
    

class WordDictionary:

    def __init__(self):
        self.trie = TrieNode()

    def addWord(self, word: str) -> None:
        head = self.trie
        for i in range(len(word)):
            if word[i] not in head.children:
                head.children[word[i]] = TrieNode()
            head = head.children[word[i]]
        head.end = True

    def search(self, word: str) -> bool:
        def dfs(j: int, root: TrieNode):
            current = root
            for i in range(j, len(word)):
                if word[i] != ".":
                    if word[i] not in current.children:
                        return False
                    current = current.children[word[i]]
                else:
                    for node in current.children.values():
                        if dfs(i+1, node):
                            return True
                    return False
            return current.end
        return dfs(0, self.trie)
        
