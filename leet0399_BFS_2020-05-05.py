class Solution(object):
    def bfs(self, query, graph):
        a, b = query
        if a not in graph or b not in graph:
            return -1.0
        #寻找从a到b的路径
        queue = collections.deque([[a,1.0]])
        visited = set()
        while(queue):
            curr, currVal = queue.pop()
            if curr in visited:
                continue
            visited.add(curr)
            if curr == b:
                graph[a][b] = currVal
                graph[b][a] = 1.0/currVal
                return currVal
            for neighbor in graph[curr]:
                if neighbor not in visited:
                    # print a, neighbor
                    queue.appendleft([neighbor, currVal*graph[curr][neighbor]])
        return -1.0
            
        
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = collections.defaultdict(dict)
        
        #build the graph
        for i in range(len(equations)):
            a, b = equations[i]
            val = values[i]
            graph[a][b] = val
            graph[b][a] = 1.0/val
            graph[a][a] = 1.0
            graph[b][b] = 1.0
        # print graph
        res = []
        for query in queries:
            res.append(self.bfs(query, graph))
        return res
