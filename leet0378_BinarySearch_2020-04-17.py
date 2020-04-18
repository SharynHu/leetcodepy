#要得到的是第k个最小的数，因此我们比较的对象应该是k
#假设matrix中第k小的数为a_p，如果我们将矩阵排序的话得到的有序数列为[a_1, a_2, a_3, ...., a_p, a_p, a_p, ....], a_p可能多次出现。 在这个问题中， 变量为x， 函数f(x)为matrix中小于等于x的元素个数，那么f(x)就是一个单调递增函数。
#对于第k小的数p, f(p)>=k，并且f(p)是最接近k的(最左边的).
class Solution(object):
    def calVal(self, matrix, middle):
        '''
        计算对于数middle, matrix中有多少个数小于等于它。
        '''
        m, n = len(matrix), len(matrix[0])
        count = 0
        #trick:由于nums[i][j]逐行递增，那么在第i行，当我们得到nums[i][j]<=middle并且nums[i时[j+1]>middle，我们有nums[i+1][j]>=middle并且nums[i+1][j+1]>middle。因此在下一行中我们的j不需要重置，直接从上一行的j开始就行。
        j = n-1
        for i in range(m):
            while(j>=0 and matrix[i][j]>middle):
                j -= 1
            count += j+1
        return count
    
    
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        start = matrix[0][0]
        end = matrix[m-1][n-1]
        
        while(start+1<end):
            middle = (start+end)/2
            #我们需要知道对于middle所对应的数字，matrix中有多少数字不比它大
            count = self.calVal(matrix, middle)
            #如果count<k那么说明第k个小的数是在range [middle, end]中
            if count<k:
                start = middle
            #如果count>=k那么说明第k个小的数在range [start, middle]中
            else:
                end = middle
        if self.calVal(matrix, start)>=k:
            return start
        return end
