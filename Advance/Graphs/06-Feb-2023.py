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


# 4 : Gym Trainer

# You are the trainer of a gym and there are A people who come to your gym.

# Some of them are friends because they walk together, and some of them are friends because they talk together.
# But people become possessive about each other, so a person cannot walk with one friend and talk with another. Although he can walk with two or more people or talk with two or more people.

# You being the trainer, decided to suggest each one of the 2 possible diets. But friends, being friends will always have the same diet as all the other friends are having.

# Find and return the number of ways you can suggest each of them a diet.

# As the number of ways can be huge, return the answer modulo 109+7.

# NOTE: If there is any person who walks with one person and talks with the another person, then you may return 0.



# Problem Constraints

# 1 <= A, N, M <= 105

# 1 <= B[i][0], B[i][1], C[i][0], C[i][1] <= A



# Input Format

# The first argument contains an integer A, representing the number of people.
# The second argument contains a 2-D integer array B of size N x 2, where B[i][0] and B[i][1] are friends because they walk together.
# The third argument contains a 2-D integer array C of size M x 2, where C[i][0] and C[i][1] are friends because they talk together.



# Output Format

# Return an integer representing the number of ways to suggest one of the two diets to the people.



# Example Input

# Input 1:

#  A = 4
#  B = [
#        [1, 2]
#      ]
#  C = [
#        [3, 4]
#      ]
# Input 2:

#  A = 3
#  B = [
#        [1, 2]
#      ]
#  C = [
#        [1, 3] 
#      ]


# Example Output

# Output 1:

#  4
# Output 2:

#  0


# Example Explanation

# Explanation 1:

#  There are four ways to suggest the diet:
#  Diet-1 to (1, 2) and Diet-2 to (3, 4).
#  Diet-1 to (1, 2) and Diet-1 to (3, 4).
#  Diet-2 to (1, 2) and Diet-1 to (3, 4).
#  Diet-2 to (1, 2) and Diet-2 to (3, 4).
 
# Explanation 2:

#  Person 1 walks with person 2 and talks with person 3. So, we will return 0.

class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @param C : list of list of integers
    # @return an integer
    def solve(self, A, B, C):
        mod = (10**9)+7
        res = 1
        ans = A
        WT = [ '' for _ in range(A+1) ]
        rank = [0 for _ in range(A+1) ]
        parent = [ i for i in range(A+1) ]

        for i in range(len(B)):
            WT[B[i][0]] = 'W'
            WT[B[i][1]] = 'W'

        for i in range(len(C)):
            if ( WT[C[i][0]] == 'W' or WT[C[i][1]] == 'W'):
                return 0


        def root(x):
            while( x != parent[x]):
                x = parent[x]

            return x

        def union(x,y):
            ans = A
            rx = root(x)
            ry = root(y)

            if( rx == ry ):
                return
            ans -= 1
            if rank[rx] < rank[ry]:
                parent[rx] = ry
            elif rank[rx] > rank[ry]:
                parent[ry] = rx
            else:
                parent[ry] = rx
                rank[rx] += 1


        for i in range(len(B)):
            union(B[i][0],B[i][1])
        for i in range(len(C)):
            union( C[i][0] , C[i][1])    
        for i in range(1,A+1):
            parent[i] = root(i)
        #print(set(parent))
        tmp = len(set(parent))-1
        return pow(2,tmp) % mod


# 5 :  Maximum Depth
# Given a Tree of A nodes having A-1 edges. Each node is numbered from 1 to A where 1 is the root of the tree.

# You are given Q queries. In each query, you will be given two integers L and X. Find the value of such node which lies at level L mod (MaxDepth + 1) and has value greater than or equal to X.

# Answer to the query is the smallest possible value or -1, if all the values at the required level are smaller than X.

# NOTE:

# Level and Depth of the root is considered as 0.
# It is guaranteed that each edge will be connecting exactly two different nodes of the tree.
# Please read the input format for more clarification.


# Problem Constraints

# 2 <= A, Q(size of array E and F) <= 105

# 1 <= B[i], C[i] <= A

# 1 <= D[i], E[i], F[i] <= 106



# Input Format

# The first argument is an integer A denoting the number of nodes.

# The second and third arguments are the integer arrays B and C where for each i (0 <= i < A-1), B[i] and C[i] are the nodes connected by an edge.

# The fourth argument is an integer array D, where D[i] denotes the value of the (i+1)th node

# The fifth and sixth arguments are the integer arrays E and F where for each i (0 <= i < Q), E[i] denotes L and F[i] denotes X for ith query.



# Output Format

# Return an array of integers where the ith element denotes the answer to ith query.



# Example Input

# Input 1:

#  A = 5
#  B = [1, 4, 3, 1]
#  C = [5, 2, 4, 4]
#  D = [7, 38, 27, 37, 1]
#  E = [1, 1, 2]
#  F = [32, 18, 26]
# Input 2:

