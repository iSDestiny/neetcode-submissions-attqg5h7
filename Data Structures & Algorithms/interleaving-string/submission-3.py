class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        cache = {}
        def recurse(i1: int, i2: int) -> bool: 
            i3 = i1+i2
            key = (i1,i2)
            if i3 == len(s3):
                return i1 == len(s1) and i2 == len(s2)
            if key in cache:
                return cache[key]
            
            if i1 < len(s1) and s1[i1] == s3[i3]:
                if recurse(i1+1, i2):
                    cache[key] = True
                    return cache[key]
            
            if i2 < len(s2) and s2[i2] == s3[i3]:
                if recurse(i1, i2+1):
                    cache[key] = True
                    return cache[key]
            
            cache[key] = False
            return cache[key]
        return recurse(0,0)
