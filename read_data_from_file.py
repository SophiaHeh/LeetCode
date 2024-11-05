f = open('first_file.txt', 'r')
info = f.read()
f = open('first_file.txt', 'r')

'''
If you try to read again, you will get an empty string as the cursor would 
be at the end of file (if you already ran f.read() once before)
'''
info2 = f.read()
# print(info)
print(info2)
f.close()
