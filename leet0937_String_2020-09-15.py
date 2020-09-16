class Solution(object):
    def comparator(self, log1, log2):
        id1, log1 = log1.split(" ", 1)
        id2, log2 = log2.split(" ", 1)
        #1. all of the letter-logs come before any digit-log
        if log1[0].isdigit() and log2[0].isalpha():
            return 1
        if log2[0].isdigit() and log1[0].isalpha():
            return -1
        #2. The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  
        if log1[0].isalpha():
            if log1==log2: 
                return 1 if id1>id2 else -1
            else:
                return 1 if log1>log2 else -1
        #3. The digit-logs should be put in their original order.
        return 0
                
        
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        logs.sort(cmp = self.comparator)
        return logs
