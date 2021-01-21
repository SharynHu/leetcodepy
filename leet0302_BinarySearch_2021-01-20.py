#It is easy to see that we need to find the upperbound, lowerbound, leftbound and rightbound of the black pixels.
#To loop through the matrix to find the bounds, we need O(mn) time.
#Since all the black pixels are connected, it means their vertical indice and horizontal indice are continuous. And since we've know one of the position, we can devide matrix into 4 parts, the left-part, the right part, the upside part, the downside part. And we'll get some kind of sorted arrays(include duplicates) indicating whether this row/column has black pixels.
#The time complexity for this position is nlog(m)+mlog(n)

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
