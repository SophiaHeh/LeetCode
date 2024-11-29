nums = [5, 4, 2, 1, 6, 2, 5]
new_list = []
for num in nums:
    if num == 5:
        new_list.append(num)
        
#List Comprehension
new_list_other = [num for num in nums if num == 5]
list_diff_6 = [num for num in nums if num != 6]
list_if_else = [num if num == 5  else 0 for num in nums] #if  there are one more condition(such as if..else..), we should put condition in front of for lop
#list_if_else2 = [num if num == 5 for num in nums] #error
list_if_elif_else = [num if num == 5 else "yes" if num == 4 else 0 for num in nums] #超級重要, 可以拆成：（1）if num == 5 （2）else "yes" if num == 4(elif) (3)else 0 
print(list_if_elif_else)
#print(list_diff_6)