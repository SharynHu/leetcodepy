# Intuition:

# remove all the cells with value >= min(begin,end)
# sort all remaining unique values
# enumerate all remaining values to find a maximum value that is the minimum value in a path from the begin to the end; for each value, we use DFS to check weather there exists a path from begin to end such that this value is the the minimum among the values in that path.
# if we find that value, we keep Binary Search to try to find a bigger value
# we loose our search criatria and see if there is path from begin to end that all the values in that path >= a smaller value by moving the right pointer to the left
class Solution(object):
    def dfs(self, A, i, j, visited, candidate):
        if i==len(A)-1 and j==len(A[0])-1:
            return True
        visited.add((i,j))
        for next_i, next_j in [[i,j+1], [i,j-1], [i+1, j], [i-1, j]]:
            if 0<=next_i<=len(A)-1 and 0<=next_j<=len(A[0])-1 and (next_i, next_j) not in visited and A[next_i][next_j]>=candidate and self.dfs(A, next_i, next_j,visited, candidate):
                return True
        return False
                
            
    def maximumMinimumPath(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        valueSet = set()
        # generate all candidates
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j]<=min(A[0][0], A[-1][-1]):
                    valueSet.add(A[i][j]) 
        values = list(valueSet)
        values.sort()
        
        left, right = 0, len(values) - 1
        
        while (left+1<right):
            middle = (left+right)/2
            # check if we can find a path with a minimum value less than or equal to the current candidate
            visited = set()
            if self.dfs(A, 0, 0, visited, values[middle]):
                # we try bigger candidates
                left = middle
            else:
                right = middle

        visited= set()
        if self.dfs(A, 0, 0, visited, values[right]):
            return values[right]
        return values[left]
