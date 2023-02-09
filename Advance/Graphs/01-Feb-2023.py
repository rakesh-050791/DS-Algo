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
