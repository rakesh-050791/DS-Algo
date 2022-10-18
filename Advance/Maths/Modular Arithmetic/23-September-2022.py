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


# 4 : Rearrange Array

# Rearrange a given array so that Arr[i] becomes Arr[Arr[i]] with O(1) extra space.

# Example:

# Input : [1, 0]
# Return : [0, 1]
# Lets say N = size of the array. Then, following holds true :

# All elements in the array are in the range [0, N-1]
# N * N does not overflow for a signed integer


# Approach: 

# store initial value and result in the same element.
# / by n will give the initial value
# % by n will give the final result.

# {4, 0, 2, 1, 3} -> {3, 4, 2, 0, 1}
# n = 5;

# Step I:
# 20, 0, 10, 5, 15 -> / by 5 gives back the original 4, 0, 2, 1, 3

# Step II: Include result in the element
# i = 0
# arr[i] = 20 but actual value is arr[i]/5 = 4 -> Index
# arr[Index] = 15 but actual value is arr[Index]/5 = 3 -> result
# arr[i]+3 = 23 -> 23%5 = 3 -> result, 23/5 = 4 -> Initial value

# {23, 0, 10, 5, 15}

# i = 1
# arr[i] = 0 but actual value is arr[i]/5 = 0 -> Index
# arr[Index] = 23 but actual value is arr[Index]/5 = 4 -> result
# arr[i]+4 = 4 -> 4%5 = 4 -> result, 4/5 = 0 -> Initial value

# {23, 4, 10, 5, 15}

# i = 2
# arr[i] = 10 but actual value is arr[i]/5 = 2 -> Index
# arr[Index] = 10 but actual value is arr[Index]/5 = 2 -> result
# arr[i]+2 = 12 -> 12%5 = 2 -> result, 12/5 = 2 -> Initial value

# {23, 4, 12, 5, 15}

# i = 3
# arr[i] = 5 but actual value is arr[i]/5 = 1 -> Index
# arr[Index] = 4 but actual value is arr[Index]/5 = 0 -> result
# arr[i]+0 = 5 -> 5%5 = 0 -> result, 5/5 = 1 -> Initial value

# {23, 4, 12, 5, 15}

# i = 4
# arr[i] = 15 but actual value is arr[i]/5 = 3 -> Index
# arr[Index] = 5 but actual value is arr[Index]/5 = 1 -> result
# arr[i]+1 = 16 -> 16%5 = 1 -> result, 16/5 = 3 -> Initial value

# {23, 4, 12, 5, 16}

# Step III: %5 of each element will be the final result {3, 4, 2, 0, 1}


class Solution:
    def arrange(self, A):
        n = len(A)
        arr = A 

        #STEP : 1 - Multiply existing array elements with total length of an array i.e n
        for i in range(n):
            arr[i] = arr[i] * n 

        #STEP : 2 - Divide array elements with total length of an array, create Arr[Arr[i]] and again
                    # divide it with total length of an array and sum it with array elements.
        for i in range(n):
            idx = arr[i] // n
            value = arr[idx] // n
            arr[i] = arr[i] + value
        
        #STEP : 3 - Modulo array elements with total length of an array & return array ( to get back the swap value)
        for i in range(n):
            arr[i] = arr[i] % n
        
        return arr
