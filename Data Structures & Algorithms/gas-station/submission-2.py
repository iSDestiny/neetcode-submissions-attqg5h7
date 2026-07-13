class Solution:
    # gas = [1,2,3,4], cost = [2,2,4,1]
    # constraints:
    #   - at most 1 solution
    #   - 0 <= gas[i], cost[i] < +inf
    #   - len(gas), len(cost) > 0
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        balance = 0 
        pos = 0

        for i in range(len(gas)):
            balance += gas[i] - cost[i]
            if balance < 0:
                pos = i+1
                balance = 0
        
        return pos