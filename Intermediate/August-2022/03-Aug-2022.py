# 1: Arithmetic Progression?
# Given an integer array A of size N. Return 1 if the array can be arranged to form an arithmetic progression, 
# otherwise return 0.
# A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        sortedA = sorted(A)

        if len(A) <= 1:
            return 0

        diff = sortedA[1] - sortedA[0]

        for i in range(1, len(A)-1):
            if ((sortedA[i+1] - sortedA[i]) == diff):
                pass
            else:
                return 0
        return 1



# 2 : Noble Integer 
# Given an integer array A, find if an integer p exists in the array 
# such that the number of integers greater than p in the array equals p.

class Solution:
	# @param A : list of integers
	# @return an integer
	def solve(self, A):
        A.sort()

        if A[0] == 0:
            return 1

        for i in range(1, len(A)):
            if A[i] != A[i-1]:
                count = i

            if A[i] == count:
                result += 1
        
        
        return result if result >= 1 else -1



class Solution:
	# @param A : list of integers
	# @return an integer
	def solve(self, A):
        A.sort()
     
       
        n = len(A)
       
        for i in range(n - 1):
           
            if A[i] == A[i + 1]:
                continue
               
           
            if A[i] == n - i - 1:
                return 1
       
        if A[n - 1] == 0:
            return 1
        return -1

# 3 : Sort by Color

# Given an array with N objects colored red, white, or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent red, white, and blue, respectively.

# Note: Using the library sort function is not allowed.

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def sortColors(self, A):
        zeroCount, oneCount , twoCount = [], [], []
        for i in A:
            if i == 0:
                zeroCount.append(i)
            elif i == 1:
                oneCount.append(i)
            else:
                twoCount.append(i)

        return(zeroCount + oneCount + twoCount)






