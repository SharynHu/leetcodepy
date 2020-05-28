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
        stack = []
       
        count = 0
        #1代表该节点未被访问，2代表节点已被访问 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                stack = []
                if grid[i][j] == "1":
                    stack.append([i, j])
                if not stack:
                    continue
                count += 1
                while(stack):
                    curr_i, curr_j = stack.pop()
                    if grid[curr_i][curr_j] == "2":
                        continue
                    #否则mark当前节点as discovered,接着检查其邻居是否被遍历
                    grid[curr_i][curr_j] = "2"
                    for next_i, next_j in [[curr_i, curr_j+1], [curr_i,curr_j-1], [curr_i-1, curr_j], [curr_i+1, curr_j]]:
                        if 0<=next_i<len(grid) and 0<=next_j<len(grid[0]) and grid[next_i][next_j]=="1":
                            stack.append([next_i, next_j])
                            
        return count
                      
