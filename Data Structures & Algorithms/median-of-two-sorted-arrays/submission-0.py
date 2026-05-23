class Solution:
    # Time: O(log(min(m,n))) since we only binary search one of the arrays
    # Space: O(1)
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        totalLen = len(nums1) + len(nums2)
        half = totalLen // 2

        # we always want to be processing the smaller array
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        
        l,r = 0,len(nums1)-1
        while True:
            i = (l+r) // 2 # partition point of current array
            j = half - i - 2 # partition point of other array

            aLeft = nums1[i] if i >= 0 else float('-inf')
            aRight = nums1[i+1] if i+1 < len(nums1) else float('inf')
            bLeft = nums2[j] if j >= 0 else float('-inf')
            bRight = nums2[j+1] if j+1 < len(nums2) else float('inf')

            # found the correct partition
            if aLeft <= bRight and bLeft <= aRight:
                if totalLen % 2 == 0: # even
                    return (max(aLeft, bLeft) + min(aRight, bRight)) / 2
                else:
                    return min(aRight, bRight)
            elif aLeft > bRight:
                r = i - 1
            else:
                l = i+1
        
        return 0 