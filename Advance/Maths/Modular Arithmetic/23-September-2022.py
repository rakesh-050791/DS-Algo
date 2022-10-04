# 1 : A, B & Modulo

# Given two integers A and B, find the greatest possible positive integer M, such that A % M = B % M.

# Example Input
# Input 1:

# A = 1
# B = 2

# Example Output
# Output 1: 1

# Explanation 1:
# 1 is the largest value of M such that A % M == B % M.

# Approach 

# Lets say r is the remainder ,
# A%M = B%M = r
# p & q are the quotients for A/M , B/M
# A= M*p + r , B = M*q + r  
# r = A-Mp  -----(1)
# r = B-Mq  -----(2)
# Equating (1) & (2)
# A-Mp = B-Mq
# A-B = M(p-q)
# M = (A-B) / (p-q)
# For M to be maximum , (p-q) has to be minimum
# 1 is the possible minimum value for (p-q)
# => M = (A-B) / 1
# So M is the difference between A,B


class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        return abs(A-B)


# 2 : Pair Sum divisible by M

# Given an array of integers A and an integer B, find and return the number of pairs in A whose sum is divisible by B.

# Since the answer may be large, return the answer modulo (109 + 7).

# Example Input
# Input 1:

# A = [1, 2, 3, 4, 5]
# B = 2

# Example Output
# Output 1: 4

# Example Explanation
# Explanation 1:

#  All pairs which are divisible by 2 are (1,3), (1,5), (2,4), (3,5). 
#  So total 4 pairs.

# Approach 1 : 

class Solution:
    def solve(self, A, B):

        freqArray = [0] * B
        n = len(A)
        mod = 1000000007

        # STEP 1 : Storing frequency of remainders % B
        for i in range(n):
            freqArray[A[i] % B] += 1
       
       # STEP 2 : Handle edge cases
       # Edge case 1 
        result = 0
        a = freqArray[0] # no of elements with remainder 0
        result = result + ((a * (a - 1)) // 2)

       # Edge case 2
        if B % 2 == 0:  # Only if B is even (i == j case)
            b = freqArray[ B // 2 ] # no of elements with remainder B / 2
            result = result + ((b * (b - 1)) // 2)


        # STEP 3 : Get all remaining pairs
        i = 1
        j = B-1
        while i < j:
            result =  result + freqArray[i] * freqArray[j]
            i += 1
            j -= 1
        
        return (result % mod)


# Approach 2 :        
class Solution:
    def solve(self, A, B):

        freqArray = [0] * B
        n = len(A)
        mod = 1000000007

        for i in range(n):
            freqArray[A[i] % B] += 1
            result = (freqArray[0]*(freqArray[0]-1)) / 2

        i = 1
        j = B-1
        while i <= j:
            if i == j:
                result += (freqArray[i] * (freqArray[j]-1)) / 2
            else:
                result += freqArray[i] * freqArray[j]
            i+=1
            j-= 1
        return int(result % mod)

