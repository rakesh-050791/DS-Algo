# 1 : Given a parameter A = random string and B = 2d array [ [0,2], [2, 4]] 
# you need to calculate no of vowels in A as per the ranges given in B

# Eg : A = 'randoom' , B = [ [0,2], [2, 4] ]
# Output should be :  [1, 2]



A = 'randoom'
B = [ [0, 2] , [0, 4] ]

vowels = ["a", "e", "i", "o", "u"]

prefixSum = [0]*len(A)

prefixSum[0] = 1 if A[0] in vowels else 0 

print("BEFORE prefixSum =", prefixSum)

for i in range(1, len(A)):
    if A[i] in vowels:
        prefixSum[i] = prefixSum[i-1] + 1
    else:
        prefixSum[i] = prefixSum[i-1]
        
print("AFTER prefixSum =", prefixSum)

response = []

for i in range(len(B)):
    start , end = B[i][0], B[i][1]
    if start == 0:
        response.append(prefixSum[end])
    else:
        response.append(prefixSum[end] - prefixSum[start -1])

print("Response =", response)