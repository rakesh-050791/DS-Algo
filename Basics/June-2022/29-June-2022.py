# 1 :  Given an integer A, you have to tell whether it is a prime number or not.

# A prime number is a natural number greater than 1 which is divisible only by 1 and itself.

def main(num):
    for i in range(2,num):
        if (num % i) == 0:
            print("NO")
            break
    else:
        print("YES")

if __name__ == '__main__':
    num = int(input())
    main(num)




# 2 : You are given N positive integers.

# For each given integer A, you have to tell whether it is a perfect number or not.

# Perfect number is a positive integer which is equal to the sum of its proper positive divisors.
def main(n):
    
    while n >= 1:
        sum = 0

        num = int(input())

        for i in range(1, num-1):
            if num % i == 0:
                sum += i
        if sum == num:
            print('YES')
        else:
            print('NO')
        n -= 1

    
if __name__ == '__main__':
    n = int(input())
    main(n)


# 3 : Write a program to find sum all Natural numbers from 1 to N where you have to take N as input from user

def main(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
        
    print(sum)

if __name__ == '__main__':
    n = int(input())
    main(n)

# 4 : Given a number A. Return square root of the number if it is perfect square otherwise return -1.

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        start = 1
        end = A 

        while start <= end:
            mid = (start + end) // 2

            sqrt = mid * mid

            if sqrt > A:
                end = mid - 1 
            elif sqrt < A:
                start = mid + 1
            elif sqrt == A:
                return mid
        return -1
            
            


