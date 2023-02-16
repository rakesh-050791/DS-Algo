# 1 : Path in Directed Graph

# Given an directed graph having A nodes labelled from 1 to A containing M edges given by matrix B of size M x 2such that there is a edge directed from node

# B[i][0] to node B[i][1].

# Find whether a path exists from node 1 to node A.

# Return 1 if path exists else return 0.

# NOTE:

# There are no self-loops in the graph.
# There are no multiple edges between two nodes.
# The graph may or may not be connected.
# Nodes are numbered from 1 to A.
# Your solution will run on multiple test cases. If you are using global variables make sure to clear them.


# Problem Constraints
# 2 <= A <= 105

# 1 <= M <= min(200000,A*(A-1))

# 1 <= B[i][0], B[i][1] <= A



# Input Format
# The first argument given is an integer A representing the number of nodes in the graph.

# The second argument given a matrix B of size M x 2 which represents the M edges such that there is a edge directed from node B[i][0] to node B[i][1].

# Output Format
# Return 1 if path exists between node 1 to node A else return 0.



# Example Input
# Input 1:
#  A = 5
#  B = [  [1, 2] 
#         [4, 1] 
#         [2, 4] 
#         [3, 4] 
#         [5, 2] 
#         [1, 3] ]
# Input 2:
#  A = 5
#  B = [  [1, 2]
#         [2, 3] 
#         [3, 4] 
#         [4, 5] ]


# Example Output
# Output 1: 0
# Output 2: 1


# Example Explanation
# Explanation 1:

#  The given doens't contain any path from node 1 to node 5 so we will return 0.
# Explanation 2:

#  Path from node1 to node 5 is ( 1 -> 2 -> 3 -> 4 -> 5 ) so we will return 1.


from collections import deque
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        adj_list  = [[] for _ in range(A+1)]
        T = len(B)

        for cur in range(T):
            row = B[cur][0]
            val = B[cur][1]
            adj_list[row].append(val)


        visited_list = [False] * (A+1)
        q = deque()
        q.append(1)

        while q:
            for i in range(len(q)):
                cur_node = q.popleft()
                nodes =  len(adj_list[cur_node])
                for child in range(nodes):
                    if not visited_list[adj_list[cur_node][child]]:
                        q.append(adj_list[cur_node][child])
                        visited_list[adj_list[cur_node][child]] =  True
                    
                    
        if visited_list[A]:
            return 1
        return 0


# 2 : Cycle in Directed Graph

# Given an directed graph having A nodes. A matrix B of size M x 2 is given which represents the M edges such that there is a edge directed from node B[i][0] to node B[i][1].

# Find whether the graph contains a cycle or not, return 1 if cycle is present else return 0.

# NOTE:

# The cycle must contain atleast two nodes.
# There are no self-loops in the graph.
# There are no multiple edges between two nodes.
# The graph may or may not be connected.
# Nodes are numbered from 1 to A.
# Your solution will run on multiple test cases. If you are using global variables make sure to clear them.


# Problem Constraints
# 2 <= A <= 105

# 1 <= M <= min(200000,A*(A-1))

# 1 <= B[i][0], B[i][1] <= A



# Input Format
# The first argument given is an integer A representing the number of nodes in the graph.

# The second argument given a matrix B of size M x 2 which represents the M edges such that there is a edge directed from node B[i][0] to node B[i][1].



# Output Format
# Return 1 if cycle is present else return 0.



# Example Input
# Input 1:

#  A = 5
#  B = [  [1, 2] 
#         [4, 1] 
#         [2, 4] 
#         [3, 4] 
#         [5, 2] 
#         [1, 3] ]
# Input 2:

#  A = 5
#  B = [  [1, 2]
#         [2, 3] 
#         [3, 4] 
#         [4, 5] ]


# Example Output
# Output 1:

#  1
# Output 2:

#  0


# Example Explanation
# Explanation 1:

#  The given graph contain cycle 1 -> 3 -> 4 -> 1 or the cycle 1 -> 2 -> 4 -> 1
# Explanation 2:

#  The given graph doesn't contain any cycle.

