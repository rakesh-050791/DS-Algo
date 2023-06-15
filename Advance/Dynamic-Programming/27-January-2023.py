# 1 : Russian Doll envelopes

# Given a matrix of integers A of size N x 2 describing dimensions of N envelopes, where A[i][0] denotes the height of the ith envelope and A[i][1] denotes the width of the ith envelope.

# One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

# Find the maximum number of envelopes you can put one inside other.



# Problem Constraints
# 1 <= N <= 1000
# 1 <= A[i][0], A[i][1] <= 109



# Input Format
# The only argument given is the integer matrix A.



# Output Format
# Return an integer denoting the maximum number of envelopes you can put one inside other.



# Example Input
# Input 1:

#  A = [ 
#          [5, 4]
#          [6, 4]
#          [6, 7]
#          [2, 3]  
#      ]
# Input 2:

#  A = [     '
#          [8, 9]
#          [8, 18]    
#      ]


# Example Output
# Output 1:

#  3
# Output 2:

#  1


# Example Explanation
# Explanation 1:

#  Step 1: put [2, 3] inside [5, 4]
#  Step 2: put [5, 4] inside [6, 7]
#  3 envelopes can be put one inside other.
# Explanation 2:

#  No envelopes can be put inside any other so answer is 1.

import sys
sys.setrecursionlimit(10**6)

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        A.sort(key=lambda item: (item[0], -item[1]))
        N = len(A)
        
        dp = [[-1]*(N+1) for _ in range(N+1)]
        
        def LIS(indx,prev_indx):
            if indx >= N:
                return 0
            
            if dp[indx][prev_indx] != -1:
                return dp[indx][prev_indx]
            
            # dont_take 
            
            dont_take = LIS(indx+1, prev_indx)
            take_it   = -1
            
            
            # to take the element cur_ele should be greater than prev element
            cur_w , cur_h = A[indx][0] , A[indx][1]
            pre_w , pre_h = A[prev_indx][0] , A[prev_indx][1]
            
            if prev_indx == -1 or (cur_w > pre_w and cur_h > pre_h):
                take_it =  1 + LIS(indx+1,indx)
                
            dp[indx][prev_indx] = max(dont_take,take_it)
            
            return  dp[indx][prev_indx]
        
        
        return LIS(0,-1)


# 2 : Longest Increasing Subsequence

# Find the longest increasing subsequence of a given array of integers, A.

# In other words, find a subsequence of array in which the subsequence's elements are in strictly increasing order, and in which the subsequence is as long as possible.

# In this case, return the length of the longest increasing subsequence.



# Problem Constraints
# 1 <= length(A) <= 2500
# 0 <= A[i] <= 2500



# Input Format
# The first and the only argument is an integer array A.



# Output Format
# Return an integer representing the length of the longest increasing subsequence.



# Example Input
# Input 1:

#  A = [1, 2, 1, 5]
# Input 2:

#  A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]


# Example Output
# Output 1:

#  3
# Output 2:

#  6


# Example Explanation
# Explanation 1:

#  The longest increasing subsequence: [1, 2, 5]
# Explanation 2:

#  The possible longest increasing subsequences: [0, 2, 6, 9, 13, 15] or [0, 4, 6, 9, 11, 15] or [0, 4, 6, 9, 13, 15]

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def lis(self, A):
        # Initialize a list rs with length equal to the length of the input array A
        rs = [1] * (len(A))
       
        # Iterate over the input array A
        for i in range(1, len(A)):
            # For each element A[i], compare it with all previous elements A[j] where j ranges from 0 to i-1
            for j in range(i):
                # If A[j] is less than A[i], update the value of rs[i]
                if A[j] < A[i]:
                    # Update the value of rs[i] as the maximum of its current value and (rs[j] + 1)
                    rs[i] = max(rs[j] + 1, rs[i])
       
        # Return the maximum value in the list rs
        return max(rs)



# 3 : Palindrome Partitioning II

# Given a string A, partition A such that every substring of the partition is a palindrome.

# Return the minimum cuts needed for a palindrome partitioning of A.



# Problem Constraints
# 1 <= length(A) <= 501



# Input Format
# The first and the only argument contains the string A.



# Output Format
# Return an integer, representing the minimum cuts needed.



# Example Input
# Input 1:

