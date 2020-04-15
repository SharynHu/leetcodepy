#我们不知道每个字母对应的单词的长度，因此需要一个个尝试
class Solution(object):
    def backtrack(self, pattern, i, str, j, hash1, hash2):
        if i==len(pattern) and j==len(str):
            return True
        if i==len(pattern) or j==len(str):
            return False
        #对于字母pattern[i], 如果它已经有对应的词，那么找到这个词
        if pattern[i] in hash1:
            word = hash1[pattern[i]]  
            #那么和当前的i对应的词应该就是str[j:j+len(word)]
            if word!=str[j:j+len(word)]:
                return False
            if word not in hash2 or hash2[word]!=pattern[i]:
                return False
            return self.backtrack(pattern, i+1, str, j+len(word), hash1, hash2)
        #如果当前字母没有已经对应的词，那么尝试每种可能
        for k in range(j, len(str)):
            word = str[j:k+1]
            hash1[pattern[i]] = word
            if word in hash2 and hash2[word]!=pattern[i]:
                hash1.pop(pattern[i])
                continue
            hash2[word]=pattern[i]
            tmpRes = self.backtrack(pattern, i+1, str, j+len(word), hash1, hash2)
            hash1.pop(pattern[i])
            hash2.pop(word)
            if tmpRes:
                return True
        return False
            
            
        
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        letterToWord = {}
        wordToLetter = {}
        return self.backtrack(pattern, 0, str, 0, letterToWord, wordToLetter)
