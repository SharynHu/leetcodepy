#对于每个点i，计算到这个点距离为d的点的个数,记其为n
#对于每个i来说，所存在的boomerang的个数为n(n-1)
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        distance = {}
        for i in range(len(points)):
            if i not in distance:
                distance[i] = collections.defaultdict(int)
            for j in range(len(points)):
                distSqr = (points[i][0]-points[j][0])**2+(points[i][1]-points[j][1])**2
                distance[i][distSqr] += 1
        
        #对于每个i计算tuple(i,j,k)的数量
        count = 0
        for i in distance:
            for d in distance[i]:
                count += (distance[i][d]-1)*distance[i][d]
        return count
