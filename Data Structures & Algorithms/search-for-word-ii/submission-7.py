
'''
board = [
  ["a","b","c","d"],
  ["s","a","a","t"],
  ["a","c","k","e"],
  ["a","c","d","n"]
],
words = ["bat","cat","back","backend","stack"]


Trie:

        ->  {b     c      s}
           /       |      |
      -> a         a      t
       /           |      |
  {t*  c}            t*     a
      |                   |
      k*                  c
      |                   |
      e                   k*
      |
      n
      |
      d*

'''

# Time: O(n * m * 3^t + s)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

    def __repr__(self):
        return f"{self.children},{self.isEnd}"

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # create Trie
        root = TrieNode() 

        for word in words:
            current = root
            for c in word:
                if c not in current.children:
                    current.children[c] = TrieNode()
                current = current.children[c]
            current.isEnd = True
        
        ROW = len(board)
        COL = len(board[0])
        res = set()
        visited = set()
        def dfs(i: int, j: int, node: TrieNode, word: str) -> None:
            if node.isEnd:
                res.add(word)
            if i < 0 or j < 0 or i >= ROW or j >= COL or board[i][j] not in node.children or (i,j) in visited:
                return
            dirs = [(-1,0), (1,0), (0,-1), (0,1)]
            visited.add((i,j))
            for di, dj in dirs: # O(3^cl)
                i2,j2 = i+di,j+dj
                dfs(i2,j2,node.children[board[i][j]],word+board[i][j])
            
            visited.remove((i,j))
        for i in range(ROW):
            for j in range(COL):
                dfs(i,j,root, "")
        return list(res)