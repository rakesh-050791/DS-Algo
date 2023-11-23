# Properties of XOR 

# X -> Any Element 

# X ^ X = 0
# 0 ^ X = X 
# X ^ Y = Y ^ X

# XOR is commutative and associative, meaning the order of XOR operations doesn't matter.


# Convert Integer to Binary


def int_to_binary(num):
    binary_representation = ""
    
    while num > 0:
        # Get the remainder when dividing by 2
        remainder = num % 2
        
        # Prepend the remainder to the binary representation
        binary_representation = str(remainder) + binary_representation
        
        # Update num by integer division by 2
        num //= 2

    # If the number was initially 0, the result will be an empty string
    return binary_representation if binary_representation else "0"

# Example
decimal_num = 10
binary_result = int_to_binary(decimal_num)
print(binary_result)  # Output: '1010'

This function works by repeatedly dividing the number by 2, obtaining the remainder, and concatenating it to the left of the current binary representation. The process continues until the number becomes 0.


# Convert Binary to integer

def binary_to_int(binary_str):
    decimal_num = 0
    power = 0
    
    # Iterate through the binary string from right to left
    for bit in reversed(binary_str):
        # Convert the bit to an integer and add it to the result
        decimal_num += int(bit) * (2 ** power)
        
        # Increment the power for the next bit
        power += 1

    return decimal_num

# Example
binary_str = '1010'
decimal_result = binary_to_int(binary_str)
print(decimal_result)  # Output: 10


This function iterates through the binary string from right to left, converting each bit to an integer and adding it to the result multiplied by the corresponding power of 2.