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



# 2 : Given an array A and an integer B. 
# A pair(i, j) in the array is a good pair if i != j and (A[i] + A[j] == B). 
# Check if any good pair exist or not.

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        for i in range(0, len(A)-1):
            for j in range(i+1, len(A)):
                if (A[i] + A[j] == B):
                    return 1
        return 0


# 3 : Write a program to print maximum and minimum elements of the input array A of size N 
# where you have to take integer N and other N elements as input from the user.

def main():
    A = list(map(int, input().split()))
    arrLength = A[0]
    arr = A[1:] # Removing the fist element, which signifies number of elements
    # x.pop(0) # Removing the fist element, which signifies number of elements
    maxElement = minElement = arr[0]

    for i in arr:
        if i > maxElement:
            maxElement = i
        elif i < minElement:
            minElement = i
    print(maxElement, minElement)

if __name__ == '__main__':
    main()


 # 4 : You are given a constant array A.

# You are required to return another array which is the reversed form of the input array.


class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def solve(self, A):
        newArray = list(A)
        tempArray = []

        i = 0 
        j = len(newArray) -1 

        while i < j:
            newArray[i], newArray[j] = newArray[j], newArray[i]

            i += 1
            j -= 1

# 5 : 









