# open(name of the file, process to do)
# process to do, ex: 'w' (write some info)
# process to do, ex: 'r' (read data from file)

f = open('first_file.txt', 'w')
# file_io.py

f.write("Time Complexity is hard but fun\n")
f.write("I recommend listening to APT")
f.close()  # 這個是什麼功能？
