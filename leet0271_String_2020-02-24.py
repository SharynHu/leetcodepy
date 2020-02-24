#Keypoint: keep the length info for each string while it doesn't cause confusion
class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        for string in strs:
            transformed = ""
            for char in string:
                if char=='/':
                    #转义
                    transformed += '/'+char
                else:
                    transformed += char
            # use '/0' to mark the end of the string
            res += transformed + '/0'
        return res

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return []
        
        res = []
        currStr = ""
        i = 0
        while(i<len(s)):
            if i<len(s)-1 and s[i]+s[i+1]=='//':
                currStr += '/'
                i += 2
                continue
            if i<len(s)-1 and s[i]+s[i+1]=='/0':
                #we are at the end of the string
                res.append(currStr)
                currStr = ""
                i += 2
                continue
            currStr += s[i]
            i += 1
        return res
