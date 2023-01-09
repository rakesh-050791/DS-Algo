# 1 : Finish Maximum Jobs

# There are N jobs to be done, but you can do only one job at a time.

# Given an array A denoting the start time of the jobs and an array B denoting the finish time of the jobs.

# Your aim is to select jobs in such a way so that you can finish the maximum number of jobs.

# Return the maximum number of jobs you can finish.

# Input Format
# The first argument is an integer array A of size N, denoting the start time of the jobs.
# The second argument is an integer array B of size N, denoting the finish time of the jobs.



# Output Format
# Return an integer denoting the maximum number of jobs you can finish.



# Example Input
# Input 1:

#  A = [1, 5, 7, 1]
#  B = [7, 8, 8, 8]
# Input 2:

#  A = [3, 2, 6]
#  B = [9, 8, 9]


# Example Output
# Output 1:

#  2
# Output 2:

#  1


# Example Explanation
# Explanation 1:

#  We can finish the job in the period of time: (1, 7) and (7, 8).
# Explanation 2:

#  Since all three jobs collide with each other. We can do only 1 job.

class Solution:
    def solve(self, A, B):
        n = len(A)

        Mytuple = []

        for i in range(n):
            Mytuple.append((A[i], B[i]))
        
        Mytuple.sort(key = lambda x: x[1])

        jobs = 1

        previousEndTime = Mytuple[0][1]

        for i in range(1, n):
            startTime = Mytuple[i][0]

            if startTime >= previousEndTime:
                jobs += 1
                previousEndTime = Mytuple[i][1]

        return jobs

# 2 : Free Cars

# Given two arrays, A and B of size N. A[i] represents the time by which you can buy the ith car without paying any money.

# B[i] represents the profit you can earn by buying the ith car. It takes 1 minute to buy a car, so you can only buy the ith car when the current time <= A[i] - 1.

# Your task is to find the maximum profit one can earn by buying cars considering that you can only buy one car at a time.

# NOTE:

# You can start buying from time = 0.
# Return your answer modulo 109 + 7.


# Problem Constraints
# 1 <= N <= 105
# 1 <= A[i] <= 109
# 0 <= B[i] <= 109



# Input Format
# The first argument is an integer array A represents the deadline for buying the cars.
# The second argument is an integer array B represents the profit obtained after buying the cars.



# Output Format
# Return an integer denoting the maximum profit you can earn.



# Example Input
# Input 1:

#  A = [1, 3, 2, 3, 3]
#  B = [5, 6, 1, 3, 9]
# Input 2:

#  A = [3, 8, 7, 5]
#  B = [3, 1, 7, 19]


# Example Output
# Output 1:

#  20
# Output 2:

#  30


# Example Explanation
# Explanation 1:

#  At time 0, buy car with profit 5.
#  At time 1, buy car with profit 6.
#  At time 2, buy car with profit 9.
#  At time = 3 or after , you can't buy any car, as there is no car with deadline >= 4.
#  So, total profit that one can earn is 20.
# Explanation 2:

#  At time 0, buy car with profit 3.
#  At time 1, buy car with profit 1.
#  At time 2, buy car with profit 7.
#  At time 3, buy car with profit 19.
#  We are able to buy all cars within their deadline. So, total profit that one can earn is 30.

import heapq as hq

class Solution:
    def solve(self, A, B):
        N = len(B)
        m = 1000000007

        tup = []
        for i in range(N):
            tup.append(( B[i],A[i] ))
            
        # sort based on time 
        tup.sort(key = lambda x: x[1])

        minheap = []
        max_val = max(A)
        total_sum = 0

        # to track the time 
        time = 0
        for i in range(N):
            cur_profit   = tup[i][0]
            cur_time     = tup[i][1]

            # we are buying 
            if cur_time > time:
                total_sum += cur_profit
                hq.heappush(minheap,tup[i])
                time += 1
            else:
                # we are replacing with a cheap car
                min_profit = minheap[0][0]   
                if cur_profit > min_profit:
                    delval = hq.heappop(minheap)
                    hq.heappush(minheap,tup[i])
                    total_sum -= delval[0]
                    total_sum += cur_profit
        return total_sum % m


# 3 : Distribute Candy

# N children are standing in a line. Each child is assigned a rating value.

# You are giving candies to these children subjected to the following requirements:

# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# What is the minimum number of candies you must give?



# Problem Constraints
# 1 <= N <= 105
# -109 <= A[i] <= 109



# Input Format
# The first and only argument is an integer array A representing the rating of children.



# Output Format
# Return an integer representing the minimum candies to be given.



# Example Input
# Input 1:

#  A = [1, 2]
# Input 2:

#  A = [1, 5, 2, 1]


# Example Output
# Output 1:

#  3
# Output 2:

#  7


# Example Explanation
# Explanation 1:

#  The candidate with 1 rating gets 1 candy and candidate with rating 2 cannot get 1 candy as 1 is its neighbor. 
#  So rating 2 candidate gets 2 candies. In total, 2 + 1 = 3 candies need to be given out.
# Explanation 2:

#  Candies given = [1, 3, 2, 1]

class Solution:
    # @param A : list of integers
    # @return an integer
    def candy(self, A):
        n = len(A)

        # Give each child 1 candy
        candies_00 = [1] * n
        
        # From Left to right :  
        # if child to right has higher rating—>give right child 1 candy extra than no. of candies 
        # to left child
        for i in range(1, n):
            if A[i] > A[i-1]:
                candies_00[i] = candies_00[i-1] + 1

        
        # From right to left :  
        # if child to left has higher rating—>give left child 1 candy extra than no. of candies 
        # to right child
        candies_01 = [1] * n
        for i in range(n-2, -1, -1):
            if A[i] > A[i+1]:
                candies_01[i] = candies_01[i+1] + 1

        ans = 0
        # get max from left to right and right to left
        for x, y in zip(candies_00, candies_01):
            ans += max(x, y)
        
        return ans