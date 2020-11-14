class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # initialize the indegree map and the graph
        inDegree = collections.defaultdict(int)
        graph = collections.defaultdict(list)
        
        for v, u in prerequisites:
            inDegree[v] += 1
            graph[u].append(v)
        
        # build a queue to store all vertex that have zero indegrees
        queue = collections.deque()
        for vertex in range(numCourses):
            if not inDegree[vertex]:
                queue.appendleft(vertex)
        
        # start deleting vertex with zero indegree
        while(queue):
            u = queue.pop()
            # if the indegree of the current vertex is -1, then it has already been visited, we return false
            if inDegree[u]==-1:
                return False
            # mark the indegree of this node as -a
            inDegree[u] = -1
            # deduct 1 from the indegrees of all nodes adjacant to it
            for v in graph[u]:
                inDegree[v] -= 1
                if inDegree[v] == 0:
                    queue.appendleft(v)
        # after deleting, we check if the indegree of all nodes are -1
        for u in range(numCourses):
            if inDegree[u] != -1:
                return False
        return True
