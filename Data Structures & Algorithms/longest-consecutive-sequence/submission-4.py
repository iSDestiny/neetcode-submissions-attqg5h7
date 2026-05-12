class Solution:
    # nums = [2,20,4,10,3,4,5]
    # seq = {2: 3l 20: 21, 4: 5, 10: 11, 3: 4, 4: 5, 5: 6}
    # collect all the numbers that are the start of sequences (a start of a sequence is any number where num - 1 doesn't exist)
    # follow the sequence using the seq dict for each start
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = {num: num+1 for num in nums}
        start = []
        for num in seq:
            if num-1 not in seq:
                start.append(num)
        
        res = 0
        for num in start:
            current = 1 
            c = num
            while seq[c] in seq:
                current += 1
                c = seq[c]
            res = max(res, current)
        return res