#无环图（树）
#对于一个树，任意一个节点都可以作为根节点，要想得到最长的path，那么需要我们开始的根节点为最长路径的端点（叶子结点）。
#那么问题就是怎样找到最长路径的叶子结点。
#只要对于任意一个根节点进行BFS，最后剩下的节点就是所要找的叶子结点。
class Solution(object):
    def treeDiameter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        if not edges:
            return 0
        
        #建图便于查找
        graph = collections.defaultdict(set)
        for i, j in edges:
            graph[i].add(j)
            graph[j].add(i)
        
        #找出所有的叶节点, 作为根节点push到队列中， None表示该节点没有父节点
        queue = {(v, None) for v, neighbors in graph.items() if len(neighbors)==1}
        path = 0
        while(queue):
            #对所有节点同时进行层序遍历,这里使用set来遍历。如果使用list会超时
            queue = {(v, u) for u, pre in queue for v in graph[u] if v!=pre}
            path += 1
        return path-1
