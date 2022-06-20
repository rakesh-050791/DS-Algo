# Input :

# input_list = ['red', 'blue', 'green&blue&yellow', 'pink', 'yellow&brown&red']


# Desired output :

# input_list = ['red', 'blue', 'green', 'blue', 'yellow', 'pink', 'yellow' 'brown', 'red']


# Solved without using .split()

def split_str(input_list):
    newList = []
    for item in range(len(input_list)):
        start = 0
        
        for index, char in enumerate(input_list[item]):          
            if char == '&':
                element = input_list[item][start:index]
                newList.append(element)
                start += index+1
                
        alnum_word = ''
        for element in input_list[item][::-1]:
            if element != '&':
                alnum_word += element
            else:
                break
        newList.append(alnum_word[::-1])
        
    return newList

split_str(input_list)