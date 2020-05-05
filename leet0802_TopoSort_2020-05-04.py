#安全的节点不能是某个环的一部分
#使用拓扑排序法，不断删除出度为零的节点，直到只剩下在环路中的节点
class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        #首先记录每个节点的父节点以及每个节点的出度
        outDegree = collections.defaultdict(int)
        parents = collections.defaultdict(set)
        
        for u in range(len(graph)):
            for v in graph[u]:
                parents[v].add(u)
            outDegree[u] += len(graph[u])
        
        res = []
        #initialize the queue
        queue = collections.deque()
        for v in range(len(graph)):
            if outDegree[v] == 0:
                queue.appendleft(v)
        while(queue):
            curr = queue.pop()
            res.append(curr)
            #将当前节点的父亲节点的出度-1
            for u in parents[curr]:
                outDegree[u] -= 1
                if outDegree[u] == 0:
                    queue.appendleft(u)
        return sorted(res)
