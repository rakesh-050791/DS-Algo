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


# 5 : Prime Sum

# Given an even number A ( greater than 2 ), return two prime numbers whose sum will be equal to the given number.

# If there is more than one solution possible, return the lexicographically smaller solution.

# If [a, b] is one solution with a <= b, and [c,d] is another solution with c <= d, then 
# [a, b] < [c, d], If a < c OR a==c AND b < d. 
# NOTE: A solution will always exist. Read Goldbach's conjecture.



# Problem Constraints
# 4 <= A <= 2*107



# Input Format
# First and only argument of input is an even number A.



# Output Format
# Return a integer array of size 2 containing primes whose sum will be equal to given number.



# Example Input
#  4


# Example Output
#  [2, 2]


# Example Explanation
#  There is only 1 solution for A = 4.

#Ref : https://www.youtube.com/watch?v=MxiTG96QOxw&t=33s

class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
        if A == 4: return [2,2]

        # Creating Prime Bool Seive    
        def creatseive(n):
            pf = [True] * (n)
            pf[0] , pf[1] = False , False
            i = 2
            while i * i  < n:
                if pf[i] == True:
                    j = i * i
                    while j < n:
                        pf[j] = False
                        j +=i
                i +=1
               
            return pf
           
        spf = creatseive(A+1)

        # Using Two Pointer x Goldbach's conjecture Approach
        i = 2
        j = A - 2

        while i < j:
            if spf[i] and spf[j]:
                cur_sum = i + j
                if cur_sum == A:
                    arr = [i,j]
                    return arr
            i += 1
            j -= 1

# 6 : Number Of Open Doors
# Given an integer A, which denotes the number of doors in a row numbered 1 to A. All the doors are closed initially.

# A person moves to and fro, changing the states of the doors as follows: the person opens a door that is already closed and closes a door that is already opened.

# In the first go, he/she alters the states of doors numbered 1, 2, 3, … , A.
# In the second go, he/she alters the states of doors numbered 2, 4, 6 ….
# In the third go, he/she alters the states of doors numbered 3, 6, 9 …
# This continues till the A'th go in, which you alter the state of the door numbered A.

# Find and return the number of open doors at the end of the procedure.



# Problem Constraints
# 1 <= A <= 109



# Input Format
# The only argument given is integer A.



# Output Format
# Return the number of open doors at the end of the procedure.



# Example Input
# Input 1:

#  A = 5
# Input 2:

#  A = 6


# Example Output
# Output 1:

#  2
# Output 2:

#  2 


# Example Explanation
# Input 1:

#  In the first go, he/she alters the states of doors numbered 1, 2, 3, 4, 5. Now, all doors are open.
#  In the second go, he/she closes the doors numbered 2, 4.
#  In the third go, he/she closes the door numbered 3.
#  In the fourth go, he/she open the door numbered 4.
#  In the fifth go, he/she closes the door numbered 5.
#  Doors opened at the end are 1 and 4.
# Input 2:

#  In the first go, he/she alters the states of doors numbered 1, 2, 3, 4, 5, 6. Now, all doors are open.
#  In the second go, he/she closes the doors numbered 2, 4, 6.
#  In the third go, he/she closes the door numbered 3 and opens door 6.
#  In the fourth go, he/she open the door numbered 4.
#  In the fifth go, he/she closes the door numbered 5.
#  In the sixth go, he/she closes the door numbered 6.
#  Doors opened at the end are 1 and 4.

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        '''
        0 : Close
        1 : Open
        '''

        '''Brute Force'''
        # arr = [0]*(A+1)
        # for i in range(A):
        #     for j in range(i+1, A+1, i+1):
        #         arr[j] = int(not arr[j])

        # return sum(arr)

        ''' Optimal
        by Observations from A = (1 to 10): ans is floor value of sqrt(A)'''

        return int(A**0.5)

