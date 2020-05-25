class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        #mark all visted nodes as '2'
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                queue = collections.deque()
                if grid[i][j] == "1":
                    queue.appendleft([i,j])
                if not queue:
                    continue
                count += 1
                while(queue):
                    curr_i, curr_j = queue.pop()
                    if grid[curr_i][curr_j]=="2":
                        continue
                    grid[curr_i][curr_j]="2"
                    for next_i, next_j in [[curr_i, curr_j+1], [curr_i, curr_j-1], [curr_i-1, curr_j], [curr_i+1, curr_j]]:
                        if 0<=next_i<len(grid) and 0<=next_j<len(grid[0]) and grid[next_i][next_j]=="1":
                            queue.appendleft([next_i, next_j])
        return count
                    
