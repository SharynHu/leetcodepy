class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            currSum  = carry + digits[i]
            digits[i] = currSum%10
            carry = currSum/10
        if carry:
            digits = [carry]+digits
        return digits