import sys 
sys.setrecursionlimit(10**6)
class Solution:
    def dfs(self,node,visited,Path_visited,adj):
        if not node:
            return 

        visited[node]      = True 
        Path_visited[node] = True


        for child in adj[node]:
            if not visited[child]:
                if self.dfs(child,visited,Path_visited,adj):
                    return True 
            else:
                if visited[child] and Path_visited[child]:  #path is already visited  from different path 
                    return True 


        Path_visited[node] = False     # while coming back to root , make it unvisited -> indicates visited from cur run 

        return False

    def solve(self, N, B):
        visited = [False] * (N+1)
        Path_visited = [False] * (N+1)       # we are using this path array to indicate in current run these nodes - visited 
        adj     = [[] for _ in range(N+1)]
        for i in range(len(B)):
            u = B[i][0]
            v = B[i][1]
            adj[u].append(v)


        for node in range(1,N+1):
            if not visited[node]:
                if self.dfs(node,visited,Path_visited,adj):
                    return 1 

        return 0

# 3 : Shortest Distance in a Maze
# Given a matrix of integers A of size N x M describing a maze. The maze consists of empty locations and walls.

# 1 represents a wall in a matrix and 0 represents an empty location in a wall.

# There is a ball trapped in a maze. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall (maze boundary is also considered as a wall). When the ball stops, it could choose the next direction.

# Given two array of integers of size B and C of size 2 denoting the starting and destination position of the ball.

# Find the shortest distance for the ball to stop at the destination. The distance is defined by the number of empty spaces traveled by the ball from the starting position (excluded) to the destination (included). If the ball cannot stop at the destination, return -1.



# Problem Constraints
# 2 <= N, M <= 100

# 0 <= A[i] <= 1

# 0 <= B[i][0], C[i][0] < N

# 0 <= B[i][1], C[i][1] < M



# Input Format
# The first argument given is the integer matrix A.

# The second argument given is an array of integer B.

# The third argument if an array of integer C.



# Output Format
# Return a single integer, the minimum distance required to reach destination



# Example Input
# Input 1:

# A = [ [0, 0], [0, 0] ]
# B = [0, 0]
# C = [0, 1]
# Input 2:

# A = [ [0, 0], [0, 1] ]
# B = [0, 0]
# C = [0, 1]


# Example Output
# Output 1:

#  1
# Output 2:

#  1


# Example Explanation
# Explanation 1:

#  Go directly from start to destination in distance 1.
# Explanation 2:

#  Go directly from start to destination in distance 1.


import heapq as hq 
class Solution:
    # @param A : list of list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, grid, source, destination):
        N , M = len(grid) , len(grid[0])
        
        min_heap = []
        hq.heappush(min_heap,(0,source[0],source[1]))                   # (Distance,Src,Node)
        visited        = [[False] * M for _ in range(N)]
        
        directions     = [[0,1],[1,0],[0,-1],[-1,0]]

        while min_heap:
            distance , cr , cc    =  hq.heappop(min_heap)

            if cr == destination[0] and cc == destination[1]:
                return distance

            if visited[cr][cc]: 
                continue

            visited[cr][cc] = True 

            org_cr  = cr
            org_cc  = cc
            org_dis = distance
            for i , j in directions:
                cr =  org_cr
                cc =  org_cc
                cd =  org_dis
                # move cur_point to all dirtns untl hits wall
                while cr + i >= 0 and cr + i < N and cc + j >= 0 and cc + j < M and grid[cr+i][cc+j] == 0: 
                    cr += i          
                    cc += j
                    cd += 1 
                
                hq.heappush(min_heap,(cd,cr,cc))
                
        return -1
 
# 4 : Number of islands
# Given a matrix of integers A of size N x M consisting of 0 and 1. A group of connected 1's forms an island. From a cell (i, j) such that A[i][j] = 1 you can visit any cell that shares a corner with (i, j) and value in that cell is 1.

# More formally, from any cell (i, j) if A[i][j] = 1 you can visit:

