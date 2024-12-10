'''
Sets, tuples, list
'''
#my_set = {"Monday", "numbers", 32, True, 3.14, 1} #True 和 數字1 是一樣的，所以set只會展現一個


my_set = {"Monday", "numbers", 32, True, 3.14, int(float("1.2"))} #注意 int()會無條件省略小數點
my_set.add("enchanted")
my_set.remove("numbers")
my_set.add("numbers")
my_set.remove("numbers")
print(my_set)
#print(len(my_set))

#* note: tuple
# order: does  matter (no change in my collection)
# duplicate: are allowed 

my_tuple = ("love story", "welcome to new york", "cool summer", "blank space", 9427249)
#can not modify element of tuple
#my_tuple[2] = "shake it off"
#print(my_tuple[2])
#print(type(my_tuple)) #tuple cannot add or remove or any changes

#* note: List
# order: does  matter (can change in my collection)
# duplicate: are allowed 

my_list = ["summertime sadness", "blue jeans", "last for life", False, 12.31]
my_list[3] = "young and beautiful'"
print(my_list[-1])
print(my_list)
print(type(my_list))
