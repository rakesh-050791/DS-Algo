						# Bit Manipulations

# 1 : Help From Sam 

# Alex and Sam are good friends. Alex is doing a lot of programming these days. He has set a target score of A for himself.
# Initially, Alex's score was zero. Alex can double his score by doing a question, or
# Alex can seek help from Sam for doing questions that will contribute 1 to Alex's score. 
# Alex wants his score to be precisely A. Also, he does not want to take much help from Sam.
# Find and return the minimum number of times Alex needs to take help from Sam to achieve a score of A.

# Solution 

# Hint 1 : When A = 5
# The Question Says 
# 1. Alex can double his score by doing a question, or 
# 2. Alex can seek help from Sam for doing questions that will contribute 1 to Alex’s score. 
# 3. Alex wants his score to be precisely A.

# So assume Alex score initially is 0. Now to reach it to A say 5 we have two solution
# 1. Either Alex can double his score by doing a question. But 2x0 = 0.
# 2. Or Alex can seek help from Sam. So 0+ 1= 1, 
# 3. After this Alex can double his score by doing a question. So, 1x2 =2
# 4. Again, Alex can double his score by doing a question. Since in question it is mention “Alex does not want to take much help from Sam”. So, 2x2 =4
# 5. Now Alex has to take help from Sam so that 4+1=5 which is A.
# If we go for other condiotion in which Alex double his score by doing a question then. 4x2 =8 which is not A. So that is why he need Sam’s help.

# So finally we can tell how many times Alex has taken help by using counter viz., two times from above observation


# Hint 2 : when A = 7 
# There will be 4 1’s where alex need to take help from Sam. 
# Step 1: Alex take help (0 + 1).
# Step 2: Alex will do on his own (1 * 2 = 2)
# Step 3 :  Alex take help (2 + 1).
# Step 4: Alex will do on his own (3 * 2 = 6)
# Step 5: Alex take help (6 + 1).

# The number of times Alex took help is 3

# Basically the idea behind the solution is to check the no of set bits in given integer


class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):

        numberOfSetBits = 0

        while (A > 0):
            if A & 1 == 1:
                numberOfSetBits += 1
            
            A = A >> 1
        return numberOfSetBits


# 2 : Finding Good Days

# Alex has a cat named Boomer. He decides to put his cat to the test for eternity.

# He starts on day 1 with a stash of food unit, every next day, the stash doubles.

# If Boomer is well behaved during a particular day, she receives food worth equal to the stash on that day.

# Boomer receives a net worth of A units of food. What is the number of days he was well behaved?

# Explanation :
# Given stash doubles every next day:
#   1st Day   stash is  20  =>  1 Unit
#   2nd Day  stash is 21  =>  2 Units
#   3rd Day  stash is  22   =>  4 Units
#   4th Day  stash is  23   =>  8 Units
#   5th Day  stash is  24   =>  16 Units
#   . .
#   . .
#   Nth Day  stash is 2N-1 => say(X Units)

# Cat will be rewarded with total stash units on that particular day if behaved properly, Else it won't get any food(i.e., 0 stash Units) if not behaved properly.
 
# Ex1:
#   now let's consider cat was given stash Units N = 13
#   so, In what all ways we can add the above stash Units, such that total will be equal to N = 13.
#   ==> (1 + 4 + 8) (i.e., 1st Day + 3rd Day + 4th Day) ==> 3 Days(Cat Behaved)
#   Here we can write 13 in Binary as  '1101' and our answer is 3.
  
# Ex2:
#   now let's consider cat was given stash Units N = 16
#   so, In what all ways we can add the above stash Units, such that total will be equal to N = 16.
#   ==> (16) (i.e., Only on 5th Day) ==> 1 Day (Cat Behaved)
#   Here we can write 16 in Binary as  '10000' and our answer is 1.
  
# Ex3:
# now let's consider cat was given stash Units N = 15
#         so, In what all ways we can add the above stash Units, such that total will be equal to N = 15.
# ==> (1 + 2 + 4 + 8) (i.e., 1st Day + 2nd Day + 3rd Day + 4th Day) ==> 4 Days (Cat Behaved)
# Here we can write 15 in Binary as  '1111' and our answer is 4.
 
