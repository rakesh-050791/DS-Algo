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


# Approach

# Algorithm:
# 1. Simply using 2 pointers when both pointers equal to target we iterate left towards right and count all a[left]in "count" varible and similarly we iterate right towards left and count all of them in "count1" variable. answer is  incremented by count*count1

# One edge case is if A[left]==A[right] and A[left]+A[right]==B then while we increment for "count" variable it goes till right and no answer for "count1" in this case, ans incremented by count*(count+1)/2
 
# Another edge case is ifA[left]!=A[right]  but left pointer goes upto right pointer in calculating "count1",  thats why we decrement left pointer by 1 in this case.


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

# 7 : Minimize the absolute difference

# Given three sorted arrays A, B and Cof not necessarily same sizes.

# Calculate the minimum absolute difference between the maximum and minimum number from the triplet a, b, c such that a, b, c belongs arrays A, B, C respectively. i.e. minimize | max(a,b,c) - min(a,b,c) |.

# Example :

# Input:

# A : [ 1, 4, 5, 8, 10 ]
# B : [ 6, 9, 15 ]
# C : [ 2, 3, 6, 6 ]
# Output:

# 1
# Explanation: We get the minimum difference for a=5, b=6, c=6 as | max(a,b,c) - min(a,b,c) | = |6-5| = 1.

# See Expected Output


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        pointer_A, range_A = 0, len(A)
        pointer_B, range_B = 0, len(B)
        pointer_C, range_C = 0, len(C)

        minimum = lambda a,b,c : max(abs(a-b), abs(b-c), abs(c-a))
        val = float('inf')

        while ( pointer_A < range_A and
                pointer_B < range_B and
                pointer_C < range_C):
               
            cal = minimum(A[pointer_A], B[pointer_B], C[pointer_C])
            if cal < val:
                val = cal

            if (A[pointer_A] < C[pointer_C] and
                A[pointer_A] < B[pointer_B]):
                pointer_A += 1

            elif (B[pointer_B] < C[pointer_C]):
                pointer_B += 1
               
            else:
                pointer_C += 1

        return val


# 8 : Sort by Color | DUTCH NATIONAL FLAG ALGO 

# Given an array with N objects colored red, white, or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent red, white, and blue, respectively.

# Note: Using the library sort function is not allowed.



# Problem Constraints
# 1 <= N <= 1000000
# 0 <= A[i] <= 2


# Input Format
# First and only argument of input contains an integer array A.


# Output Format
# Return an integer array in asked order


# Example Input
# Input 1 :
#     A = [0 1 2 0 1 2]
# Input 2:

#     A = [0]


# Example Output
# Output 1:
#     [0 0 1 1 2 2]
# Output 2:

#     [0]


# Example Explanation
# Explanation 1:
#     [0 0 1 1 2 2] is the required order.



# Approach

# 1)sort the array with custom comparator function.

# 2)use cmp_to_key to compare & change the original array list.sort()
# 3)while creating the custom comparator function return 1,0,-1 for your result as mentioned

# optimized 
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def sortColors(self, A):
            l = 0
            m = 0
            h = len(A) - 1

            while m <= h:
                if A[m] == 1:
                    m += 1
                
                elif A[m] == 0:
                    temp = A[m]
                    A[m] = A[l]
                    A[l] = temp
                    m += 1
                    l += 1
                
                elif A[m] == 2:
                    temp1 = A[m]
                    A[m] = A[h]
                    A[h] = temp1
                    h -= 1
            return A


#BRUTEFORCE:
   def sortColors(self, A):
        count_0 = []
        count_1 = []
        count_2 = []

        for i in A:
            if i == 0:
                count_0.append(i)
            elif i == 1:
                count_1.append(i)
            else:
                count_2.append(i)
               
        return(count_0+count_1+count_2)


# 9 : Closest pair from sorted arrays

# Given two sorted arrays of distinct integers, A and B, and an integer C, find and return the pair whose sum is closest to C and the pair has one element from each array.

# More formally, find A[i] and B[j] such that abs((A[i] + B[j]) - C) has minimum value.

# If there are multiple solutions find the one with minimum i and even if there are multiple values of j for the same i then return the one with minimum j.

# Return an array with two elements {A[i], B[j]}.



# Problem Constraints

# 1 <= length of both the arrays <= 100000

# 1 <= A[i], B[i] <= 109

# 1 <= C <= 109



# Input Format

# The first argument given is the integer array A.
# The second argument given is the integer array B.
# The third argument given is integer C.



# Output Format

# Return an array of size 2 denoting the pair which has sum closest to C.



# Example Input

# Input 1:

#  A = [1, 2, 3, 4, 5]
#  B = [2, 4, 6, 8]
#  C = 9
# Input 2:

#  A = [5, 10, 20]
#  B = [1, 2, 30]
#  C = 13


# Example Output

# Output 1:

#  [1, 8]
# Output 2:

#  [10, 2]


# Example Explanation

# Explanation 1:

#  There are three pairs: (1, 8), (3, 6), (5, 4), that gives the minimum value.
#  Since we have to return the value with minimum i and then with minimum j. We will return [1, 8].
# Explanation 2:

