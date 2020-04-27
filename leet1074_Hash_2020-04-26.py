class Solution(object):
    def numSubmatrixSumTarget(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        preSum = [[0]*(n+1) for i in range(m)]
        
        #对于每一行计算preSum
        for i in range(m):
            for j in range(1, n+1):
                preSum[i][j] = preSum[i][j-1]+matrix[i][j-1]
        # print preSum
        
        #每个矩形由行号i1, i2和列号j1, j2决定
        #固定列号j1和j2，我们可以得到每一行nums[i][j1:j2+1]的和，即一个一维数组
        res = 0
        for j1 in range(n+1):
            for j2 in range(j1+1, n+1):
                array = [preSum[i][j2]-preSum[i][j1] for i in range(m)]
                #下面需要从这个数组里选一个连续子数组使得该子数组的和为target，这又可以通过preSum转换为一个2sum问题
                preSumCol = [0]*(m+1)
                hashMap = collections.defaultdict(int)
                hashMap[0] = 1
                for i in range(1, m+1):
                    preSumCol[i] = preSumCol[i-1]+array[i-1]
                    #需要寻找之前的某一列它的preSum为preSumCol[i]-target
                    res += hashMap[preSumCol[i]-target]
                    #将当前的preSumcol[i]加入hashMap
                    hashMap[preSumCol[i]] += 1
        return res
