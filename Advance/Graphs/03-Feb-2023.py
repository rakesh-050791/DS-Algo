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


# 3 : Distance of nearest cell

# Given a matrix of integers A of size N x M consisting of 0 or 1.

# For each cell of the matrix find the distance of nearest 1 in the matrix.

# Distance between two cells (x1, y1) and (x2, y2) is defined as |x1 - x2| + |y1 - y2|.

# Find and return a matrix B of size N x M which defines for each cell in A distance of nearest 1 in the matrix A.

# NOTE: There is atleast one 1 is present in the matrix.



# Problem Constraints
# 1 <= N, M <= 1000

# 0 <= A[i][j] <= 1



# Input Format
# The first argument given is the integer matrix A.



# Output Format
# Return the matrix B.



# Example Input
# Input 1:

#  A = [
#        [0, 0, 0, 1]
#        [0, 0, 1, 1] 
#        [0, 1, 1, 0]
#      ]
# Input 2:

#  A = [
#        [1, 0, 0]
#        [0, 0, 0]
#        [0, 0, 0]  
#      ]


# Example Output
# Output 1:

#  [ 
#    [3, 2, 1, 0]
#    [2, 1, 0, 0]
#    [1, 0, 0, 1]   
#  ]
# Output 2:

#  [
#    [0, 1, 2]
#    [1, 2, 3]
#    [2, 3, 4] 
#  ]


# Example Explanation
# Explanation 1:

#  A[0][0], A[0][1], A[0][2] will be nearest to A[0][3].
#  A[1][0], A[1][1] will be nearest to A[1][2].
#  A[2][0] will be nearest to A[2][1] and A[2][3] will be nearest to A[2][2].
# Explanation 2:

#  There is only a single 1. Fill the distance from that 1.

from collections import deque 
class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, grid):
        N , M = len(grid) , len(grid[0])

        visited = [[False]*M for _ in range(N)]

        q = deque()
        
        for i in range(N):
            for j in range(M):
                # we are appending all the Ones intially in Queue 
                if grid[i][j] == 1:
                    visited[i][j] = True 
                    q.append((i,j ,0))
                    grid[i][j] = 0              # make it zero 
                    
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        
        while q:
            row , col  , count = q.popleft()
            
            for i , j in directions:
                cr = row + i
                cc = col + j 
                
                if cr < 0 or cc < 0 or cr >= N or cc >= M or visited[cr][cc] or grid[cr][cc] != 0:
                    continue
                
                grid[cr][cc] = count + 1
                visited[cr][cc] = True
                q.append( (cr,cc , count + 1) )
                
                
        return grid

# 4 : Check Bipartite Graph
# Given a undirected graph having A nodes. A matrix B of size M x 2 is given which represents the edges such that there is an edge between B[i][0] and B[i][1].

# Find whether the given graph is bipartite or not.

# A graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B

# Note:

# There are no self-loops in the graph.

# No multiple edges between two pair of vertices.

# The graph may or may not be connected.

# Nodes are Numbered from 0 to A-1.

# Your solution will run on multiple testcases. If you are using global variables make sure to clear them.



# Problem Constraints
# 1 <= A <= 100000

# 1 <= M <= min(A*(A-1)/2,200000)

# 0 <= B[i][0],B[i][1] < A



# Input Format
# The first argument given is an integer A.

# The second argument given is the matrix B.



# Output Format
# Return 1 if the given graph is bipartide else return 0.



# Example Input
# Input 1:

# A = 2
# B = [ [0, 1] ]
# Input 2:

# A = 3
# B = [ [0, 1], [0, 2], [1, 2] ]


# Example Output
# Output 1:

# 1
# Output 2:

# 0


# Example Explanation
# Explanation 1:

# Put 0 and 1 into 2 different subsets.
# Explanation 2:

 
# It is impossible to break the graph down to make two different subsets for bipartite matching

from collections import deque
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def bfs(self,src,graph,visited)-> bool:
        q = deque()
        q.append((src,'red'))
        visited[src] = True

        while q:
            nodes = len(q)
            
            for _ in range(nodes):
                cur_node , parent_color = q.popleft()
                # print("cur_node",cur_node)
                for child in graph[cur_node]:
                    # if not visited then mark adjacent nodes to different color 
                    if not visited[child]:
                        # register the current colo
                        if parent_color == 'red':
                            q.append( (child,'black') )
                            visited[child] = 'black'
                        else:
                            q.append( (child,'red') )
                            visited[child] = 'red'
                    else:
                        # that means already visted now check color is same as parent color
                        if parent_color == visited[child]:
                            return False
                        
        return True 

    def createAdj(self,B,N):
        adj_list  = [[] for _ in range(N)]

        for cur in range(len(B)):
            row = B[cur][0]
            val = B[cur][1]

            adj_list[row].append(val)
            adj_list[val].append(row)

        return adj_list

    def solve(self, N, B):
        
        graph = self.createAdj(B,N)

        visited = [False] * (N)
        
        for node in range(N):
            if not visited[node]:
                if not self.bfs(node,graph,visited):
                    return 0
                
        return 1 
