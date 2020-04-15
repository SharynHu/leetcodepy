class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split(' ')
        if len(pattern)!=len(words):
            return False
        wordToLetter = {}
        letterToWord = {}
        for i in range(len(pattern)):
            word = words[i]
            letter = pattern[i]
            if letter in letterToWord and word in wordToLetter and letterToWord[letter] == word and wordToLetter[word]==letter:
                continue
            if letter not in letterToWord and word not in wordToLetter:
                letterToWord[letter] = word
                wordToLetter[word] = letter
                continue
            return False
        return True
