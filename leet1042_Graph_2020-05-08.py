# 先构建无向图，对于每个顶点检查其所有相邻顶点的编号，这个顶点用一个没有用过的编号，依次类推。
class Solution(object):
    def gardenNoAdj(self, N, paths):
        """
        :type N: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        graph = collections.defaultdict(list)
        for i, j in paths:
            graph[i].append(j)
            graph[j].append(i)
                
        color = {}
        for i in range(1, N+1):
            available = set([1,2,3,4])
            for j in graph[i]:
                if j in color and color[j] in available:
                    available.remove(color[j])
            color[i] = available.pop()
        res = []
        for i in range(1, N+1):
            res.append(color[i])
        return res
