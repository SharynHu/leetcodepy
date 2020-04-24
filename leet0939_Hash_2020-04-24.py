#确定左上角和右下角，那么一个长方形就确定了
class Solution(object):
    def minAreaRect(self, points):  
        """
        :type points: List[List[int]]
        :rtype: int
        """
        x = collections.defaultdict(set)
        
        for (i, j) in points:
            x[i].add(j)
        maxArea = float('inf')
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                x1,y1 = points[i]
                x2,y2 = points[j]
                #先确定两个点不再一条线
                if x1==x2 or y1==y2:
                    continue
                #查看其他两个点(x1, y2)和(x2, y1)存不存在
                if y1 not in x[x2] or y2 not in x[x1]:
                    continue
                #更新最大的面积
                maxArea = min(maxArea, abs(y1-y2)*abs(x1-x2))
        if maxArea == float('inf'):
            return 0
        return maxArea
