class Solution(object):
    def isValid(self, path, j):
        '''
        check if we can put the next queen at column j
        '''
        #每两个皇后都不能处于同一行/列/斜线
        #由于当前我们保证了每行只有一个皇后，因此只需要比较同列和在同一斜线上的皇后
        for i in range(len(path)):
            #先比较在不在同一列
            if path[i]==j:
                return False
            #比较在不在同一斜线上
            if abs(path[i]-j) == len(path)-i:
                return False
        return True

    def backtrack(self, path, res, n):
        if len(path)==n:
            #找到一个解，将其转换格式加入到res数列中
            curRes = []
            for j in path:
                curRes.append("."*j+"Q"+"."*(n-j-1))
            res.append(curRes)
            return 
        for j in range(n):
            if self.isValid(path, j):
                path.append(j)
                self.backtrack(path, res, n)
                path.pop()
        
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        #path[i]= j表示第i行的皇后在第j列
        path = []
        res = []
        self.backtrack(path, res, n)
        return res
