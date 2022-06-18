# https://gist.github.com/ajay2611/c3378bc78dda6af54a1cfd1960184140

# Input :

# input_list = ['red', 'blue', 'green&blue&yellow', 'pink', 'yellow&brown&red']

# Desired output :

# input_list = ['red', 'blue', 'green', 'blue', 'yellow', 'pink', 'yellow' 'brown', 'red']



def split_str(input_list):
    new_list = []
    for item in range(len(input_list)):
        start = 0
        for index, char in enumerate(input_list[item]):
            if char == '&':
                new_list.append(input_list[item][start:index])
                
                start += index+1
            
        new_list.append(input_list[item][start:index + 1])

    return new_list

split_str(input_list)