
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
            if i < 0 or j < 0 or i >= ROW or j >= COL:
                return
            visited.add((i,j))
            dirs = [(-1,0), (1,0), (0,-1), (0,1)]

            

            letter = board[i][j]
            if letter in node.children:
                for di, dj in dirs: # O(3^cl)
                    i2,j2 = i+di,j+dj
                    if (i2,j2) in visited:
                        continue
                    dfs(i2,j2,node.children[letter],word+letter)
            
            visited.remove((i,j))
        for i in range(ROW):
            for j in range(COL):
                dfs(i,j,root, "")
        return list(res)