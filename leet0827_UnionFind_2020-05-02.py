class UnionFind(object):
    def __init__(self,grid):
        self.parent = [-1]*(len(grid)*len(grid[0]))
        self.size = [0]*(len(grid)*len(grid[0]))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.parent[i*len(grid)+j] = i*len(grid)+j
                    self.size[i*len(grid)+j] = 1
                    
    def getRoot(self, x):
        while(self.parent[x]!=x):
            self.parent[x] = self.parent[self.parent[x]]
            x= self.parent[x]
        return x
    
    def find(self, x, y):
        return self.getRoot(x)==self.getRoot(y)
    
    def connect(self, x, y):
        rootX = self.getRoot(x)
        rootY = self.getRoot(y)
        if rootX == rootY:
            return
        if self.size[rootX]>=self.size[rootY]:
            self.parent[rootY] = rootX
            self.size[rootX] += self.size[rootY]
            return
        self.parent[rootX] = rootY
        self.size[rootY] += self.size[rootX]
        
        
class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        #build the union find object
        uf = UnionFind(grid)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                for (m,n) in [[i-1, j], [i, j-1],[i+1, j], [i, j+1]]:
                    if grid[i][j] == 1 and 0<=m<len(grid) and 0<=n<len(grid[0]) and grid[m][n] == 1:
                        # this means (i,j) and (m, n) are connected
                        uf.connect(i*len(grid)+j, m*len(grid)+n)
        maxSize = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] != 0:
                    maxSize = max(maxSize, uf.size[uf.getRoot(i*len(grid)+j)])
                    continue
                roots = set()
                for (m,n) in [[i-1, j], [i, j-1],[i+1, j], [i, j+1]]:
                    if 0<=m<len(grid) and 0<=n<len(grid[0]) and grid[m][n]==1:
                        roots.add(uf.getRoot(m*len(grid)+n))
                size = 0
                for root in roots:
                    size += uf.size[root]
                # print size
                maxSize =max(maxSize, size+1)
        return maxSize
        
