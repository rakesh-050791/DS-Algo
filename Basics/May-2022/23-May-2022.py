
### 23 May Assignment

# 1 : Write a program to input T numbers(N) from user and print count of digits of the given numbers.

def main():
    T = int(input())
    while T > 0:
        T -= 1
        num = int(input())
        count = 0
        if num == 0:
            count = 1
        while num > 0:
            num //= 10
            count += 1
        print(count)
    return 0

if __name__ == '__main__':
    main()

# 2 : Write a program to input T numbers(N) from user and print the sum of the digits of the given numbers.

def main():
    T = int(input())
    while T > 0:
        T -= 1
        num = int(input())
        count = 0
        if num == 0:
            count = 1
        while num > 0:
            r = num % 10
            count += r
            num //= 10
        print(count)
    return 0

if __name__ == '__main__':
    main()

# 3 : Given two numbers A and B. Print the floor of A/B.

def main(a, b):
    x = a // b
    print(a // b)
    return x

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    main(a, b)

# 4 : For a given number A, print its multiplication table having the first 10 multiples.

def main(num):
    count = 0

    while count < 10:
        count += 1
        result = '{a} * {b} = {mul}'.format(a=num, b=count, mul=num*count )
        print(result)
        

if __name__ == '__main__':
    a = int(input())
    main(a)

# 5 : You are given two integers A and B. You have to find the value of AB

def main(a, b):
    ans = 1
    while b > 0:
        ans *= a
        b -= 1
    print(ans)

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    main(a, b)
