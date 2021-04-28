class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points)==1:
            return 1
        hashmap = collections.defaultdict(set)
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                x1,y1 = points[i]
                x2,y2 = points[j]
                if x1==x2:
                    k = float('inf')
                    b = x1
                elif y1==y2:
                    k = 0
                    b = y1
                else:
                    k = float(y2-y1)/(x2-x1)
                    b = float(x1*y2-x2*y1)/(x2-x1)
                hashmap[(k,b)].add((x1,y1))
                hashmap[(k,b)].add((x2,y2))
        maxLen = 0
        for key in hashmap:
            maxLen = max(maxLen, len(hashmap[key]))
        return maxLen
