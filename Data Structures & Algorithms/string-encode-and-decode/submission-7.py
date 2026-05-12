class Solution:

    # ["Hello", "World"] -> "5;Hello5;World"
    # Time: O(n) length of the array
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"{len(s)};{s}"
        return res
        
    #         
    # "5;Hello5;World"
    # idx = 14
    # freq = "5"
    # res = ["Hello", "World"]
    #
    # result = ["Hello", "World"]
    # Time: O(m) length of the encoded string
    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        idx = 0
        freq = ""
        res = []
        while idx < len(s):
            if s[idx] != ";":
                freq += s[idx]
                idx += 1
            else:
                res.append(s[idx+1:idx + int(freq)+1])
                idx += int(freq)+1
                freq = ""
        return res
            