# 1 : Given an Integer N. Print N stars in a single line.

'''For example:-

Input :-

5

Output :-

***** '''

def main(n):
    for i in range(n):
        print('*', end='')

if __name__ == '__main__':
    n = int(input())
    main(n)


# 2 : Given two integers N and M. Print a matrix of stars of N rows and M columns.

'''For example

Input:-

3 2

Output:-

**

**

** '''

def main(n, m):
    for i in range(n):
        for i in range(m):
            print('*', end='')
        print()

if __name__ == '__main__':
    n, m = map(int, input().split())
    main(n, m)


# 3 : Given an integer N, print the corresponding stair pattern for N.

'''For example if N = 4 then stair pattern will be like:

*
**
***
**** '''

def main(n):
    for i in range(n):
        for j in range (i+1):
            print('*', end='')
        print()

if __name__ == '__main__':
    n = int(input())
    main(n)


# 4 : Given an integer A, you have to tell whether it is a prime number or not.

'''A prime number is a natural number greater than 1 which is divisible only by 1 and itself.'''

def main(a):
    for i in range(2,a):
        if (a % i) == 0:
            print("NO")
            break
    else:
        print("YES")

if __name__ == '__main__':
    A = int(input())
    main(A)

# 868725 999563
# def main(a):
#     prime = False
#     count = 2
#     if a > 1:
#         for i in range(count, count < a):
#             if (a % i) == 0:
#                 count += 1
#                 prime = False
#             else:
#                 prime = True
#     if prime == True:
#         print("YES")
#     else:
#         print("NO")

# if __name__ == '__main__':
#     A = int(input())
#     main(A)


# 5 : Write a program to input three numbers(A, B & C) from user and print the maximum element among A, B & C in each line.

def main(num1, num2, num3):
    if (num1 >= num2) and (num1 >= num3):
        print(num1)
    elif (num2 >= num1) and (num2 >= num3):
        print(num2)
    else:
        print(num3)

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    main(a, b, c)


# 6 :  Write a program to input T numbers(N) from user and print first and last digits of the given numbers.

def main(T):
    for i in range(0, T):
        n = int(input())

        first = 0
        last = 0
        last = n % 10

        while(n > 0):
            first = (n % 10) 
            n //= 10
        print(first, last)


if __name__ == '__main__':
    T = int(input())
    main(T)

