# 1 : Fibonacci Number

# Given a positive integer A, write a program to find the Ath Fibonacci number.

# In a Fibonacci series, each term is the sum of the previous two terms and the first two terms of the series are 0 and 1. i.e. f(0) = 0 and f(1) = 1. Hence, f(2) = 1, f(3) = 2, f(4) = 3 and so on.

# NOTE: 0th term is 0. 1th term is 1 and so on.



# Problem Constraints
# 0 <= A <= 44



# Input Format
# First and only argument is an integer A.



# Output Format
# Return an integer denoting the Ath Fibonacci number.

# Example Input
# Input 1:

#  A = 4
# Input 2:

#  A = 6


# Example Output
# Output 1:

#  3
# Output 2:

#  8


# Example Explanation
# Explanation 1:

#  Terms of Fibonacci series are: 0, 1, 1, 2, 3, 5, 8, 13, 21 and so on.
#  0th term is 0 So, 4th term of Fibonacci series is 3. 
# Explanation 2:

#  6th term of Fibonacci series is 8.

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    i = int(input())
    a =0
    b =1
    result = [0,1]
    for x in range(i):
        c = a+b
        result.append(c)
        a = b
        b = c
    print(result[i])
    
    return 0

if __name__ == '__main__':
    main()


# 2 : Minimum Number of Squares
# Given an integer A. Return minimum count of numbers, sum of whose squares is equal to A.

# Problem Constraints
# 1 <= A <= 105


# Input Format
# First and only argument is an integer A.

# Output Format
# Return an integer denoting the minimum count.


# Example Input
# Input 1:

#  A = 6
# Input 2:

#  A = 5


# Example Output
# Output 1:

#  3
# Output 2:

#  2


# Example Explanation
# Explanation 1:

#  Possible combinations are : (12 + 12 + 12 + 12 + 12 + 12) and (12 + 12 + 22).
#  Minimum count of numbers, sum of whose squares is 6 is 3. 
# Explanation 2:

#  We can represent 5 using only 2 numbers i.e. 12 + 22 = 5


class Solution:
    # @param A : integer
    # @return an integer
    def countMinSquares(self, A):
        dp=[-1]*(A+1)
        dp[0]=0
        for i in range(1, A+1):
            ans=float('inf')
            for j in range(1, i+1):
                if j*j<=(i):
                    ans=min(ans, dp[i-j*j]+1)
                else:
                    break
            dp[i]=ans
        return dp[A]