#  A = "aba"
# Input 2:

#  A = "aab"


# Example Output
# Output 1:

#  0
# Output 2:

#  1


# Example Explanation
# Explanation 1:

#  "aba" is already a palindrome, so no cuts are needed.
# Explanation 2:

#  Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.

class Solution:
    def isPalindrome(self, A):
        dp = []
        n = len(A)
        for i in range(n):
            dp.append([True] * n)
        for l in range(2, n+1): # considering window size from 2 to n(inclusive)
            for start in range(n - l + 1): # last index of start will be n-l (inclusive)
                end = start + l - 1
                dp[start][end] = A[start] == A[end] and dp[start + 1][end - 1]
        return dp

    # @param A : string
    # @return an integer
    def minCut(self, A):
        n = len(A)
        isPalindrome = self.isPalindrome(A)
        dp = [-1 for i in range(n)]
        dp[0] = 0
        for i in range(n):
            if isPalindrome[0][i]:
                dp[i] = 0
            else:
                mini = float('inf')
                for j in range(i, 0, -1):
                    if isPalindrome[j][i]: # get the min cut for all the substrings before i
                        if dp[j - 1] < mini:
                            mini = dp[j - 1]
                dp[i] = mini + 1
        return dp[n - 1]



# 4 : Longest Palindromic Subsequence
# Given a string A. Find the longest palindromic subsequence (A subsequence which does not need to be contiguous and is a palindrome).

# You need to return the length of longest palindromic subsequence.



# Problem Constraints
# 1 <= length of(A) <= 103



# Input Format
# First and only integer is a string A.



# Output Format
# Return an integer denoting the length of longest palindromic subsequence.



# Example Input
# Input 1:

#  A = "bebeeed"
# Input 2:

#  A = "aedsead"


# Example Output
# Output 1:

#  4
# Output 2:

#  5


# Example Explanation
# Explanation 1:

#  The longest palindromic subsequence is "eeee", which has a length of 4.
# Explanation 2:

#  The longest palindromic subsequence is "aedea", which has a length of 5.

 sys.setrecursionlimit(1000000)
class Solution:
    # @param A : string
    # @return an integer
    dp = []
    def solve(self, A):
        s = A
        rs = s[::-1]

        N = len(s)

        self.dp = []
        for i in range(N+1):
            self.dp.append([-1]*(N+1))

        result = self.LPS(s, rs, N-1, N-1)
        return len(result)

    def LPS(self, s, rs, N, M):

        if N < 0 or M < 0:
            return ''

        if self.dp[N][M] != -1:
            return self.dp[N][M]

        if s[N] == rs[M]:
            self.dp[N][M] = s[N] + self.LPS(s, rs, N-1, M-1)
            return self.dp[N][M]

        takes = self.LPS(s, rs, N, M-1)
        takers = self.LPS(s, rs, N-1, M)

        self.dp[N][M] = takes if len(takes) > len(takers) else takers
        return self.dp[N][M]



# 5 : Length of LIS

# You are given an array A. You need to find the length of the Longest Increasing Subsequence in the array.

# In other words, you need to find a subsequence of array A in which the elements are in sorted order, (strictly increasing) and as long as possible.



# Problem Constraints
# 1 ≤ length(A), A[i] ≤ 105



# Input Format
# The first and only argument of the input is the array A.



# Output Format
# Output a single integer, the length of the longest increasing subsequence in array A.



# Example Input
# Input 1:

# A: [2, 1, 4, 3]
# Input 2:

# A: [5, 6, 3, 7, 9]


# Example Output
# Output 1:

# 2
# Output 2:

# 4


# Example Explanation
# Explanation 1:

#  [2, 4] and [1, 3] are the longest increasing sequences of size 2. 
# Explanation 2:

# The longest increasing subsequence we can get is [5, 6, 7, 9] of size 4.



# Below solution is in C++, reference is GFG : https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/

int Solution::findLIS(vector<int> &A) {
    vector<int> temp;
    int ans=0;
    for(int a:A){
        auto it = lower_bound(temp.begin(),temp.end(),a);
        if(it == temp.end()){
            temp.push_back(a);
            ans++;
        }
        else{
            if(*it > a){
                int pos = it - temp.begin();
                temp[pos] = a;
            }
        }
    }
    return ans;
}