class UnionFind(object):
    def __init__(self, n):
        self.parent = range(n)
        self.size = [1]*n
    
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
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        uf = UnionFind(len(M))
        for i in range(len(M)):
            for j in range(i+1, len(M)):
                if M[i][j] == 1:
                    uf.connect(i, j)
        roots = set()
        for i in range(len(M)):
            roots.add(uf.getRoot(i))
        return len(roots)
