#key points: 如何判断两个island相等，既然不考虑reflection和rotation，那么肯定是通过平移。也就是说如果我们固定island的最左上的点，那么他们的相对位置是相等的
#solution: 记录下同一个island中所有点相对于第一个点的遍历顺序
class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        islandSet = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 1:
                    continue
                island = []
                queue = collections.deque([[i, j]])
                while(queue):
                    size = len(queue)
                    for k in range(size):
                        curr_i, curr_j = queue.pop()
                        if grid[curr_i][curr_j] == "v":
                            continue
                        grid[curr_i][curr_j] = "v"
                        for next_i, next_j in [[curr_i-1, curr_j], [curr_i+1, curr_j], [curr_i, curr_j-1], [curr_i, curr_j+1]]:
                            if 0<=next_i<len(grid) and 0<=next_j<len(grid[0]) and grid[next_i][next_j]==1:
                                queue.appendleft([next_i, next_j])
                        island.append(curr_i-i)
                        island.append(curr_j-j)
                islandSet.add(tuple(island))
        return len(islandSet)
                         