# From Above Examples, we can observe whatever N can be, the number of Days cat behaved = number of Set bits in N.

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        numberOfSetBits = 0

        while (A > 0):
            if (A & 1 == 1):
                numberOfSetBits += 1
            
            A = A >> 1
        return numberOfSetBits


# 3 :  Unset x bits from right

# Given an integer A. Unset B bits from the right of A in binary.
# For eg:-
# A = 93, B = 4
# A in binary = 1011101
# A should become = 1010000 = 80. Therefore return 80.


# Problem Constraints
# 1 <= A <= 1018
# 1 <= B <= 60


# Input Format
# The first argument is a single integer A.
# The second argument is a single integer B.


# Output Format
# Return the number with B unset bits from the right.


# Example Input
# Input 1:-
# A = 25
# B = 3
# Input 2:-
# A = 37
# B = 3


# Example Output
# Output 1:-
# 24
# Output 2:-
# 32


# Example Explanation
# Explanation 1:-
# A = 11001 to 11000
# Explantio 2:-
# A = 100101 to 100000



# class Solution:
#     # @param A : long
#     # @param B : integer
#      # @return an long
#     def solve(self, A, B):

#         A = A>>B; #// Unsets any set numbers by Bth place, for example: 1011>>0010
#         A = A<<B;# // Brings back digits post Bth place, our answer, for example 1000<<0010
#         return A;
class Solution:
    # @param A : long
    # @param B : integer
    # @return an long
    def solve(self, A, B):
        return (A >> B) << B


# 4 : Subarrays with Bitwise OR 1
# Given an array B of length A with elements 1 or 0. Find the number of subarrays such that the bitwise OR of all the elements present in the subarray is 1.


# Problem Constraints
# 1 <= A <= 105


# Input Format
# The first argument is a single integer A.
# The second argument is an integer array B.


# Output Format
# Return the number of subarrays with bitwise array 1.


# Example Input
# Input 1:
#  A = 3
# B = [1, 0, 1]
# Input 2:
#  A = 2
# B = [1, 0]


# Example Output
# Output 1:
# 5
# Output2:
# 2


# Example Explanation
# Explanation 1:
# The subarrays are :- [1], [0], [1], [1, 0], [0, 1], [1, 0, 1]
# Except the subarray [0] all the other subarrays has a Bitwise OR = 1
# Explanation 2:
# The subarrays are :- [1], [0], [1, 0]
# Except the subarray [0] all the other subarrays has a Bitwise OR = 1

class Solution:
    # @param A : integer
    # @param B : list of integers
     # @return an long
    def solve(self, A, B):
        ans = 0
        prev_subarray_count = 0

        for i in range(A):
            if B[i] == 1:
                current_subarray_count = i+1 # when ith element(rightMostElement) = 1. no. of subarrays= i+1
                ans += current_subarray_count
                prev_subarray_count = current_subarray_count

            else:
                ans += prev_subarray_count # when ith element = 0. then no of subarrays = previousSubarrayCount

        return(ans)

# 5 : Single Number III
# Given an array of positive integers A, two integers appear only once, and all the other integers appear twice.
# Find the two integers that appear only once.

# Note: Return the two numbers in ascending order.


# Problem Constraints
# 2 <= |A| <= 100000
# 1 <= A[i] <= 109



# Input Format
# The first argument is an array of integers of size N.



# Output Format
# Return an array of two integers that appear only once.



# Example Input
# Input 1:
# A = [1, 2, 3, 1, 2, 4]
# Input 2:

# A = [1, 2]


# Example Output
# Output 1:
# [3, 4]
# Output 2:

# [1, 2]


# Example Explanation
# Explanation 1:
# 3 and 4 appear only once.
# Explanation 2:

# 1 and 2 appear only once.

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        xor = 0     # the result of a xor b
        grA = 0
        grB = 0
        for x in A:
            xor ^= x
        mask = (xor & (xor - 1)) ^ xor  # the last bit that a differs from b
        for x in A:
            # based on the last bit, group the items into groupA (include a) and groupB
            if x & mask:
                grA ^= x
            else:
                grB ^= x  
        lst = [grA, grB]
        lst.sort()
        return lst
