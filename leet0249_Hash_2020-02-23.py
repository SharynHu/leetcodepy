# Note: 
#    1. duplicates must be added;
#    2. "az"->"ba" is allowed

class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        resMap = {}
        
        for string in strings:
            found = False
            for i in range(26):
                trans = ""
                for j in range(len(string)):
                    trans += chr((ord(string[j])+i)%26+ord('a'))
                if trans in resMap:
                    found = True
                    resMap[trans].append(string)
                    break
            if not found:
                resMap[string] = [string]
               
        
        res = []
        for key in resMap:
            res.append(resMap[key])
        return res
                    
