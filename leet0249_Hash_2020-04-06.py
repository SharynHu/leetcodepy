class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        counts = collections.Counter(strings)
        
        res = []
        while(counts):
            currStr, count = counts.popitem()
            tempRes = [currStr]*count
            #find all the successive strings for currStr
            for j in range(26):
                successive = ""
                for letter in currStr:
                    successive += chr((ord(letter)-ord('a')+j)%26+ord('a'))
                if successive in counts:
                    tempRes += [successive]*counts[successive]
                    counts.pop(successive)
            res.append(tempRes)
        return res
