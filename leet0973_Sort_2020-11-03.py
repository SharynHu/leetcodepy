class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        if not K or not points:
            return []
        if len(points)<=K:
            return points
        
        distances = []
        for x, y in points:
            distances.append([x**2+y**2, x, y])
        distances.sort()
        return [[x, y] for (d, x, y) in distances[:K]]
