with open('first_file.txt', 'r') as f:  # it close for you automatcally
    line1 = f.readline()  # read line one by one
    line2 = f.readline()
print(line1)  # 為何不用重新read仍會有結果??
# ans: 因為需要重新read的是使用function read，function print不會，
# line1 這個結果已經儲存起來了(line1 = f.readline()), print只是打印這個結果
print(line2)
