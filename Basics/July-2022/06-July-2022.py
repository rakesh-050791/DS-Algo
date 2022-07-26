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

# 5 : You are given an integer T (number of test cases). 
# You are given array A and an integer B for each test case. 
# You have to tell whether B is present in array A or not.

def main():
    no_of_test_case = int(input())

    while no_of_test_case > 0:

        no_of_test_case -= 1
        find = 0
        A = input()
        arr = [int(x) for x in A.split()]
        element_to_find = int(input())

        for i in range(len(arr)):
            if arr[i] == element_to_find:
                find += 1
        if find > 0:
            print(1)
        else:
            print(0)


if __name__ == '__main__':
    main()



# 6 :
# You are given an integer array A. You have to find the second largest element/value in the array or report that no such element exists.

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        maxElement = -1
        maxElementIndex = 0

        for i in range(len(A)):
            if A[i] > maxElement:
                maxElement = A[i]
                maxElementIndex = i

        secondMax = -1

        for i in range(len(A)):
            if i != maxElementIndex:
                secondMax = max(secondMax , A[i])
        return secondMax


# 7 : Little Ponny is given an array, A, of N integers. In a particular operation, he can set any element of the array equal to -1.

# He wants your help in finding out the minimum number of operations required such that the maximum element of the resulting array is B. 
# If it is not possible, then return -1.

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        flag = count = 0

        for i in A:
            if i == B:
                flag = 1
            if i > B:
                count += 1

        return -1 if flag < 1 else count 

# 8 : Minimum Picks 
# You are given an array of integers A of size N.
# Return the difference between the maximum among all even numbers of A and the minimum among all odd numbers in A.

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        n = len(A)

        maxNo = -9999
        minNo = 9999

        for i in range(n):
            if A[i] % 2 == 0:
                if A[i] > maxNo:
                    maxNo = A[i]
            else:
                if A[i] < minNo:
                    minNo = A[i]

        return(maxNo - minNo)

# 9 :  Separate Odd Even 
# You are given an integer T denoting the number of test cases. For each test case, you are given an integer array A.

# You have to put the odd and even elements of array A in 2 separate arrays and print the new arrays.

# NOTE: Array elements should have the same relative order as in A.

def main():
    T = int(input())
    # evenArr = []
    # oddArr = []

    while T > 0:
        T -= 1
        evenArr = []
        oddArr = []
        N = int(input())
        arr = list(map(int,input().split()))
        for i in range(N):
            if arr[i] % 2 == 0:
                evenArr.append(arr[i])
            else:
                oddArr.append(arr[i])

        for k in range(len(oddArr)):
            print(oddArr[k],end=" ")
        print()
        for l in range(len(evenArr)):
            print(evenArr[l],end=" ")
        print()

    return 0 

if __name__ == '__main__':
    main()

# 10 : Multiple left rotations of the array
# Given an array of integers A and multiple values in B, 
# which represents the number of times array A needs to be left rotated.
# Find the rotated array for each value and return the result in the from of a matrix where ith row represents the rotated array for the ith value in B.

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of list of integers
    def solve(self, A, B):

        n = len(A)
        finalOutput = []

        for i in B:
            rotationNo = i
            newArr = A[:]
            rotationNo = rotationNo % n #to handel the case when rotationNo > array length
            self.rotateList(newArr, rotationNo)
            finalOutput.append(newArr)
        return finalOutput 

    def rotateList(self, arr, rotationNo):
        arrLength = len(arr)
        reversedArr = self.reverse(arr, 0, rotationNo - 1)
        # print("A = ", arr, "rotationNo = ", rotationNo, "reversedArr = ", reversedArr)
        reverseKElements = self.reverse(arr, rotationNo, arrLength - 1)
        # print("A = ", arr, "rotationNo = ", rotationNo, "reverseKElements = ", reverseKElements)
        reverseNElements = self.reverse(arr, 0, arrLength - 1)
        
                
    def reverse(self, arr, start, end):
        while start < end:
            arr[start] , arr[end] = arr[end] , arr[start]
            start += 1
            end -= 1

        









