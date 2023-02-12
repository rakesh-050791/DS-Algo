# 1 :  Topological Sort

# Given an directed acyclic graph having A nodes. A matrix B of size M x 2 is given which represents the M edges such that there is a edge directed from node B[i][0] to node B[i][1].

# Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge uv, vertex u comes before v in the ordering. Topological Sorting for a graph is not possible if the graph is not a DAG.

# Return the topological ordering of the graph and if it doesn't exist then return an empty array.

# If there is a solution return the correct ordering. If there are multiple solutions print the lexographically smallest one.

# Ordering (a, b, c) is said to be lexographically smaller than ordering (e, f, g) if a < e or if(a==e) then b < f and so on.

# NOTE:

# There are no self-loops in the graph.
# There are no multiple edges between two nodes.
# The graph may or may not be connected.
# Nodes are numbered from 1 to A.
# Your solution will run on multiple test cases. If you are using global variables make sure to clear them.


# Problem Constraints
# 2 <= A <= 104

# 1 <= M <= min(100000,A*(A-1))

# 1 <= B[i][0], B[i][1] <= A

# Input Format
# The first argument given is an integer A representing the number of nodes in the graph.

# The second argument given a matrix B of size M x 2 which represents the M edges such that there is a edge directed from node B[i][0] to node B[i][1].



# Output Format
# Return a one-dimensional array denoting the topological ordering of the graph and it it doesn't exist then return empty array.



# Example Input
# Input 1:

#  A = 6
#  B = [  [6, 3] 
#         [6, 1] 
#         [5, 1] 
#         [5, 2] 
#         [3, 4] 
#         [4, 2] ]
# Input 2:

#  A = 3
#  B = [  [1, 2]
#         [2, 3] 
#         [3, 1] ]


# Example Output
# Output 1:

#  [5, 6, 1, 3, 4, 2]
# Output 2:

#  []


# Example Explanation
# Explanation 1:

#  The given graph contain no cycle so topological ordering exists which is [5, 6, 1, 3, 4, 2]
# Explanation 2:

#  The given graph contain cycle so topological ordering not possible we will return empty array.

class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        from queue import  PriorityQueue 
        #create min heap/priority queue
        pq=PriorityQueue()
        
        g=[[] for i in range(A+1)]
        ans=[]
        ind=[0 for i in range(A+1)]
        #generate adjacency list of DAG
        for i in B:
            u=i[0]
            v=i[1]
            g[u].append(v)
            ind[v]+=1
        
        # if in-degree is zero put them in priority queue(these are the source nodes)
        for i in range(1,A+1):
            if ind[i]==0:
                pq.put(i)
        
        while not (pq.empty()) > 0:
            #get the top element from priority queue and insert to ans
            front=pq.get()
            ans.append(front)
            #for each of the front node, do a BFS
            for i in range(len(g[front])):
                u=g[front][i]
                ind[u]-=1
                if ind[u]==0:
                    pq.put(u)
        return ans


# 2 : Possibility of Finishing

# There are a total of A courses you have to take, labeled from 1 to A.

# Some courses may have prerequisites, for example to take course 2 you have to first take course 1, which is expressed as a pair: [1,2].

# So you are given two integer array B and C of same size where for each i (B[i], C[i]) denotes a pair.

# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

# Return 1 if it is possible to finish all the courses, or 0 if it is not possible to finish all the courses.



# Problem Constraints
# 1 <= A <= 6*104

# 1 <= length(B) = length(C) <= 105

# 1 <= B[i], C[i] <= A



# Input Format
# The first argument of input contains an integer A, representing the number of courses.

# The second argument of input contains an integer array, B.

# The third argument of input contains an integer array, C.



# Output Format
# Return 1 if it is possible to finish all the courses, or 0 if it is not possible to finish all the courses.



# Example Input
# Input 1:

#  A = 3
#  B = [1, 2]
#  C = [2, 3]
# Input 2:

#  A = 2
#  B = [1, 2]
#  C = [2, 1]


# Example Output
# Output 1:

#  1
# Output 2:

#  0


# Example Explanation
# Explanation 1:

#  It is possible to complete the courses in the following order:
#     1 -> 2 -> 3
# Explanation 2:

