# 1 : Count of pairs with the given sum

# Given a sorted array of distinct integers A and an integer B, find and return how many pair of integers ( A[i], A[j] ) such that i != j have sum equal to B.

# Input 1:
#     A = [1, 2, 3, 4, 5]
#     B = 5

# Output 1: 2

class Solution:
    def solve(self, A, B):
        n = len(A)
        pairs = 0
        i = 0
        j = n-1

        while (i < j):
            if A[i] + A[j] == B: # we got a valid pair,increase pair count and move left
                pairs += 1
                j -= 1
            elif A[i] + A[j] > B: # move to left side
               j -= 1
            elif A[i] + A[j] < B: # move to right side
                i += 1
        return pairs


# 2 : Pairs with Given Difference

# Given an one-dimensional integer array A of size N and an integer B.

# Count all distinct pairs with difference equal to B.

# Here a pair is defined as an integer pair (x, y), where x and y are both numbers in the array and their absolute difference is B.

# Example Input

# Input 1:

# A = [1, 5, 3, 4, 2]
# B = 3

# Example Output
# Output 1: 2


# Example Explanation

# Explanation 1:

# There are 2 unique pairs with difference 3, the pairs are {1, 4} and {5, 2} 


# Approach 1 # TC: O(NlogN); SC: O(N^2)
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        ans = set()
        n = len(A)
        p1 = 0
        p2 = 1
        A.sort()

        while p2 < n:
            diff = A[p2] - A[p1]
            if diff == B:
                ans.add(tuple([A[p1], A[p2]]))
                p1 += 1
                p2 += 1
            elif diff > B:
                p1 += 1
                if p1 == p2:
                    p2 += 1
            else:
                p2 += 1

        return len(ans)

    
# Approach 2 # TC: O(N); SC: O(N)

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        freq = {}
        p = 0

        # hashing for arrays with unique elements
        if B != 0:
            for a in set(A):
                if a in freq:
                    freq[a] += 1
                if a not in freq:
                    freq[a] = 1
                if a + B in freq:
                    p += 1
                if a - B in freq:
                    p += 1

        # hashing for arrays with duplicates
        else:
            for a in A:
                if a in freq:
                    freq[a] += 1
                else:
                    freq[a] = 1
            for f in freq:
                if freq[f] > 1:
                    p += 1

        return p

# Final Approach 3 # TC: O(NlogN); SC: O(1) 

class Solution:
    def solve(self, A, B):

        n = len(A)
        start = 0 
        end = 1
        pairs = 0
        A.sort()

        while (end < n):
            diff = abs(A[end] - A[start])
            if diff == B:
                pairs += 1
                start += 1
                end += 1

                # handling duplicates
                while end < n and A[end] == A[end - 1]:
                    end += 1
                while start < end and start > 0 and A[start] == A[start - 1]:
                    start += 1

            elif diff < B:
                end += 1
            elif diff > B:
                start += 1
                if start == end:
                    end += 1
        return pairs

# 3 : Subarray with given sum
# Given an array of positive integers A and an integer B, find and return first continuous subarray which adds to B.

# If the answer does not exist return an array with a single element "-1".

# First sub-array means the sub-array for which starting index in minimum.



# Output Format
# Return the first continuous sub-array which adds to B and if the answer does not exist return an array with a single element "-1".



# Example Input
# Input 1:

#  A = [1, 2, 3, 4, 5]
#  B = 5


# Example Output
# Output 1: [2, 3]


# Example Explanation
# Explanation 1: [2, 3] sums up to 5.

class Solution:
    def solve(self, A, B):
        n = len(A)
        start = 0
        end = 0
        currentSum = 0
        subArray = []

        while (start < n and end < n):
            if currentSum < B:
                currentSum += A[end]
                end += 1
            
            if currentSum > B:
                currentSum -= A[start]
                start += 1
            
            if currentSum == B:
                return A[start:end]
        
        return [-1]


# 4 Container With Most Water

# Given n non-negative integers A[0], A[1], ..., A[n-1] , where each represents a point at coordinate (i, A[i]).

# N vertical lines are drawn such that the two endpoints of line i is at (i, A[i]) and (i, 0).

# Find two lines, which together with x-axis forms a container, such that the container contains the most water.

# Note: You may not slant the container.



# Problem Constraints
# 0 <= N <= 105

# 1 <= A[i] <= 105



# Input Format
# Single Argument representing a 1-D array A.



# Output Format
# Return single Integer denoting the maximum area you can obtain.



# Example Input
# Input 1:

# A = [1, 5, 4, 3]
# Input 2:

# A = [1]


# Example Output
# Output 1:

#  6
# Output 2:

#  0


