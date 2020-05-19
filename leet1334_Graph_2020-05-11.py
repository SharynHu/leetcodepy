#对有向图使用Dijkstra算法
import heapq
class Solution(object):
    def traverse(self, graph, cost, s, n, threshold):
        dist = {}
        for v in range(n):
            if v==s:
                dist[v] = 0
                continue
            dist[v] = float('inf')
        # push the source node into the queue
        minHeap = [(0, s)]
        heapq.heapify(minHeap)
        
        visited = set()
        count = 0
        while(minHeap):
            #pop the node currently achievable with the minimum distance
            currDist, node = heapq.heappop(minHeap)
            if currDist>threshold:
                break
            if node in visited:
                continue
            visited.add(node)
            count += 1
            for v in graph[node]:
                dist[v] = currDist+cost[node][v]
                heapq.heappush(minHeap, (dist[v], v))
        return count-1
                
            
            
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        # build the bidirected graph and cost matrix
        graph = collections.defaultdict(list)
        cost = collections.defaultdict(dict)
        for u, v, weight in edges:
            graph[u].append(v)
            graph[v].append(u)
            cost[u][v] = cost[v][u] = weight
        
        res = []
        minCnt = float('inf')
        for i in range(n):
            count = self.traverse(graph, cost, i, n, distanceThreshold)
            if not res or count<minCnt:
                res = [i]
                minCnt = count
                continue
            if count==minCnt:
                res.append(i)
                continue
        return max(res)
            
     
