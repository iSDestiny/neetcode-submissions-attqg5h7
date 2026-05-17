from collections import defaultdict, deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        if not words:
            return ""
        if len(words) == 1:
            return words[0]

        # build adj list
        adjList = defaultdict(list)
        indegrees = defaultdict(int)

        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]

            # initialize all possible characters in indegrees
            for ci in range(len(word2)):
                indegrees[word2[ci]]
            for ci in range(len(word1)):
                indegrees[word1[ci]]
            
            if len(word1) > len(word2) and word1.startswith(word2):
                return ""


            if word1 != word2:
                for ci in range(len(word2)):
                    if ci >= len(word1):
                        break
    
                    if word1[ci] != word2[ci]:
                        adjList[word1[ci]].append(word2[ci])
                        indegrees[word2[ci]] += 1
                        break
            
        
        # topological sort
        queue = deque([c for c in indegrees if indegrees[c] == 0])
        
        ordering = ""
        while queue:
            u = queue.popleft()
            ordering += u
            for v in adjList[u]:
                indegrees[v] -= 1
                if indegrees[v] == 0:
                    queue.append(v)
        
        if len(ordering) != len(indegrees):
            return ""
        return ordering