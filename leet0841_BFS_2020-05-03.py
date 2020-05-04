#检测一个有向图是不是连通图
#使用BFS来遍历该有向图
#最后检查所有被遍历的节点是否包含全部节点
class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        queue = collections.deque([0])
        visited = set()
        while(queue):
            curr = queue.pop()
            if curr in visited:
                continue
            visited.add(curr)
            for i in rooms[curr]:
                queue.appendleft(i)
        return len(visited)==len(rooms)
