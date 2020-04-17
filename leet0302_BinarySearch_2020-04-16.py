#需要得到最大/小的横坐标以及最大/小的纵坐标

# 立足所给的点(x,y)，划分整个区域为上半部分、下半部分、左半部分、右半部分。

# 对于上半部分， 由于所有的1都是连续的，所以有1的行的行号是连续的(sorted array with duplicates)，我们需要找到最上边的一个
# 对于其他部分也是一样
class Solution(object):
    def searchX(self, image, x, y, up):
        #find the minimum row index
        start, end = (0, x) if up else (x, len(image)-1)
        while(start+1<end):
            middle = (start+end)/2
            currVal = sum(map(int, image[middle]))
            if currVal>=1:
                if up:
                    end = middle
                else:
                    start = middle
            if currVal == 0:
                if up:
                    start = middle
                else:
                    end = middle
        if up: 
            if sum(map(int, image[start]))>=1:
                return start
            return end
        if sum(map(int, image[end]))>=1:
            return end
        return start
    
    def searchY(self, image, x, y, left):
        #find the minimum row index
        start, end = (0, y) if left else (y, len(image[0])-1)
        while(start+1<end):
            middle = (start+end)/2
            currVal = 0
            for i in range(len(image)):
                currVal += 1 if image[i][middle]=='1' else 0
            if currVal>=1:
                if left:
                    end = middle
                else:
                    start = middle
            if currVal == 0:
                if left:
                    start = middle
                else:
                    end = middle
        if left: 
            currVal = 0
            for i in range(len(image)):
                currVal += 1 if image[i][start]=='1' else 0
            if currVal>=1:
                return start
            return end
        currVal = 0
        for i in range(len(image)):
            currVal += 1 if image[i][end]=='1' else 0
        if currVal>=1:
            return end
        return start
                
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        if not image or not image[0]:
            return 0
        up = self.searchX(image, x, y, True)
        down =  self.searchX(image, x, y, False)
        left =  self.searchY(image, x, y, True)
        right =  self.searchY(image, x, y, False)
        return (down-up+1)*(right-left+1)
