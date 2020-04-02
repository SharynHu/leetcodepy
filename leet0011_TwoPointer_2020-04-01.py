#一个矩形container的高由短边决定
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height)-1
        
        maxHeight = 0
        while(i<j):
            currHeight = min(height[i], height[j])
            currArea = currHeight*(j-i)
            maxHeight = max(maxHeight, currArea)
            if height[i]<=height[j]:
                i += 1
            else:
                j -= 1
        return maxHeight
                