#  [10, 2] is the only pair such abs(10+2-13) is minimum.

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        last_sum = float('inf') 
        low = 0
        high = len(B) - 1

        first_indx = 0
        secnd_indx = -1

        while low <= len(A)-1 and high >= 0:
            
            cur_sum = A[low] + B[high]
            
            if abs(cur_sum - C) < last_sum:
                # min-diff check with last answer
                last_sum = abs(cur_sum - C)
                first_indx = low
                secnd_indx = high


            elif abs(cur_sum - C) == last_sum:
                # if sum is equal then we need min - i index answer

                if low < first_indx:
                    first_indx = low
                    secnd_indx = high

                # if i is same , then min j index check 
                elif low == first_indx and high < secnd_indx:
                    first_indx = low
                    secnd_indx = high



            if cur_sum > C:
                high -= 1
            else:
                low += 1
                
        return(A[first_indx],B[secnd_indx])


# 10 : 3 Sum 

# Given an array A of N integers, find three integers in A such that the sum is closest to a given number B. Return the sum of those three integers.

# Assume that there will only be one solution.



# Problem Constraints
# -108 <= B <= 108
# 1 <= N <= 104
# -108 <= A[i] <= 108


# Input Format
# First argument is an integer array A of size N.

# Second argument is an integer B denoting the sum you need to get close to.



# Output Format
# Return a single integer denoting the sum of three integers which is closest to B.



# Example Input
# Input 1:

# A = [-1, 2, 1, -4]
# B = 1
# Input 2:

 
# A = [1, 2, 3]
# B = 6


# Example Output
# Output 1:

# 2
# Output 2:

# 6


# Example Explanation
# Explanation 1:

#  The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)
# Explanation 2:

#  Take all elements to get exactly 6.

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        A.sort()
        N = len(A) - 1

        diff = float('inf')
        ans = 0

        for i in range(N-1):
            j = i + 1
            k = len(A) - 1

            while j < k:
                cur_sum = A[i] + A[j] + A[k]

                if cur_sum == B:
                    return cur_sum

                if abs(cur_sum - B) < diff:
                    diff = abs(cur_sum - B)
                    ans = cur_sum

                elif cur_sum < B:
                    j += 1

                else:
                    k -= 1


        return ans

# 11 : Another Count Rectangles

# Given a sorted array of distinct integers A and an integer B, find and return how many rectangles with distinct configurations can be created using elements of this array as length and breadth whose area is lesser than B.

# (Note that a rectangle of 2 x 3 is different from 3 x 2 if we take configuration into view)



# Problem Constraints

# 1 <= |A| <= 100000
# 1 <= A[i] <= 109
# 1 <= B <= 109



# Input Format

# The first argument given is the integer array A.

# The second argument given is integer B.



# Output Format

# Return the number of rectangles with distinct configurations with area less than B modulo (109 + 7).



# Example Input

# Input 1:

#  A = [1, 2]
#  B = 5
# Input 2:

#  A = [1, 2]
#  B = 1


# Example Output

# Output 1:

#  4
# Output 2:

#  0


# Example Explanation

# Explanation 1:

#  All 1X1, 2X2, 1X2 and 2X1 have area less than 5.
# Explanation 2:

#  No Rectangle is valid.

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        A.sort()
        lenA= len(A)
        start,end = 0,lenA-1
        modulo = 1000000007
        count = 0

        while end>=0 and start<lenA:
            area = A[start] * A[end]
         
            if area<B :
                count +=(end+1)
                start +=1
            else:
                end -=1
            count %= modulo

        return count%modulo


# 12 : Array 3 Pointers

# You are given 3 sorted arrays A, B and C.

# Find i, j, k such that : max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i])) is minimized.

# Return the minimum max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i])).

# Problem Constraints
# 0 <= len(A), len(B), len(c) <= 106

# 0 <= A[i], B[i], C[i] <= 107

# Input Format
# First argument is an integer array A.

# Second argument is an integer array B.

# Third argument is an integer array C.



# Output Format
# Return an single integer denoting the minimum max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i])).



# Example Input
# Input 1:

#  A = [1, 4, 10]
#  B = [2, 15, 20]
#  C = [10, 12]
# Input 2:

#  A = [3, 5, 6]
#  B = [2]
#  C = [3, 4]


# Example Output
# Output 1:

#  5
# Output 2:

#  1


# Example Explanation
# Explanation 1:

#  With 10 from A, 15 from B and 10 from C.
# Explanation 2:

#  With 3 from A, 2 from B and 3 from C.

class Solution:
# @param A : tuple of integers
# @param B : tuple of integers
# @param C : tuple of integers
# @return an integer
    def minimize(self, A, B, C):
        n=[len(A)-1, len(B)-1, len(C)-1]
        p1, p2, p3 = n
        mindiff=1e7
        while(p1>=0 and p2>=0 and p3>=0):
            mindiff = min(mindiff, max(abs(A[p1]-B[p2]), abs(B[p2]-C[p3]), abs(C[p3]-A[p1])))
            # print(p1, p2, p3, A[p1], B[p2], C[p3], max(A[p1], B[p2], C[p3])-min(A[p1], B[p2], C[p3]))
            if(A[p1] >= B[p2] and A[p1] > C[p3]):
                p1-=1
            elif(B[p2] > A[p1] and B[p2] > C[p3]):
                p2-=1
            else:
                p3-=1
        return mindiff