#  It is not possible to complete all the courses.

class Solution:
	# @param A : integer
	# @param B : list of integers
	# @param C : list of integers
	# @return an integer
	def solve(self, A, B, C):
        from queue import  PriorityQueue 
        #create min heap/priority queue
        pq=PriorityQueue()
        
        g=[[] for i in range(A+1)]
        ans=[]
        ind=[0 for i in range(A+1)]
        #generate adjacency list of DAG
        for i in range(len(B)):
            u=B[i]
            v=C[i]
            g[u].append(v)
            ind[v]+=1
        
        for i in range(1,A+1):
                    if ind[i]==0:
                        pq.put(i)
        c=0        
        while not (pq.empty()) > 0:
            #get the top element from priority queue and insert to ans
            front=pq.get()
            c+=1
            #for each of the front node, do a BFS
            for i in range(len(g[front])):
                u=g[front][i]
                ind[u]-=1
                if ind[u]==0:
                    pq.put(u)
        if c!=A:
            return 0
        return 1

# 3 Batches
# A students applied for admission in IB Academy. An array of integers B is given representing the strengths of A people i.e. B[i] represents the strength of ith student.

# Among the A students some of them knew each other. A matrix C of size M x 2 is given which represents relations where ith relations depicts that C[i][0] and C[i][1] knew each other.

# All students who know each other are placed in one batch.

# Strength of a batch is equal to sum of the strength of all the students in it.

# Now the number of batches are formed are very much, it is impossible for IB to handle them. So IB set criteria for selection: All those batches having strength at least D are selected.

# Find the number of batches selected.

# NOTE: If student x and student y know each other, student y and z know each other then student x and student z will also know each other.



# Problem Constraints

# 1 <= A <= 105

# 1 <= M <= 2*105

# 1 <= B[i] <= 104

# 1 <= C[i][0], C[i][1] <= A

# 1 <= D <= 109



# Input Format

# The first argument given is an integer A.
# The second argument given is an integer array B.
# The third argument given is a matrix C.
# The fourth argument given is an integer D.



# Output Format

# Return the number of batches selected in IB.



# Example Input

# Input 1:

#  A = 7
#  B = [1, 6, 7, 2, 9, 4, 5]
#  C = [  [1, 2]
#         [2, 3] 
#        `[5, 6]
#         [5, 7]  ]
#  D = 12
# Input 2:

#  A = 5
#  B = [1, 2, 3, 4, 5]
#  C = [  [1, 5]
#         [2, 3]  ]
#  D = 6


# Example Output

# Output 1:

#  2
# Output 2:

#  1


# Example Explanation

# Explanation 1:

#  Initial Batches :
#     Batch 1 = {1, 2, 3} Batch Strength = 1 + 6 + 7 = 14
#     Batch 2 = {4} Batch Strength = 2
#     Batch 3 = {5, 6, 7} Batch Strength = 9 + 4 + 5 = 18
#     Selected Batches are Batch 1 and Batch 2.
# Explanation 2:

#  Initial Batches :
#     Batch 1 = {1, 5} Batch Strength = 1 + 5  = 6
#     Batch 2 = {2, 3} Batch Strength = 5
#     Batch 3 = {4} Batch Strength = 4  
#     Selected Batch is only Batch 1.

import sys 
sys.setrecursionlimit(10**6)
class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of list of integers
    # @param D : integer
    # @return an integer
    def dfs(self,node,visited,adj,strengths):
        visited[node] = True

        total_sum = 0
        total_sum += strengths[node -1]

        for child in adj[node]:
            if not visited[child]:
                total_sum += self.dfs(child,visited,adj,strengths)
                visited[child] = True 
                
        return total_sum
        


    def solve(self, N, Strengths ,Edges, K):
        visited = [False] * (N+1)
        adj     = [[] for _ in range(N+1)]

        for u , v in Edges:
            adj[u].append(v)
            adj[v].append(u)

        
        total_batches = 0
        # graph traversal
        for node in range(1,N+1):
            if not visited[node]:
                batch_strength = self.dfs(node,visited,adj,Strengths)

                if batch_strength >= K:
                    total_batches += 1

        return total_batches
