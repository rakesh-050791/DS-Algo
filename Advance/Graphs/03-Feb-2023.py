# 1 : Coloring a Cycle Graph
# Given the number of vertices A in a Cyclic Graph.

# Your task is to determine the minimum number of colors required to color the graph so that no two Adjacent vertices have the same color.


# A cyclic graph with A vertices is a graph with A edges, such that it forms a loop. See example test case explanation for more details.



# Problem Constraints
# 3 <= A <= 109



# Input Format
# First argument is an integer A denoting the number of vertices in the Cyclic Graph.



# Output Format
# Return an single integer denoting the minimum number of colors required to color the graph so that no two Adjacent vertices have the same color.



# Example Input
# Input 1: 5
# Input 2: 4

# Example Output
# Output 1: 3
# Output 2: 2


# Solution Explanation 

# Cycle:- cycle is a path of edges and vertices wherein a vertex is reachable from itself. or in other words, it is a Closed walk.

# Even Cycle:- In which Even number of vertices is present is known as Even Cycle.

# Odd Cycle:- In which Odd number of Vertices is present is known as Odd Cycle.

# Approach:

# If the no. of vertices is Even then it is Even Cycle and to color such graph we require 2 colors.
# If the no. of vertices is Odd then it is Odd Cycle and to color such graph we require 3 colors.



class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A == 1:
            return 1
        elif A % 2 == 0:
            return 2
        else:
            return 3


# 2 : Rotten Oranges
# Given a matrix of integers A of size N x M consisting of 0, 1 or 2.

# Each cell can have three values:

# The value 0 representing an empty cell.

# The value 1 representing a fresh orange.

# The value 2 representing a rotten orange.

# Every minute, any fresh orange that is adjacent (Left, Right, Top, or Bottom) to a rotten orange becomes rotten. Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1 instead.

# Note: Your solution will run on multiple test cases. If you are using global variables, make sure to clear them.

# Problem Constraints
# 1 <= N, M <= 1000

# 0 <= A[i][j] <= 2

# Input Format
# The first argument given is the integer matrix A.

# Output Format
# Return the minimum number of minutes that must elapse until no cell has a fresh orange.

# If this is impossible, return -1 instead.

# Example Input
# Input 1:

# A = [   [2, 1, 1]
#         [1, 1, 0]
#         [0, 1, 1]   ]
# Input 2:

 
# A = [   [2, 1, 1]
#         [0, 1, 1]
#         [1, 0, 1]   ]


# Example Output
# Output 1:   4
# Output 2:  -1


# Example Explanation
# Explanation 1: Max of 4 using (0,0) , (0,1) , (1,1) , (1,2) , (2,2)

# Explanation 2: Task is impossible

from collections import deque

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        rows = len(A)
        cols = len(A[0])
        grid = A

        time , freshOranges = 0, 0

        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    freshOranges += 1

                if grid[r][c] ==2:
                    q.append([r,c])
        
        directions = [ [0, 1], [0, -1], [1, 0], [-1, 0] ]

        while q and freshOranges > 0:
            for i in range(len(q)):
                r , c = q.popleft()

                for dr, dc in directions:
                    row, col = dr + r, dc + c

                    if (row < 0 or row == len(grid) or 
                        col < 0 or col == len(grid[0]) or 
                        grid[row][col] != 1):

                        continue

                    grid[row][col] = 2
                    q.append([row, col])
                    freshOranges -= 1
            
            time += 1
        
        return time if freshOranges == 0 else -1
