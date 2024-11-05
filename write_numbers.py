with open('file_numbers.txt', 'w') as f:
    f.write(str([1, 2, 3]))

with open('file_numbers.txt', 'r') as f_read:
    data = f_read.read()

'''
storing lists would require us to convert it to a str. Converting 
the str back to a list seperates every character of the string into one 
element of the list
we'll explore another function that can handle list/arrays better
'''

print(list(data))

