class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        maxStr = s[0]
        for k in range(2*len(s)-1):
            # if k is odd, it means a letter, if k is even, it means a space
            if k%2==1:
                i = (k-1)/2
                j = (k+1)/2
                
                while(i>=0 and j<len(s)):
                    if s[i]==s[j]:
                        if j-i+1>len(maxStr):
                            maxStr = s[i:j+1]
                        i -= 1
                        j += 1
                    else:
                        break
            if k%2==0:
                i = k/2-1
                j = k/2+1
               
                while(i>=0 and j<len(s)):
                    if s[i]==s[j]:
                        if j-i+1>len(maxStr):
                            maxStr = s[i:j+1]
                        i -= 1
                        j += 1
                    else:
                        break
        return maxStr
