# 4 : Food Packets Distribution
# The government wants to set up B distribution offices across N cities for the distribution of food
# packets. The population of the ith city is A[i]. Each city must have at least 1 office, and people can go to an office of their own city. We want to maximize the minimum number of people who can get food in any single office.


# Input Format
# The first line of input contains an integer array A. 

# The second line of input contains an integer B.



# Output Format
# Return one integer representing the maximum number of people who can get food in any single office.


# Example Input
# Input 1:

# A = [10000, 20000, 30000]
# B = 6



# Example Output
# Output 1: 10000


# Example Explanation
# Explanation 1:

#   1 office can be opened in the first city,
#   2 offices in the second city and
#   3 in the third. This way ,
#   10,000 people can get food in the office in the first city, and
#   10,000 people can get food in each office in the second city and
#   10,000 people can get food in third city.
#   We will allot 10000 people in each office in the third city. 
#   Had we alloted more in some office, we had to allot lesser in some other office which will reduce the answer.

class Solution:
    def solve(self, A, B):
        n = len(A)        

        low = 0
        high = min(A)
        result = -1

        while (low <= high):
            mid = (low + high) // 2

            if self.check(A, B, mid):
                result = mid
                low = mid + 1
            else:
                high = mid - 1 
        return 0 if result == -1 else result

    def check(self, A, B, mid):
        centers = 0
        for i in range(len(A)):
            if mid == 0:
                centers += A[i]
            else:
                centers += A[i]//mid
        return centers >= B

