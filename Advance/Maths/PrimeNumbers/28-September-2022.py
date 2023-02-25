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

# 2 : Lucky Numbers
# A lucky number is a number that has exactly 2 distinct prime divisors.

# You are given a number A, and you need to determine the count of lucky numbers between the range 1 to A (both inclusive).
# Example Input
# Input 1:

# A = 8

# Example Output
# Output 1: 1

# Explanation 1:

#  Between [1, 8] there is only 1 lucky number i.e 6.
#  6 has 2 distinct prime factors i.e 2 and 3.

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        res = 0

        arr = [0]*(A+1)
        
        p = 2
        while p <= A:
            # if we encounter 2 then that has 2 distinct primes
            if arr[p] == 2: 
                res += 1
                p += 1
                continue
            
            # 0 indicates a new prime number
            if arr[p] == 0:
                for i in range(2*p, A+1, p):
                    arr[i] += 1

            p += 1
        return res

# 3 : Prime Subsequences

# Given an array A having N positive numbers. You have to find the number of Prime subsequences of A.

# A Prime subsequence is one that has only prime numbers, for example [2, 3], [5] are the Prime subsequences where [2, 4] and [1, 2, 3, 4] are not.



# Input Format

# The first argument given is an Array A, having N integers.
# Output Format

# Return an integer X, i.e number of Prime subsequences. 
# As X can be very large print X % (1000000007), here % is modulus operator.
# Constraints

# 1 <= N <= 1e3
# 1 <= A[i] <= 1e6
# For Example

# Input:
#     A = [1, 2, 3]
# Output:
#      3

# Explanation:
#     no. Subsequences      Prime subsequences
#     1.  [1]                     No
#     2.  [1, 2]                  No
#     3.  [1, 3]                  No
#     4.  [1, 2, 3]               No
#     5.  [2]                     Yes
#     6.  [2, 3]                  Yes
#     7.  [3]                     Yes
#     8.  []                      No

#     here we have 3 subsequences(5, 6, 7) those have only prime number(s). 

class Solution:
    # @param A : list of integers
    # @return an integer
    def isPrime(self,num):
        root = int(math.sqrt(num))
        for i in range(2,root+1):
            if num%i==0:
                return False
        return True
        
    def solve(self, A):

        mod = 1000000007
        count = 1
        for elem in A:
            if elem > 1 and self.isPrime(elem):
                count = (count%mod * 2)%mod

        return count-1


# 4 : Prime Addition
# You are given an even number N and you need to represent the given number as the sum of primes. The prime numbers do not necessarily have to be distinct. It is guaranteed that at least one possible solution exists.

# You need to determine the minimum number of prime numbers needed to represent the given number.

# Input

# The first argument contains an integer N,the number you need to represent (2<=N<=10^9).
# Output

# Return an integer which is the minimum number of prime numbers needed to represent the given number N.
# Examples

# Input

# 26
# Output

# 2
# Explanation

# Testcase 1-

# You can represent 26 as: 13+13
# So we require minimum of 2 prime numbers to represent the number 26.

#ref : https://www.youtube.com/watch?v=MxiTG96QOxw&t=33s


class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A == 2: return 1
        return 2
