# 1 : Given an integer array A of size N and an integer B, 
# you have to print the same array after rotating it B times towards the right.

def main():    
    A = list(map(int,input().split()))
    arr = A[1::]
    rotationNo = int(input())

    rotateList(arr, rotationNo)
    
    for i in arr:
        print(i, end=' ')

def rotateList(arr, rotationNo):
    arrLength = len(arr)
    rotationNo = rotationNo % arrLength #to handel the case when rotationNo > arrLength
    reversedArr = reverse(arr, 0, arrLength -1 )
    reverseKElements = reverse(arr, 0, rotationNo - 1)
    reverseNElements = reverse(arr, rotationNo, arrLength - 1)

                
def reverse(arr, start, end):
    while start < end:
        arr[start] , arr[end] = arr[end] , arr[start]
        start += 1
        end -= 1


if __name__ == '__main__':
    main()