# (i-1, j) if (i-1, j) is inside the matrix and A[i-1][j] = 1.
# (i, j-1) if (i, j-1) is inside the matrix and A[i][j-1] = 1.
# (i+1, j) if (i+1, j) is inside the matrix and A[i+1][j] = 1.
# (i, j+1) if (i, j+1) is inside the matrix and A[i][j+1] = 1.
# (i-1, j-1) if (i-1, j-1) is inside the matrix and A[i-1][j-1] = 1.
# (i+1, j+1) if (i+1, j+1) is inside the matrix and A[i+1][j+1] = 1.
# (i-1, j+1) if (i-1, j+1) is inside the matrix and A[i-1][j+1] = 1.
# (i+1, j-1) if (i+1, j-1) is inside the matrix and A[i+1][j-1] = 1.
# Return the number of islands.

# NOTE: Rows are numbered from top to bottom and columns are numbered from left to right.



# Problem Constraints
# 1 <= N, M <= 100

# 0 <= A[i] <= 1



# Input Format
# The only argument given is the integer matrix A.



# Output Format
# Return the number of islands.



# Example Input
# Input 1:

#  A = [ 
#        [0, 1, 0]
#        [0, 0, 1]
#        [1, 0, 0]
#      ]
# Input 2:

#  A = [   
#        [1, 1, 0, 0, 0]
#        [0, 1, 0, 0, 0]
#        [1, 0, 0, 1, 1]
#        [0, 0, 0, 0, 0]
#        [1, 0, 1, 0, 1]    
#      ]


# Example Output
# Output 1:

#  2
# Output 2:

#  5


# Example Explanation
# Explanation 1:

#  The 1's at position A[0][1] and A[1][2] forms one island.
#  Other is formed by A[2][0].
# Explanation 2:

#  There 5 island in total.

import sys 
sys.setrecursionlimit(10**6)

class Solution:
    def backtracking(self,i,j,mat,N,M):
        if i < 0 or i >= N or j < 0 or j >= M:
            return 
        
        if mat[i][j] == 0:
            return 
        
        if mat[i][j] == 1:
            mat[i][j] = 0              # make it visited 
            
            # go top 
            self.backtracking(i-1,j,mat,N,M)
            # go left
            self.backtracking(i,j-1,mat,N,M)
            # go down
            self.backtracking(i+1,j,mat,N,M)
            # go right
            self.backtracking(i,j+1,mat,N,M)



            self.backtracking(i-1, j-1,mat,N,M)
            self.backtracking(i+1, j+1,mat,N,M)
            self.backtracking(i-1, j+1,mat,N,M)
            self.backtracking(i+1, j-1,mat,N,M)


        
    
    def solve(self,grid):
        N , M = len(grid) , len(grid[0])
        
        islands = 0
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    self.backtracking(i,j,grid,N,M)
                    islands += 1
        return islands


# 5 : Clone Graph

# Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.

# Note: The test cases are generated in the following format (use the following format to use See Expected Output option):
# First integer N is the number of nodes.
# Then, N intgers follow denoting the label (or hash) of the N nodes.
# Then, N2 integers following denoting the adjacency matrix of a graph, where Adj[i][j] = 1 denotes presence of an undirected edge between the ith and jth node, O otherwise.



# Problem Constraints
# 1 <= Number of nodes <= 105



# Input Format
# First and only argument is a node A denoting the root of the undirected graph.



# Output Format
# Return the node denoting the root of the new clone graph.



# Example Input
# Input 1:

#       1
#     / | \
#    3  2  4
#         / \
#        5   6
# Input 2:

#       1
#      / \
#     3   4
#    /   /|\
#   2   5 7 6


# Example Output
# Output 1:

#  Output will the same graph but with new pointers:
#       1
#     / | \
#    3  2  4
#         / \
#        5   6
# Output 2:

#       1
#      / \
#     3   4
#    /   /|\
#   2   5 7 6


# Example Explanation
# Explanation 1:

#  We need to return the same graph, but the pointers to the node should be different.

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
from collections import deque , defaultdict
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node: return node
        
        q = deque()
        q.append(node)
        
        clones = {node.label: UndirectedGraphNode(node.label)}
        
        while q:
            cur_node   = q.popleft()
            cur_clone  = clones[cur_node.label]
            
            for child  in cur_node.neighbors:
                cur_child = child.label
                
                if cur_child not in clones:
                    clones[cur_child] = UndirectedGraphNode(cur_child)
                    q.append(child)
                    
                cur_clone.neighbors.append(clones[cur_child])
                    
        return clones[node.label]  
        

