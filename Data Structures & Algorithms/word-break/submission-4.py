class Solution:
    # iterate through s recursively:
    #. - for each word in wordDict check if a word can be formed from current index i, if so recurse on these two choices:
    #.    - choose to use this word and recurse on the subproblem where i is the position of the rest of the string
    #.    - skip this word, and choose another word to check for the current index
    #. - return True if any of the recursive paths above reaches the end
    # Time: O(t*m*n)
    # 
    # neetcode -> code -> "" -> True
    # applepenapple -> penapple -> apple -> "" -> True
    # catsincars -> incars -> [cars] -> [s] -> False
    #            -> sincars -> [cars] -> [s] -> False
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = [None] * len(s)
        def recurse(i: int) -> bool:
            if i == len(s):
                return True
            if cache[i] != None:
                return cache[i]
            found = False
            for w in wordDict:
                if s[i:i+len(w)] == w:
                    found = found or recurse(i+len(w))
            cache[i] = found
            return cache[i]
        return recurse(0)