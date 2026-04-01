class Solution:

    # Hello World -> 5#Hello10#World
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += str(len(word)) + "#" + word
        return encoded


    def decode(self, s: str) -> List[str]:
        words = []
        i = 0
        print(s)
        while i < len(s):
            print(words)
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j]) 
            i = j+1
            j = i+length
            word = s[i:j]
            words.append(word)
            i = j

        return words