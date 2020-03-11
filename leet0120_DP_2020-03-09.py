class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle or not triangle[0]:
            return 0
        
        pathSum = triangle[0]
        for i in range(1, len(triangle)):
            tmpSum = pathSum+[]
            for j in range(len(triangle[i])):
                if j==0:
                    tmpSum[j] = triangle[i][j]+pathSum[j]
                    continue
                if j<len(triangle[i])-1:
                    tmpSum[j] = min(pathSum[j]+triangle[i][j], pathSum[j-1]+triangle[i][j])
                    continue
                tmpSum.append(triangle[i][j]+pathSum[j-1])
            pathSum = tmpSum
        return min(pathSum)
