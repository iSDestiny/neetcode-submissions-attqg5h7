class Solution:
    # Since each num in nums is in the range [1,n], this means
    # that we can use each num as an index since it's in range.
    # Using this information we can form a singly linked list where the
    # next pointer for each number is nums[i].
    #
    # If a duplicate exists this will cause a cycle in the linked list formed
    # from following the number as the index. The start of the cycle will be the number
    # that appears more than once (start of the cycle).
    #
    # We can utilize the floyd detection algorithm of slow and fast pointers to get this number.
    # We would have a slow pointer moving one at a time and a fast pointer
    # moving two at a time, we'll keep iterating until these pointers meet.
    # Once it meets to get the start of the cycle, set the slow pointer back to the start
    # of the list and iterate both one at a time until they meet again (this will be the start of the cycle)
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]

        # cycle found
        while fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
    
        # get the start of the cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow