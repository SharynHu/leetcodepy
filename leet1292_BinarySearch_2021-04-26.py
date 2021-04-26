class Solution(object):
    def prefixSum(self, mat):
        prefixSum =[[0]*(len(mat[0])+1) for i in range(len(mat)+1)]
        for i in range(1, len(mat)+1):
            for j in range(1, len(mat[0])+1):
                prefixSum[i][j] = prefixSum[i][j-1]+prefixSum[i-1][j]-prefixSum[i-1][j-1]+mat[i-1][j-1]
                
        return prefixSum
    
    
    def getRec(self, prefixSum, x1, y1, x2, y2):
        return prefixSum[x2][y2]+prefixSum[x1-1][y1-1]-prefixSum[x2][y1-1]-prefixSum[x1-1][y2]
    
    
    def check(self, prefixSum, mat, c, threshold):
        '''
        check if there is a square with side length c exits in mat satisfying sum of it less than or equal to threshold.
        '''
        m, n = len(mat), len(mat[0])
        for i in range(1, m-c+2):
            for j in range(1, n-c+2):
                currSum = self.getRec(prefixSum, i, j, i+c-1, j+c-1)
                if currSum<=threshold:
                    return True
        return False
        
    def maxSideLength(self, mat, threshold):
        """
        :type mat: List[List[int]]
        :type threshold: int
        :rtype: int
        """
        maxSize = 0
        
        if not mat or not mat[0]:
            return 0
        
        prefixSum = self.prefixSum(mat)
        m,n = len(mat), len(mat[0])
        left = 1
        right = min(m,n)
        
        while(left+1<right):
            middle = (left+right)/2
            if self.check(prefixSum, mat, middle, threshold):
                left = middle
            else:
                right = middle
        # check right
        if self.check(prefixSum, mat,right, threshold):
            return right
        if self.check(prefixSum, mat, left, threshold):
            return left
        return 0
