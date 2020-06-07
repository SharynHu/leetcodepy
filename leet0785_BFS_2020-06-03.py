#二分图：可以将图分成两个互斥的子集，使得每个边均包含两个子集中的节点
#假设这两个互斥的子集为A, B, 也就是说对于每个属于集合A的节点，它的邻居只能属于另一个集合B；对于每个属于集合B的节点，它的邻居只能属于集合A.
#当一个节点它所属的集合确定时，它的邻居所属的集合也确定，因此应该使用BFS来解决
#每个子图的第一个节点加入哪个集合并不影响最终结果
class Solution(object):
    def bfs(self, graph, root, visited):
        setA = set()
        setB = set()
        queue = collections.deque([[root, "A"]])
        
        while(queue):
            curr, currSet = queue.pop()
            if visited[curr]:
                continue
            visited[curr] = True
            if currSet=="A":
                setA.add(curr)
                for neighbor in graph[curr]:
                    if visited[neighbor] and neighbor in setA:
                        return False
                    if not visited[neighbor]:
                        queue.appendleft([neighbor, "B"])
                        continue
            if currSet=="B":
                setB.add(curr)
                for neighbor in graph[curr]:
                    if visited[neighbor] and neighbor in setB:
                        return False
                    if not visited[neighbor]:
                        queue.appendleft([neighbor, "A"])
                        continue
        return True
            
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        setA = set()
        setB = set()
        visited = [False] * len(graph)
        
        for i in range(len(graph)):
            if not visited[i]:
                if not self.bfs(graph, i, visited):
                    return False
        return True
        
