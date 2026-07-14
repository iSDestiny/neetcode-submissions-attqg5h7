class Solution:
    # horizontal even, vertical odd
    # middle is 1D horizontal, multiple entries
    # [1,2,3,4],
    # [5,6,7,8],
    # [9,10,11,12]
    #
    # horizontal odd, vertical even
    # middle is 1D vertical, multiple entries
    # [1,2,3],
    # [5,6,7],
    # [9,10,11]
    # [99,100,110]
    #
    # both odd
    # middle is a single element
    # [1,2,3],
    # [4,5,6],
    # [7,8,9]
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])

        l,r = 0, m
        top, bottom = 0, n
        res = []
        while l < r and top < bottom:
            for i in range(l,r):
                res.append(matrix[top][i])
            top += 1
            for i in range(top,bottom):
                res.append(matrix[i][r-1])
            r -= 1
            if not (l < r and top < bottom):
                break
            for i in range(r-1, l-1, -1):
                res.append(matrix[bottom-1][i])
            bottom -= 1
            for i in range(bottom-1, top-1, -1):
                res.append(matrix[i][l])
            l += 1

        return res 