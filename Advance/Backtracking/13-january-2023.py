# 1 :  NQueens

# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

# Given an integer A, return all distinct solutions to the n-queens puzzle.

# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively. The final list should be generated in such a way that the indices of the queens in each list should be in reverse lexicographical order.

# Problem Constraints
# 1 <= A <= 10



# Input Format
# First argument is an integer n denoting the size of chessboard



# Output Format
# Return an array consisting of all distinct solutions in which each element is a 2d char array representing a unique solution.



# Example Input
# Input 1:

# A = 4
# Input 2:

# A = 1


# Example Output
# Output 1:

# [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],

#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# Output 1:

# [
#  [Q]
# ]


# Example Explanation
# Explanation 1:

# There exist only two distinct solutions to the 4-queens puzzle:
# Explanation 1:

# There exist only one distinct 

class Solution:
    # @param A : integer
    # @return a list of list of strings
    def solveNQueens(self, A):

        if A==1:
            return ["Q"]

        size_of_matrix = A
        # creating a matrix of size A with values 0.
        array = []
        for i in range(size_of_matrix):
            sol = [0]*size_of_matrix
            array.append(sol)
       
        n = len(array)
        # for storing the solution.
        ans = []
       
        def valid(arr,row,col):
            #iterate on above columns
            for i in range(row):
                if arr[i][col] == 1:
                    return False
           
            # checking on left diagonal
            i = row-1
            j = col-1
            while i>=0 and j>=0:
                if arr[i][j]==1:
                    return False
                i-=1
                j-=1
           
            # checking on right diagonal
            i = row-1
            j = col+1
            while i>=0 and j<len(arr):
                if arr[i][j]==1:
                    return False
                i-=1
                j+=1
           
            # returning True if there is no queen in either of the above checked direction.
            return True

        def add_solution(arr):
            curr_list = []
            for row in range(len(arr)):
                # storing row values in a string.
                # if store in a list. your submission will fail.
                stt=""
                for col in range(len(arr)):
                    val = arr[row][col]
                    if val == 0:
                        stt+="."
                    else:
                        stt+="Q"
                curr_list.append(stt)
            ans.append(curr_list)
            return

        def NQueens(arr,length,curr_pos):
            # if curren position is equal to length of the 2D list
            # it means you covered entire 2D list, now add the list to the ans list
            if curr_pos == length:
                add_solution(arr)
                return
           
            # At ith row choice
            for col in range(0,length):
               
                # we want to place queen at ith row and jth column
                # we can only place queen in 2Dlist such that queen doesn't kill each other
                # for that we will use validating function.
                if valid(arr,curr_pos,col):

                    arr[curr_pos][col] = 1

                    NQueens(arr,length,curr_pos+1)
                   
                    arr[curr_pos][col] = 0
           
            return

        NQueens(array,n,0)

        return ans



# 2 : Word Break

# Given a string A and a dictionary of words B, determine if A can be segmented into a space-separated sequence of one or more dictionary words.

# Input Format:

# The first argument is a string, A.
# The second argument is an array of strings, B.
# Output Format:

# Return 0 / 1 ( 0 for false, 1 for true ) for this problem.
# Constraints:

# 1 <= len(A) <= 6500
# 1 <= len(B) <= 10000
# 1 <= len(B[i]) <= 20
# Examples:

# Input 1:
#     A = "myinterviewtrainer",
#     B = ["trainer", "my", "interview"]

# Output 1:
#     1

# Explanation 1:
#     Return 1 ( corresponding to true ) because "myinterviewtrainer" can be segmented as "my interview trainer".

# Input 2:
#     A = "a"
#     B = ["aaa"]

# Output 2:
#     0

# Explanation 2:
#     Return 0 ( corresponding to false ) because "a" cannot be segmented as "aaa".


class Solution:
    # @param A : string
    # @param B : list of strings
    # @return an integer
    def wordBreak(self, A, B):
        dp = [0] * (len(A) + 1)
        dp[len(A)] = 1
        for i in range(len(A)-1, -1, -1):
            for w in B:
                if (i + len(w)) <= len(A) and A[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]


# 3 : Sudoku
# Write a program to solve a Sudoku puzzle by filling the empty cells. Empty cells are indicated by the character '.' You may assume that there will be only one unique solution.



# A sudoku puzzle,



# and its solution numbers marked in red.



# Problem Constraints
# N = 9


# Input Format
# First argument is an array of array of characters representing the Sudoku puzzle.


# Output Format
# Modify the given input to the required answer.


