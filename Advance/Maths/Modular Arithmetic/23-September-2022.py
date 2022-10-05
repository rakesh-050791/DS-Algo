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

# 3 : Prime Modulo Inverse
# Given two integers A and B. Find the value of A-1 mod B where B is a prime number and gcd(A, B) = 1.

# A-1 mod B is also known as modular multiplicative inverse of A under modulo B.

# Example Input
# Input 1:

#  A = 3
#  B = 5


# Example Output
# Output 1: 2

# Example Explanation
# Explanation 1:

#  Lets say A-1 mod B = X, then (A * X) % B = 1.
#  3 * 2 = 6, 6 % 5 = 1.


class Solution:
    def solve(self, A, B):
        #using FERMET's Little Theoram  -> calculate (A^B-2 % B) % B 
        result = self.calculatePower(A, B-2, B) % B
        return result

    
    def calculatePower(self, base, exponent, mod):
        if base == 0:
            return 0 #if 0 ^ n where n = any natural number, we get 0 only. Eg: 0 ^ 2 = 0
        
        if exponent == 0:
            return 1 #If power is 0, we get 1 for all base values.

        # storing the recursion calls in a variable power which gives us the SC: O(log N_base2)
        power = self.calculatePower(base, exponent // 2, mod)

        # Using modulo to keep the multiplication of two max integers in the worst case also comes in the range [0, mod-1]
        if exponent % 2 == 0: #If B is even, powers can be broken in equal parts
            return ((power % mod) * (power % mod)) % mod
        else:
            return ((power % mod) * (power % mod) * (base % mod)) % mod

