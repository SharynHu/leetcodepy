ass Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        
        leftBound, rightBound, upBound, downBound = 0, len(matrix[0])-1, 0, len(matrix)-1
        # the directions are:
        # 1. rightwards
        # 2. downwards
        # 3. leftwards
        # 4. upwards
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0] ]
        currDir = 0
        res = []
        i, j = 0, 0
        while(len(res)<len(matrix)*len(matrix[0])):
            res.append(matrix[i][j])
            # determine the next position, first we need to determine if we need to change the direction
            if currDir==0 and j==rightBound:
                currDir +=1
                upBound += 1
            elif currDir==1 and i==downBound:
                currDir += 1
                rightBound -= 1
            elif currDir==2 and j==leftBound:
                currDir += 1
                downBound -=1
            elif currDir==3 and i==upBound:
                currDir += 1
                leftBound += 1
            currDir %= 4
            i, j = dirs[currDir][0]+i, dirs[currDir][1]+j
        return res
