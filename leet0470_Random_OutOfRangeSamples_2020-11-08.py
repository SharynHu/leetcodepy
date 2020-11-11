# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        while(True):
            # get index from 1 to 49
            a,  b= rand7(), rand7()
            index = (a-1)*7+b
            if index<=40:
                return 1+(index-1)%10
            
            # get index from 1 to 63
            a = index-40
            b = rand7()
            index = b+(a-1)*7
            if index<=60:
                return 1+(index-1)%10
            
            # get index from 1 to 21
            a = index-60
            b = rand7()
            index = b+(a-1)*7
            if index<=20:
                return 1+(index-1)%10
            
