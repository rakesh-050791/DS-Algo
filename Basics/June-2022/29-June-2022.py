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