# Example Explanation
# Explanation 1:

 
# 5 and 3 are distance 2 apart. So size of the base = 2. Height of container = min(5, 3) = 3. 
# So total area = 3 * 2 = 6
# Explanation 2:

 
# No container is formed.

class Solution:
    def maxArea(self, A):
        n = len(A)
        start = 0
        end = n-1

        maxArea = 0

        while (start < end):
            totalWaterUnits = abs(end - start)
            minHeight = min(A[start], A[end]) 
            area = minHeight * totalWaterUnits
            maxArea = max(maxArea, area)

            if A[end] < A[start]:
                end -= 1
            else:
                start += 1
        
        return maxArea

# 5 : Sum Zero
# Given an array A of N integers, are there elements a, b, c in S such that a + b + c = 0

# Find all unique triplets in the array which gives the sum of zero.

# Note:

# Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c) The solution set must not contain duplicate triplets.



# Problem Constraints

# 0 <= N <= 7000

# -108 <= A[i] <= 108



# Input Format

# Single argument representing a 1-D array A.



# Output Format

# Output a 2-D vector where each row represent a unique triplet.



# Example Input

# A = [-1,0,1,2,-1,4]


# Example Output

# [ [-1,0,1],
#   [-1,-1,2] ]


# Example Explanation

# Out of all the possible triplets having total sum zero,only the above two triplets are unique.

class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def threeSum(self, A):
        A = sorted(A) 
        ans = []
        
        for i in range(len(A)-2):
            # to avoid duplicate triplet
            if i > 0 and A[i] == A[i-1]:
                continue
            
            j = i + 1
            k = len(A) - 1
            target = -(A[i]) 
            while j < k:
                cur_sum =  A[j] + A[k]
                if cur_sum == target:
                    triplet = [-target,A[j],A[k]]
                    ans.append([-target,A[j],A[k]])
                    # another conditional for not calculating duplicates
                    while j < k and A[j] == A[j+1]:
                        j += 1
                        
                    while j < k and A[k] == A[k-1]:
                        k -= 1

                    j = j + 1
                    k = k - 1                    
                if cur_sum < target:
                    j = j + 1
                elif cur_sum > target:
                    k = k - 1
        return ans

# 6 : Pairs with given sum II

# Given a sorted array of integers (not necessarily distinct) A and an integer B, find and return how many pair of integers ( A[i], A[j] ) such that i != j have sum equal to B.

# Since the number of such pairs can be very large, return number of such pairs modulo (109 + 7).



# Problem Constraints
# 1 <= |A| <= 100000

# 1 <= A[i] <= 10^9

# 1 <= B <= 10^9



# Input Format
# The first argument given is the integer array A.

# The second argument given is integer B.



# Output Format
# Return the number of pairs for which sum is equal to B modulo (10^9+7).



# Example Input
# Input 1:

# A = [1, 1, 1]
# B = 2
# Input 2:

 
# A = [1, 1]
# B = 2


# Example Output
# Output 1:

#  3
# Output 2:

#  1


# Example Explanation
# Explanation 1:

#  Any two pairs sum up to 2.
# Explanation 2:

#  only pair (1, 2) sums up to 2.

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        dic = {}
        ans = 0
        mod = pow(10, 9) + 7

        # dictionary
        for ind, ele in enumerate(A):
            if ele in dic:
                dic[ele] += 1
            else:
                dic[ele] = 1

        for ele in A:
            if B - ele in dic:
                # i != j
                dic[ele] -= 1

                # if the pair constitutes the same element
                # then the frequency must at least be 2
                # to constitute a pair.
                if B - ele == ele and dic[ele] > 1:  # duplicates
                    ans += dic[ele] % mod
                else:
                    ans += dic[B - ele] % mod

                    # restoring the current element
                dic[ele] += 1

        return (ans // 2) % mod

        # TC: O(N); SC: O(N)


# optimisation

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        p1 = 0
        p2 = n - 1
        mod = pow(10, 9) + 7
        ans = 0
        while p1 < p2:
            summ = A[p1] + A[p2]
            if summ < B:
                p1 += 1
            elif summ > B:
                p2 -= 1
            else:
                if A[p1] == A[p2]:
                    # this is a scenario when we encounter duplicates
                    # thus, there are no other elements between p1 and p2 now
                    x = p2 - p1 + 1
                    ans += ((x * (x - 1)) // 2) % mod  # xC2
                    break
                else:
                    dup1 = 1
                    p1 += 1
                    while A[p1] == A[p1 - 1]:
                        p1 += 1
                        dup1 += 1

                    dup2 = 1
                    p2 -= 1
                    while A[p2] == A[p2 + 1]:
                        p2 -= 1
                        dup2 += 1

                    ans += (dup1 * dup2) % mod

        return ans % mod

        # TC: O(N); SC: O(1)
