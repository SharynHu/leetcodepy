# N can be expressed as k, k + 1, k + 2, ..., k + (i - 1), where k is a positive integer; therefore

# N = k * i + (i - 1) * i / 2 => N - (i - 1) * i / 2 = k * i, which implies that as long as N - (i - 1) * i / 2 is k times of i, we get a solution corresponding to i; Hence iteration of all possible values of i, starting from 1, will cover all cases of the problem.

# Since k*i>=0, we get i*(i-1)/2<N. We can just loop through 1 to sqrt(2*N) to check if we can get a pair of i and k.
class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        count = 0
        i = 1
        while(i*(i-1)/2<N):
            if (N-i*(i-1)/2)%i==0:
                count += 1
            i += 1
        return count
                
