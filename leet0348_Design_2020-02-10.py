#规则：
#两个人轮流往棋盘上放棋子；谁先在某一行/列/对角线上放满自己的棋子谁先赢，游戏结束。
class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.n = n
        self.rows = [[0]*n for i in range(2)]
        self.cols = [[0]*n for i in range(2)]
        self.diagLeft = [0, 0]
        self.diagRight = [0, 0]

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        # check row
        self.rows[player-1][row] += 1
        if self.rows[player-1][row] == self.n:
            return player
        #check column
        self.cols[player-1][col] += 1
        if self.cols[player-1][col] ==self.n:
            return player
        # check the left diagnal
        if row == col:
            self.diagLeft[player-1] += 1
            if self.diagLeft[player-1] == self.n:
                return player
        # check the right diagnal
        if row == self.n-col-1:
            self.diagRight[player-1] += 1
            if self.diagRight[player-1] == self.n:
                return player
        # no one wins, return 0
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)