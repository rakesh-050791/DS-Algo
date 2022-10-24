# 1 : Painter's Partition Problem
# Given 2 integers A and B and an array of integers C of size N. Element C[i] represents the length of ith board.
# You have to paint all N boards [C0, C1, C2, C3 … CN-1]. There are A painters available and each of them takes B units of time to paint 1 unit of the board.

# Calculate and return the minimum time required to paint all boards under the constraints that any painter will only paint contiguous sections of the board.
# NOTE:
# 1. 2 painters cannot share a board to paint. That is to say, a board cannot be painted partially by one painter, and partially by another.
# 2. A painter will only paint contiguous boards. This means a configuration where painter 1 paints boards 1 and 3 but not 2 is invalid.

# Return the ans % 10000003.

# Input Format
# The first argument given is the integer A.
# The second argument given is the integer B.
# The third argument given is the integer array C.

# Output Format
# Return minimum time required to paint all boards under the constraints that any painter will only paint contiguous sections of board % 10000003.

# Example Input
# Input 1:

# A = 2
# B = 5
# C = [1, 10]

# Example Output : 50

# Example Explanation
# Explanation 1:

# Possibility 1:- One painter paints both blocks, time taken = 55 units.
# Possibility 2:- Painter 1 paints block 1, painter 2 paints block 2, time take = max(5, 50) = 50
# There are no other distinct ways to paint boards.
# ans = 50 % 10000003

class Solution:
    def paint(self, A, B, C):
        n = len(C)
        for i in range(n):
            C[i] = B * C[i]
        
        return self.binarySearch(A, C) 
    
    def binarySearch(self, painters, board):
        mod = 10000003
        low = max(board)
        high = sum(board)
        result = high

        while (low <= high):
            mid = (low + high) // 2

            if (self.check(painters, board, mid) == True):
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        return result % mod
    

    def check(self, painters, board, mid):
        n = len(board)
        total = 0 
        count = 0

        for i in range(n):
            total += board[i]

            if total > mid:
                count += 1
                total = board[i]

                if count == painters:
                    return False
        return True
        

# 3 : Allocate Books

# Given an array of integers A of size N and an integer B.

# The College library has N books. The ith book has A[i] number of pages.

# You have to allocate books to B number of students so that the maximum number of pages allocated to a student is minimum.

# A book will be allocated to exactly one student.
# Each student has to be allocated at least one book.
# Allotment should be in contiguous order, for example: A student cannot be allocated book 1 and book 3, skipping book 2.
# Calculate and return that minimum possible number.

# NOTE: Return -1 if a valid assignment is not possible.


# Input Format
# The first argument given is the integer array A.
# The second argument given is the integer B.



# Output Format
# Return that minimum possible number.



# Example Input
# A = [12, 34, 67, 90], B = 2


# Example Output : 113


# Example Explanation
# There are two students. Books can be distributed in following fashion : 

# 1)  [12] and [34, 67, 90]
#     Max number of pages is allocated to student 2 with 34 + 67 + 90 = 191 pages
# 2)  [12, 34] and [67, 90]
#     Max number of pages is allocated to student 2 with 67 + 90 = 157 pages 
# 3)  [12, 34, 67] and [90]
#     Max number of pages is allocated to student 1 with 12 + 34 + 67 = 113 pages
#     Of the 3 cases, Option 3 has the minimum pages = 113.


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def books(self, A, B):
        n = len(A)
        if B > n :
            return -1
        return self.binarySearch(A, B)

    
    def binarySearch(self, books, students):
        low = max(books)
        high = sum(books)
        result = high

        while (low <= high):
            mid = (low + high) // 2

            if (self.check(books, students, mid) == True):
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return result
    
    def check(self, books, totalStudents, mid):
        n = len(books)
        pages = 0
        studentsCount = 1

        for i in range(n):
            if pages + books[i] <= mid:
                pages += books[i]
            else:
                studentsCount += 1
                pages = books[i]

        if studentsCount > totalStudents:
                return False
        return True


# 4 : Food Packets Distribution
# The government wants to set up B distribution offices across N cities for the distribution of food
# packets. The population of the ith city is A[i]. Each city must have at least 1 office, and people can go to an office of their own city. We want to maximize the minimum number of people who can get food in any single office.


# Input Format
# The first line of input contains an integer array A. 

# The second line of input contains an integer B.



# Output Format
# Return one integer representing the maximum number of people who can get food in any single office.


# Example Input
# Input 1:

# A = [10000, 20000, 30000]
# B = 6



# Example Output
# Output 1: 10000


# Example Explanation
# Explanation 1:

#   1 office can be opened in the first city,
#   2 offices in the second city and
#   3 in the third. This way ,
#   10,000 people can get food in the office in the first city, and
#   10,000 people can get food in each office in the second city and
#   10,000 people can get food in third city.
#   We will allot 10000 people in each office in the third city. 
#   Had we alloted more in some office, we had to allot lesser in some other office which will reduce the answer.

class Solution:
    def solve(self, A, B):
        n = len(A)        

        low = 0
        high = min(A)
        result = -1

        while (low <= high):
            mid = (low + high) // 2

            if self.check(A, B, mid):
                result = mid
                low = mid + 1
            else:
                high = mid - 1 
        return 0 if result == -1 else result

    def check(self, A, B, mid):
        centers = 0
        for i in range(len(A)):
            if mid == 0:
                centers += A[i]
            else:
                centers += A[i]//mid
        return centers >= B

