class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        #up的值置于上面一行有关
        up = [0]*len(grid[0])
        #left的值置于左边一个有关
        left = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                curr = float('inf')
                # print i, j, left, up
                if j-1>=0:
                    curr = min(curr, left+grid[i][j])
                if i-1>=0:
                    curr = min(curr, up[j]+grid[i][j])
                if curr==float('inf'):
                    curr = grid[i][j]
                grid[i][j] = curr
                # update left
                left = curr
                up[j] = curr
            left = 0
        return curr
