#"M": unrevealed mine
#    --->"X": revealed mine
#"E": unrevealed empty space
#    ---> "B": no adjacent mines
#    ---> digit: adjacent mines
class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        queue = collections.deque([click])
      
        while(queue):
            curr_i, curr_j = queue.pop()
            #如果当前节点已经被访问过
            if board[curr_i][curr_j]=="B" or board[curr_i][curr_j].isdigit():
                continue
            # 如果当前节点是"M", 那么将其改为"X"，并且结束访问
            if board[curr_i][curr_j] == "M":
                board[curr_i][curr_j] = "X"
                return board
            #如果当前节点是"E"， 需要记录其邻居中含有多少"M"，并且访问其邻居
            countM = 0
            for next_i, next_j in [[curr_i-1,curr_j-1],[curr_i-1,curr_j], [curr_i-1, curr_j+1], [curr_i, curr_j-1], [curr_i, curr_j+1], [curr_i+1, curr_j-1], [curr_i+1, curr_j], [curr_i+1, curr_j+1]]:
                if 0<=next_i<len(board) and 0<=next_j<len(board[0]):
                    if board[next_i][next_j]=="M":
                        countM += 1
            #如果该节点周围没有炸弹，那么我们访问其邻居
            if countM==0:
                board[curr_i][curr_j] = "B"
                for next_i, next_j in [[curr_i-1,curr_j-1],[curr_i-1,curr_j], [curr_i-1, curr_j+1], [curr_i, curr_j-1], [curr_i, curr_j+1], [curr_i+1, curr_j-1], [curr_i+1, curr_j], [curr_i+1, curr_j+1]]:
                    if 0<=next_i<len(board) and 0<=next_j<len(board[0]) and board[next_i][next_j] == "E":
                        queue.appendleft([next_i, next_j])
            else:
                board[curr_i][curr_j] = str(countM)
        return board
                
