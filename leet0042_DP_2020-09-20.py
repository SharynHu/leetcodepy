# This is a DP solution
# We need to determine the height of the water serface for each index
# for each index the height of the water serface is min(max(height[:i+1]), max(height[i:]))
# we can use dp to get the maximun vaule of height[:i+1] and height[i:]

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height or len(height)<=2:
            return 0
        
        # 1. find the maximum height from both sides
        maxLeftToRight = [height[0]]*len(height)
        maxRightToLeft = [height[-1]]*len(height)
        
        for i in range(1, len(height)):
            maxLeftToRight[i] = max(maxLeftToRight[i-1], height[i])
            maxRightToLeft[len(height)-1-i] = max(maxRightToLeft[len(height)-i], height[len(height)-1-i])
        print maxLeftToRight
        print maxRightToLeft
        
        #2. for each i, calculate the water volumn and accumulate them together
        totalWater = 0
        for i in range(len(height)):
            currDepth =  min(maxLeftToRight[i], maxRightToLeft[i])-height[i]
            totalWater += currDepth
        return totalWater
