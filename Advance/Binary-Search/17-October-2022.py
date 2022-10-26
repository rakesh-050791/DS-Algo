# 1 :  Square Root of Integer
# Given an integer A.

# Compute and return the square root of A.

# If A is not a perfect square, return floor(sqrt(A)).

# DO NOT USE SQRT FUNCTION FROM THE STANDARD LIBRARY.

# NOTE: Do not use the sqrt function from the standard library. Users are expected to solve this in O(log(A)) time.

# Output Format
# Return floor(sqrt(A))



# Example Input
# Input 1: 11

# Example Output
# Output 1: 3

# Example Explanation
# Explanation:

#  When A = 11 , square root of A = 3.316. It is not a perfect square so we return the floor which is 3.
#  When A = 9 which is a perfect square of 3, so we return 3.

class Solution:
    def sqrt(self, A):
        
        if A == 0:
            return 0

        n = A
        low = 1
        high = n
        result = 1

        while (low <= high):
            mid = (low + high) // 2

            if (mid * mid) == n:
                return mid
            
            elif (mid * mid) < n:
                #search in left direction
                result = mid
                low = mid + 1
                
            elif (mid * mid) > n:
                #search in right direction
                high = mid - 1

        return int(result)
