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

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):

        n = len(A)
        minPrice = 3*10**9

        if n < 3:
            return - 1
        elif n==3:
            if A[0]<A[1] and A[1]<A[2]:
                return sum(B)
            else:
                return -1
            
        for j in range(1, n):
            midElement = A[j]
            midPrice = B[j]

            minLeftPrice = 3*10**9
            minRightPrice = 3*10**9

            for i in range(j):
                if A[i] < midElement and B[i] < minLeftPrice:
                    minLeftPrice = B[i]
            
            for k in range(j+1, n):
                if A[k] > midElement and B[k] < minRightPrice:
                    minRightPrice = B[k]

            total = minLeftPrice + minRightPrice + midPrice
            minPrice = min(minPrice, total)
        return minPrice


# 3 : Hollow diamond star pattern
# Write a program to input an integer N from user and print hollow diamond star pattern series of N lines.

# See example for clarifications over the pattern.

def main():
    n = int(input())

    for row in range(1, n+1):
        for col in range(0,n-row+1):
            print('*', end='')
        
        for col in range((row-1) * 2):
            print(' ', end='')

        for col in range(0, n - row + 1):
            print('*', end='')
        print()
    
    for row in range(1, n+1):
        for col in range(0,row):
            print('*', end='')
        
        for col in range((n-row) * 2):
            print(' ', end='')

        for col in range(0, row):
            print('*', end='')
        print() 

if __name__ == '__main__':
    main()

# 4 : Maximum positivity

# Given an array of integers A, of size N.

# Return the maximum size subarray of A having only non-negative elements. If there are more than one such subarray, return the one having the smallest starting index in A.

# NOTE: It is guaranteed that an answer always exists.

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        n = len(A)
        subarraylength, subarrayStartIndex, subarrayEndIndex = 0, 0, 0
        resultantSubarrayLength = -sys.maxsize - 1
        resultantSubarrayStartIndex, resultantSubarrayEndIndex = 0, 0
        

        for i in range(n):
            if A[i] < 0:
                subarrayStartIndex = i+1
            if A[i] > 0:
                subarrayEndIndex = i 
            
            if subarrayEndIndex >= subarrayStartIndex:
                subarraylength = (subarrayEndIndex - subarrayStartIndex)
            
                if subarraylength > resultantSubarrayLength:
                    resultantSubarrayLength = subarraylength
                    resultantSubarrayStartIndex, resultantSubarrayEndIndex = subarrayStartIndex, subarrayEndIndex

        return(A[resultantSubarrayStartIndex:resultantSubarrayEndIndex+1])


            


