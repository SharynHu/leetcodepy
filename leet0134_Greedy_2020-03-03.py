# 假设开始设置起点start = 0, 并从这里出发，如果当前的gas值大于cost值，就可以继续前进，此时到下一个站点，剩余的gas加上当前的gas再减去cost，看是否大于0，若大于0，则继续前进。当到达某一站点时，若这个值小于0了，则说明从起点到这个点中间的任何一个点都不能作为起点，则把起点设为下一个点，继续遍历。当遍历完整个环时，当前保存的起点即为所求。

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas)<sum(cost):
            return -1
        
        tmp = [gas[i]-cost[i] for i in range(len(cost))]
        currGas = 0
        
        start = 0
        for i in range(len(tmp)):
            currGas += tmp[i]
            
            if currGas>=0:
                # we can continue to move on the the next station
                continue
            else:
                # we cannot move on here, which means the index i cannot be a start
                start = i+1
                currGas = 0
        return start
