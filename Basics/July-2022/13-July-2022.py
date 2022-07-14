# 1 : Special Subsequences "AG"
# You have given a string A having Uppercase English letters.

# You have to find how many times subsequence "AG" is there in the given string.

# NOTE: Return the answer modulo 109 + 7 as the answer can be very large.

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        n = len(A)
        totalNoOfG = 0 
        result = 0

        for i in range(n-1, -1, -1):
            if A[i] == 'G' :
                totalNoOfG += 1
            elif A[i] == 'A':
                result += totalNoOfG
        return(result%1000000007)


