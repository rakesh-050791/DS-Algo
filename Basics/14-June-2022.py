#  1 :
# Write a program to return a single string from two given strings, separated by a space, 
# and also swap the first two characters of the first string (s1) with the second one (s2).

def swap(s1, s2):
    str= ''

    str += s2[:2] + s1[2::] + ' ' + s1[:2] + s2[2::]

    return str


# 2 : Write a program that takes a sentence as a parameter and returns the number of alphabets and digits separately.

def alphandig_count(s):
    '''Input: s takes the string as input
       Output: return count of alphabets and digits'''
       
    count_digit = 0
    count_alpha = 0

    # YOUR CODE GOES HERE
    for i in range(len(s)):
        # print("Value of I %s" %i)
        if s[i].isdigit():
            count_digit += 1
        elif s[i].isalnum():
            count_alpha += 1
    
    return count_alpha, count_digit


# 3 : 
# Given a string, complete the function modify() that returns the string after performing string modifications according to the following conditions:

# 1) If the length of the given string is less than 3, leave it unchanged.

# 2) Otherwise add 'ing' at the end of the given string.

# 3) If the given string already ends with 'ing' then add 'ly' instead.

def modify(s):
    '''Input: s is the string
       Output:return the resultant string with described modifications'''
    # YOUR CODE GOES HERE

    if len(s) < 3:
        return s
    elif s[-3::] == 'ing':
        s += 'ly'
    else:
        s += 'ing'
    return s

# 4 :Write a program to check whether the given string is a palindrome or not. Return True if it is palindrome else return False.

# Note: A string is said to be a palindrome if the reverse of the string is the same as the string itself.

def isPalindrome(s):
    for i in range(len(s)):
        if s[i] == s[i-1]:
            return True
    return False




# 5 : Write a program to return the mirror string for the given string.

def StringMirror(string):
          
    return string + string[::-1]     

 # 6 : Write a Python program to return a string from a given string s where all occurrences of the first char of the string except the first occurrence have been changed to '$'.

def change_char(s):
    res = ''
    
    for i in range(len(s)):
        if i == 0:
            res += s[0]
        elif s[i] == s[0]:
            res += '$'
        else:
            res += s[i]
    return res














    