# Example Input
# Input 1:

# A = [[53..7....], [6..195...], [.98....6.], [8...6...3], [4..8.3..1], [7...2...6], [.6....28.], [...419..5], [....8..79]]


# Example Output
# Output 1:

# [[534678912], [672195348], [198342567], [859761423], [426853791], [713924856], [961537284], [287419635], [345286179]]


# Example Explanation
# Explanation 1:

# Look at the diagrams given in the question.

from collections import defaultdict
class Solution:
    # @param A : list of list of chars
    def insertinMaps(self,value,row,col,rowMap,colMap,sqrMap):
        rowMap[row].add(value)
        colMap[col].add(value)
        sqrMap[(row//3,col//3)].add(value)

    def removeinMaps(self,value,row,col,rowMap,colMap,sqrMap,indx):
        rowMap[row].remove(value)
        colMap[col].remove(value)
        sqrMap[(row//3,col//3)].remove(value)

    def verifyMaps(self,value,row,col,rowMap,colMap,sqrMap):
        if value in colMap[col] or value in rowMap[row] or value in sqrMap[(row//3,col//3)]:
            return False
        return True

    def solveSudoku(self, A):
        rows , cols = 9 , 9
        rowMap = defaultdict(set)
        colMap = defaultdict(set)
        sqrMap = defaultdict(set)   # (row//3 , col// 3) 
        
        ans_mat = []
        
        # inserting initial cells in map
        for ii in range(9):
            for jj in range(9):
                if  A[ii][jj] != '.':
                    self.insertinMaps(int(A[ii][jj]),ii,jj,rowMap,colMap,sqrMap) 
                    
        def Sudoku(indx,mat):
            if indx == 81:
                temp_mat = mat.copy()
                ans_mat  = temp_mat
                return True
            
            row = indx // 9           # row indx in matrix
            col = indx % 9            # col indx in matrix
            
            # already filled 
            if mat[row][col] != '.':
                return Sudoku(indx+1,mat)
            else:
                # not filled try all possible numbers
                for cell in range(1,10):
                    if self.verifyMaps(cell,row,col,rowMap,colMap,sqrMap):        # verify cell can be placed
                        self.insertinMaps(cell,row,col,rowMap,colMap,sqrMap)      # if so then add newval in maps
                        mat[row][col] = str(cell)
                        if Sudoku(indx+1,mat):                                    # since we filled call next cell
                            return True
                        
                        # if last call not working undo and backtrack
                        mat[row][col] = '.'
                        self.removeinMaps(cell,row,col,rowMap,colMap,sqrMap,indx)
                        
                return False
            
        Sudoku(0,A)
        return ans_mat


# 4 : Combination Sum
# Given an array of candidate numbers A and a target number B, find all unique combinations in A where the candidate numbers sums to B.

# The same repeated number may be chosen from A unlimited number of times.

# Note:

# 1) All numbers (including target) will be positive integers.

# 2) Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).

# 3) The combinations themselves must be sorted in ascending order.

# 4) CombinationA > CombinationB iff (a1 > b1) OR (a1 = b1 AND a2 > b2) OR ... (a1 = b1 AND a2 = b2 AND ... ai = bi AND ai+1 > bi+1)

# 5) The solution set must not contain duplicate combinations.



# Problem Constraints
# 1 <= |A| <= 20

# 1 <= A[i] <= 50

# 1 <= B <= 500



# Input Format
# The first argument is an integer array A.

# The second argument is integer B.



# Output Format
# Return a vector of all combinations that sum up to B.



# Example Input
# Input 1:

# A = [2, 3]
# B = 2
# Input 2:

# A = [2, 3, 6, 7]
# B = 7


# Example Output
# Output 1:

# [ [2] ]
# Output 2:

# [ [2, 2, 3] , [7] ]


# Example Explanation
# Explanation 1:

# All possible combinations are listed.
# Explanation 2:

# All possible combinations are listed.

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def dfs(self, A, pos, cur, total, B, res):
        if total == B:
            if cur not in res:
                res.append(cur.copy())
            return

        if pos == len(A) or total > B: return

        # including the current element
        cur.append(A[pos])
        self.dfs(A, pos, cur, total + A[pos], B, res)

        # popping the current element
        cur.pop()
        self.dfs(A, pos + 1, cur, total, B, res)

    def combinationSum(self, A, B):
        res = []
        A.sort()

        self.dfs(A, 0, [], 0, B, res)
        # res.sort()

        return res

        # TC: O(2^B); SC: O(B)
