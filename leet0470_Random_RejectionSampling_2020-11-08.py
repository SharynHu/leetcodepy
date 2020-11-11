# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        while(True):
            row, col = rand7(), rand7()
            index = (row-1)*7+col
            if index>40:
                continue
            else:
                return 1+(index-1)%10
