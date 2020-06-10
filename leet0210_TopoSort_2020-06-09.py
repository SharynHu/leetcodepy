#detect cycles in the graph
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = collections.defaultdict(set)
        indegree = collections.defaultdict(int)
        
        for i, j in prerequisites:
            graph[j].add(i)
            indegree[i] += 1
       
        #queue中存储所有入度为0的节点
        queue = collections.deque([course for course in range(numCourses) if indegree[course]==0])

        res = []
        while(queue):
            size = len(queue)
          
            curr = queue.pop()
            #将当前节点的入度标记为-1
            if indegree[curr]==-1:
                continue
            res.append(curr)
            indegree[curr] = -1
            for j in graph[curr]:
                if indegree[j] != -1:
                    indegree[j] -= 1
                    if indegree[j] == 0:
                        queue.appendleft(j)
        
        #检查是否所有课程的入度均为-1
        for course in range(numCourses):
            if indegree[course]!=-1:
                return []
        return res
        
