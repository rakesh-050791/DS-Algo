# 1 : Find a peak element

# Given an array of integers A, find and return the peak element in it. An array element is peak if it is NOT smaller than its neighbors.

# For corner elements, we need to consider only one neighbor. We ensure that answer will be unique.

# NOTE: Users are expected to solve this in O(log(N)) time. The array may have duplicate elements.

# Example Input
# Input 1: A = [1, 2, 3, 4, 5]

# Example Output
# Output 1: 5

# Example Explanation
# Explanation 1: 5 is the peak.


class Solution:
    def solve(self, A):
        n = len(A)
        arr = A

        if n == 1:
            return A[0]

        if arr[0] >= arr[1]:
            return arr[0]
        
        if arr[n-1] >= arr[n-2]:
            return arr[n-1]

        low = 0
        high = n-1

        while (low < high):
            mid = (low + high) // 2

            if (arr[mid] > arr[mid-1]) and (arr[mid] > arr[mid+1]):
                return arr[mid]

            elif arr[mid-1] > arr[mid]:
                high = mid - 1
                
            elif arr[mid+1] > arr[mid]:
                low = mid + 1
            
        return arr[low]
            

# 2 : Search in Bitonic Array!

# Given a bitonic sequence A of N distinct elements, write a program to find a given element B in the bitonic sequence in O(logN) time.

# NOTE:

# A Bitonic Sequence is a sequence of numbers which is first strictly increasing then after a point strictly decreasing.


# Example Input
# Input 1:

#  A = [3, 9, 10, 20, 17, 5, 1]
#  B = 20

# Example Output
# Output 1: 3
 
# Example Explanation
# Explanation 1: B = 20 present in A at index 3

class Solution:
    def solve(self, A, B):
        n = len(A)

        #Searching Bitonic element
        low = 0
        high = n-1
        while (low <= high):
            mid = (low + high) // 2

            if (A[mid-1] < A[mid]) and (A[mid] > A[mid+1]):
                bionicPoint = mid
                break

            elif A[mid+1] > A[mid]:
                low = mid + 1
            elif A[mid-1] > A[mid]:
                high = mid - 1

        # Binary search on the left side of the Bitonic element
        low = 0
        high = bionicPoint-1
        while (low <= high):
            mid = (low + high) // 2

            if A[mid] == B:
                return mid
            
            elif A[mid] < B:
                low = mid + 1
            else:
                high = mid - 1

        # Binary search on the right side of the Bitonic element
        low = bionicPoint
        high = n-1
        while (low <= high):
            mid = (low + high) // 2

            if A[mid] == B:
                return mid
            
            elif A[mid] < B:
                high = mid - 1
            else:
                 low = mid + 1

        return -1


# 3 Sorted Insert Position

# Given a sorted array A of size N and a target value B, return the index (0-based indexing) if the target is found.
# If not, return the index where it would be if it were inserted in order.

# NOTE: You may assume no duplicates in the array. Users are expected to solve this in O(log(N)) time.


# Input Format
# The first argument is an integer array A of size N.
# The second argument is an integer B.



# Output Format
# Return an integer denoting the index of target value.


# Example Input
# Input 1:

# A = [1, 3, 5, 6]
# B = 5 
# Input 2:

# A = [1]
# B = 1


# Example Output
# Output 1: 2 
# Output 2: 0


# Example Explanation
# Explanation 1:

# The target value is present at index 2. 
# Explanation 2:

# The target value is present at index 0.

class Solution:
    def searchInsert(self, A, B):
        n = len(A)
        low = 0
        high = n-1

        while low <= high:
            mid = (low + high) // 2

            if A[mid] == B:
                return mid
            
            if A[mid] > B:
                high = mid - 1
            elif A[mid] < B:
                low = mid + 1
                
        #low indicates position where new element needs to be inserted into array after while loop breaks
        return low 


# 4 Search for a Range

# Given a sorted array of integers A(0 based index) of size N, find the starting and the ending position of a given integer B in array A.

# Your algorithm's runtime complexity must be in the order of O(log n).

# Return an array of size 2, such that the first element = starting position of B in A and the second element = ending position of B in A, if B is not found in A return [-1, -1].

