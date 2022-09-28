# 1 : Count of divisors
# Given an array of integers A, find and return the count of divisors of each element of the array.

# NOTE: The order of the resultant array should be the same as the input array.

# Input 1:

# A = [2, 3, 4, 5]

# Output 1:

# [2, 2, 3, 2]

# Explanation 1:
#  The number of divisors of 2 : [1, 2], 3 : [1, 3], 4 : [1, 2, 4], 5 : [1, 5]
#  So the count will be [2, 2, 3, 2].

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        N = len(A)

        ## Creating smallest prime factor of a number
        def createspf(n):
            spf = [i for i in range(n)]
            rng = math.sqrt(len(spf))
            i = 2
            while i < rng:
                if spf[i] == i:
                    j = i * i
                    while j < n:
                        if spf[j] == j:
                            spf[j] = i
                        j += i
                i += 1
            return spf
         
        def primefactors(spf,n):
            total = 1
            while n > 1:
                prime = spf[n]
                count = 0
                while n % prime == 0:
                    count += 1
                    n = n // prime
                   
                total = total * (count +1)
            return total

           
        spf = createspf(max(A)+1)
        res = []
        for k in range(N):
            value = primefactors(spf,A[k])
            res.append(value)
           
        return res