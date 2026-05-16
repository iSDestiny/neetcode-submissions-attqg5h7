#  beginWord = "cat", endWord = "sag", wordList = ["bat","bag","sag","dag","dot"]
# 
# cat - bat - bag - sag
#              |  /
#             dag
# dot
#
# Time: O(n^2*m) where n is the size of wordList and m is the length of a word
# Space: O(n)

from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        def oneCharDiff(a: str, b: str) -> bool:
            if len(a) != len(b):
                return False
            diff = 0
            for x, y in zip(a, b):
                if x != y:
                    diff += 1
                    if diff > 1:
                        return False
            return diff == 1
        
        adjList = defaultdict(set)
        wordList.append(beginWord)
        
        for word1 in wordList:
            for word2 in wordList:
                if word1 != word2 and oneCharDiff(word1, word2):
                    adjList[word1].add(word2)
                    adjList[word2].add(word1)
        
        print(adjList)
        queue = deque([beginWord])

        count = 0
        visited = set(beginWord)
        while queue:
            count += 1
            for _ in range(len(queue)):
                u = queue.popleft()
                for v in adjList[u]:
                    if v in visited:
                        continue
                    if v == endWord:
                        return count + 1
                    visited.add(v)
                    queue.append(v)
        return 0 