#Keypoint: try to distribute the force as distant as possible.
class Solution(object):
    def count(self, position, candidate):
        # count how many balls we can put if we set the minimum distance as candiate
        count = 0
        currDist = 0
        for i in range(1, len(position)):
            currDist += position[i]-position[i-1]
            if currDist>=candidate:
                count += 1
                currDist = 0
        return count+1
    
    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """
        position.sort()
        
        left,right = 1, position[-1]-position[0]
        
        while(left+1<right):
            middle = (left+right)/2
            currCount = self.count(position, middle)
            # the current distance is too big to put m balls, we need to make it smaller     
            if currCount<m:
                right = middle
            # the current distance can put m balls, we try bigger distances
            else:
                left = middle
        
        # check left and right
        # first check the right [position]
        if self.count(position, right) >=m:
            return right
        return left
