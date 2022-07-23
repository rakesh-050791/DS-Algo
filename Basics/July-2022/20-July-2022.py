# 1 : Length of longest consecutive ones

# Given a binary string A. It is allowed to do at most one swap between any 0 and 1.
# Find and return the length of the longest consecutive 1’s that can be achieved.

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        n = len(A)
        count = 0

        for i in range(n):
            if A[i] == '1':
                count += 1
        
        #if all is 1:
        if count == n:
            return n
        #if all are 0:    
        elif count == 0:
            return count

        result = 0

        for i in range(n):
            if A[i] =='0':
        
                left = 0

                for j in range(i-1, -1, -1):
                    if A[j] == '1':
                        left += 1
                    else:
                        break

                right = 0

                for j in range(i+1, n):
                    if A[j] == '1':
                        right += 1
                    else:
                        break

                if left + right == count:
                    ones = left + right
                else:
                    ones = left + right + 1
                result = max(result, ones)
        
        return result


# 2 : Christmas Trees
# You are given an array A consisting of heights of Christmas trees and an array B of the same size consisting of the cost of each of the trees (Bi is the cost of tree Ai, where 1 ≤ i ≤ size(A)), and you are supposed to choose 3 trees (let's say, indices p, q, and r), such that Ap < Aq < Ar, where p < q < r.
# The cost of these trees is Bp + Bq + Br.

# You are to choose 3 trees such that their total cost is minimum. Return that cost.

# If it is not possible to choose 3 such trees return -1.
