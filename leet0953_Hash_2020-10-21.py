class Solution(object):
    def check(self, s1, s2, orderDict):
        """
        check if s1<=s2 under orderDict
        """
        for i in range(min(len(s1), len(s2))):
            if orderDict[s1[i]]<orderDict[s2[i]]:
                return True
            if orderDict[s1[i]]>orderDict[s2[i]]:
                return False
        if len(s1)<=len(s2):return True
        return False
    
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        orderDict = dict()
        for i in range(len(order)):
            orderDict[order[i]] = i
        if len(words)<=1:
            return True
        for i in range(1, len(words)):
            if not self.check(words[i-1], words[i], orderDict):
                return False
        return True
