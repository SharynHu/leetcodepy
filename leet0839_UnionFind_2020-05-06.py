# 只要按位置对比字符，若不相等则 diff 自增1，若 diff 大于2了直接返回 false，因为只有 diff 正好等于2或者0的时候才相似。题目中说了字符串之间都是异构词，说明字符的种类个数都一样，只是顺序不同，就不可能出现奇数的 diff，而两个字符串完全相等时也是满足要求的，是相似的
class UnionFind(object):
    def __init__(self, A):
        self.parent = {i:i for i in A}
        self.rank = {i:1 for i in A}

    def getRoot(self, x):
        path = []
        while(self.parent[x] != x):
            # path compression
            path.append(x)
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        for i in path:
            self.parent[i] = x
        return x

    def union(self, x, y):
        rootX = self.getRoot(x)
        rootY = self.getRoot(y)
        if rootX == rootY:
            return
        if self.rank[rootX] > self.rank[rootY]:
            rootX, rootY = rootY, rootX
        self.parent[rootX] = rootY
        self.rank[rootY] += 1
           
    def find(self, x, y):
        return self.getRoot(x)==self.getRoot(y)


class Solution(object):
    def similar(self, word1, word2):
        diff = 0
        for i in range(len(word1)):
            if word1[i]!=word2[i]:
                diff += 1
        return diff==0 or diff==2
    
    def numSimilarGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        #few words
        uf = UnionFind(A)
        if len(A)<len(A[0])*len(A[0]):
            for i in range(len(A)):
                for j in range(i+1, len(A)):
                    if self.similar(A[i], A[j]):
                        uf.union(A[i], A[j])
        #lot of words
        else:
            A = set(A)
            for word in A:
                for i in range(len(word)):
                    for j in range(i+1, len(word)):
                        newWord = word[:i]+word[j]+word[i+1:j]+word[i]+word[j+1:]
                        if newWord in A:
                            uf.union(word, newWord)
        roots = set()
        for word in A:
            roots.add(uf.getRoot(word))
        return len(roots)

