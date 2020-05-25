#按从低到高的顺序来砍树，砍过的地方变成草地， 树和草地可以walk through,要求砍掉所有树所经过的最短距离。
#由于没有树有重复的高度，因此砍树的顺序是唯一的。也就是说在遍历图的时候，所经过的点的顺序是唯一的， 那么最短的路径就是每两棵相邻的树之间最短路径的和。
class Solution(object):
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        treesToCut = [ ]
        for i in range(len(forest)):
            for j in range(len(forest[0])):
                if forest[i][j]>1:
                    treesToCut.append([i,j,forest[i][j]])
        treesToCut.sort(key=lambda x:x[2])
        
        totalDist = 0
        queue = collections.deque([[0,0,0]])
        while(treesToCut):
            # use BFS to find the minimum distance from the current position to the 
            visited = set()
            next_i, next_j, next_height = treesToCut.pop(0)
            while(queue):
                curr_i, curr_j, curr_dist = queue.pop()
                if (curr_i, curr_j) in visited:
                    continue
                forest[curr_i][curr_j] = 1
                visited.add((curr_i, curr_j))
                if next_i==curr_i and next_j==curr_j:
                    #we get to the tree from curr_i and curr_j
                    totalDist += curr_dist
                    #寻找下一棵需要被砍的树
                    queue = collections.deque([[curr_i, curr_j, 0]])
                    break
                #访问该树的邻居
                for neighbor_i, neighbor_j in [(curr_i-1, curr_j), (curr_i, curr_j-1), (curr_i, curr_j+1), (curr_i+1, curr_j)]:
                    if 0<=neighbor_i<len(forest) and 0<=neighbor_j<len(forest[0]) and (neighbor_i, neighbor_j) not in visited and forest[neighbor_i][neighbor_j]>=1:
                        queue.appendleft([neighbor_i, neighbor_j, curr_dist+1])
            #如果一直到queue空了也没将要砍的树砍断，那么说明无法reach，返回-1
            if (next_i, next_j) not in visited:
                return -1
        return totalDist
                    