# Input Format
# The first argument given is the integer array A.
# The second argument given is the integer B.



# Output Format
# Return an array of size 2, such that the first element = starting position of B in A and the second element = the ending position of B in A if B is not found in A return [-1, -1].



# Example Input
# Input 1:

#  A = [5, 7, 7, 8, 8, 10]
#  B = 8
# Input 2:

#  A = [5, 17, 100, 111]
#  B = 3


# Example Output
# Output 1: [3, 4]
# Output 2: [-1, -1]


# Example Explanation
# Explanation 1:

#  The first occurence of 8 in A is at index 3.
#  The second occurence of 8 in A is at index 4.
#  ans = [3, 4]
# Explanation 2:

#  There is no occurence of 3 in the array.

class Solution:
    def searchRange(self, A, B):
        n = len(A)
        low = 0
        high = n-1
        startIndex = self.getFirstOccurence(A, B, low, high)
        endIndex = self.getLastOccurence(A, B, low, high)
        return [startIndex, endIndex]

    
    def getFirstOccurence(self, A, B, low, high):
        firstOccurence = -1
        while low <= high:
            mid = (low + high) // 2

            if A[mid] == B:
                firstOccurence = mid
                high = mid - 1
                
            elif A[mid] > B:
                high = mid - 1
            elif A[mid] < B:
                low = mid + 1

        return firstOccurence
    
    def getLastOccurence(self, A, B, low, high):
        lastOccurence = -1
        while low <= high:
            mid = (low + high) // 2

            if A[mid] == B:
                lastOccurence = mid
                low = mid + 1

            elif A[mid] > B:
                high = mid - 1
            elif A[mid] < B:
                low = mid + 1
        
        return lastOccurence


# 5 : Matrix Search

# Given a matrix of integers A of size N x M and an integer B. Write an efficient algorithm that searches for integer B in matrix A.

# This matrix A has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than or equal to the last integer of the previous row.
# Return 1 if B is present in A, else return 0.

# NOTE: Rows are numbered from top to bottom, and columns are from left to right.



# Problem Constraints
# 1 <= N, M <= 1000
# 1 <= A[i][j], B <= 106



# Input Format
# The first argument given is the integer matrix A.
# The second argument given is the integer B.



# Output Format
# Return 1 if B is present in A else, return 0.



# Example Input
# Input 1:

# A = [ 
#       [1,   3,  5,  7]
#       [10, 11, 16, 20]
#       [23, 30, 34, 50]  
#     ]
# B = 3
# Input 2:

# A = [   
#       [5, 17, 100, 111]
#       [119, 120, 127, 131]    
#     ]
# B = 3


# Example Output
# Output 1:

# 1
# Output 2:

# 0


# Example Explanation
# Explanation 1:

#  3 is present in the matrix at A[0][1] position so return 1.
# Explanation 2:

#  3 is not present in the matrix so return 0.

# Approach 1 : (https://dcga8ozhbq5np.cloudfront.net/original/2X/8/8acfc22f7bb54681bc3530e3c10359785f02aa38.jpeg)

class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        rows = len(A)
        cols = len(A[0])
        
        low = 0
        high = (rows * cols) - 1
        
        while low <= high:
            
            mid = (low + high) // 2
            
            rowidx = mid // cols # i
            colidx = mid % cols  # j
            
            if A[rowidx][colidx] == B:
                return 1
            
            if A[rowidx][colidx] > B:
                high = mid - 1
                
            else:
                low = mid + 1
                
        return 0 

# TC : log(N*M)


# Approach 2 
class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        rows = len(A)
        cols = len(A[0])

        # finding the potential row
        l = 0
        h = rows - 1
        # potential_row = 0
        while(l <= h):
            mid = (l + h) // 2

            if A[mid][0] == B:
                return 1
            elif A[mid][0] < B:
                l = mid + 1
            else:
                h = mid - 1
       
        row = l - 1

        # Now that we have the row, apply BS to find B in that row
        # print(row)
        l = 0
        h = cols - 1

        while(l <= h):
            mid = (l + h) // 2

            if A[row][mid] == B:
                return 1
            elif A[row][mid] < B:
                l = mid + 1
            else:
                h = mid - 1
       
        return 0
        