#  A = 3
#  B = [1, 2]
#  C = [3, 1]
#  D = [7, 15, 27]
#  E = [1, 10, 1]
#  F = [29, 6, 26]


# Example Output

# Output 1:

#  [37, 37, 27]
# Output 2:

#  [-1, 7, 27]


# Example Explanation

# Explanation 1:

#       1[7]
#      /    \
#    5[1]  4[37]
#         /    \
#        2[38]  3[27]

#  Query 1: 
#     L = 1, X = 32
#     Nodes for level 1 are 5, 4
#     Value of Node 5 = 1 < 32
#     Value of Node 4 = 37 >= 32
#     Ans = 37
# Explanation 2:

#       1[7]
#      /    \
#    2[15]  3[27]

#  Query 1: 
#     L = 1, X = 6
#     Nodes for level 1 are 2, 3 having value 15 and 27 respectively.
#     Answer = -1 (Since no node is greater or equal to 29).
#  Query 1: 
#     L = 10 % 2 = 0, X = 6
#     Nodes for level 0 is 1 having value 7.
#     Answer = 7. 

import bisect

class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of integers
    # @param D : list of integers
    # @param E : list of integers
    # @param F : list of integers
    # @return a list of integers
    def __init__(self) -> None:
        self.max_depth = 0

    def dfs(self, u, parent, lvl, dist, adj, vals):
        self.max_depth = max(self.max_depth, dist)
        lvl[dist].append(vals[u])
        for nex in adj[u]:
            if nex == parent:
                continue
            self.dfs(nex, u, lvl, dist + 1, adj, vals)

    def solve(self, A, B, C, D, E, F):
        # create adjancency list
        adj = [[] for _ in range(A+1)]
        vals = [0] * (A + 1)        
        for i in range(len(B)):
            node, edge = B[i], C[i]
            adj[node].append(edge)
            adj[edge].append(node)
        levels = [[] for _ in range(A+1)]
        for i in range(A):
            vals[i + 1] = D[i]
        self.dfs(1, 1, levels, 0, adj, vals)
       
        for i in range(self.max_depth+1):
            levels[i].sort()        
        res = []
        for i in range(len(E)):
            l, x = E[i], F[i]
            l %= (self.max_depth + 1)
            lb_idx = bisect.bisect_left(levels[l], x) # returns idx of lb
            if lb_idx == len(levels[l]):
                res.append(-1)
            else:
                res.append(levels[l][lb_idx])
        return res

# 6 : Cows and snacks

# The legendary Farmer John is throwing a huge party, and animals from all over the world are hanging out at his house. His guests are hungry, so he instructs his cow Bessie to bring out the snacks! Moo!

# There are A snacks flavors, numbered with integers 1,2,…,A. Bessie has A snacks, one snack of each flavor. There are M guests and every guest has exactly two favorite flavors. The procedure for eating snacks will go as follows:

# First, Bessie will line up the guests in some way.
# Each guest in their turn will eat all remaining snacks of their favorite flavor. In case no favorite flavors are present when a guest goes up, they become very sad.
# Help Bessie to minimize the number of sad guests by lining the guests in an optimal way.



# Problem Constraints

# 2 <= A <= 100000
# 1 <= M <= 100000
# 1 <= B[i][0] , B[i][1] <= A
# B[i][0] != B[i][1]



# Input Format

# First argument of input contains a single integer A.
# Second argument of input contains a M x 2 integer matrix B denoting favorite flavors of each guest.



# Output Format

# Return a single integer denoting the ,minimum possible number of sad guests.



# Example Input

# Input 1:

#  A = 5
#  B = [ 
#        [1, 2],
#        [4, 3],
#        [1, 4],
#        [3, 4]
#      ]
# Input 2:

#  A = 6
#  B = [
#        [2, 3],
#        [2, 1],
#        [3, 4],
#        [6, 5],
#        [4, 5]
#      ]


# Example Output

# Output 1:

#  1
# Output 2:

#  0


# Example Explanation

# Explanation 1:

#  Bessie can order the guests like this: (3, 1, 2, 4). Guest 3 goes first and eats snacks 1 and 4. 
#  Then the guest 1 goes and eats the snack 2 only, because the snack 1 has already been eaten.
#  Similarly, the guest 2 goes up and eats the snack 3 only. All the snacks are gone, so the guest 4 will be sad.
# Explanation 2:

#  Bessie can order the guests like this: (1, 2, 3, 5, 4). So no-one will be sad.

class Solution:
    def search(self, val , dp) :
        while(val != dp[val]):
            dp[val] = dp[dp[val]]
            val = dp[val]
        return val

    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        dp = [0] * 100001
        ans = 0
        for i in range(A + 1):
            dp[i] = i
       
        for i in B:
            x = self.search(i[0],dp)
            y = self.search(i[1],dp)
            if x == y:
                ans += 1
            else:
                dp[x] = y
        return ans


