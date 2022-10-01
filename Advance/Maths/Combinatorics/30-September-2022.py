# 1 : Sorted Permutation Rank
# Given a string A. Find the rank of the string amongst its permutations sorted lexicographically.
# Assume that no characters are repeated.

# Note: The answer might not fit in an integer, so return your answer % 1000003

# Example Input
# Input 1:
# A = "acb"

# Example Output
# Output 1: 2

# Explanation 1:

# Given A = "acb".
# The order permutations with letters 'a', 'c', and 'b' : 
# abc
# acb
# bac
# bca
# cab
# cba
# So, the rank of A is 2.

class Solution:
	# @param A : string
	# @return an integer
	def findRank(self, A):
        ans = 0
        s = A 
        n = len(A)

        for i in range(n-1):
            count = 0
            for j in range(i+1, n):
                if (s[j] < s[i]):
                    count += 1
            
            ans += (count * self.factorial(n-i-1)) % 1000003
        
        return (ans + 1) % 1000003

    def factorial(self, n):
        if (n == 0 or n == 1):
            return 1
        else:
            return (n * self.factorial(n-1)) % 1000003