#Q1
id_number = {'NU42521', 'NU49284', 'NU94284', 'NU39204', 'NU69482'}
#print(id_number)


id_number.add('NU42521')
id_number.add('NU49284')
id_number.add('NU94284')
id_number.add('NU39204')
id_number.add('NU69482')
id_number.add('NU37492')
id_number.add('NU20384')
id_number.add('NU37582')
id_number.add('NU81736')
id_number.add('NU72837')
print(id_number)

#Q2.
my_set1 = {3, 5, 1, 7}
my_set2 = {7, 3}
print(7 in my_set1 and 3 in my_set2 )

#Q3.
my_tuple = (4, 2, 5, 2)
list_1 = list(my_tuple)
print(list_1)
list_1[2] = 6
print(list_1)
my_tuple = tuple(list_1)
print(my_tuple)


#Q4.
my_dict = {"John": "Yellow", "Kaleigh": "Red", "Priya": "Blue", "Jad": "Green"}
key_dict = list(my_dict.keys())
values_dict = list(my_dict.values())
print(key_dict)
print(values_dict)

#Q5.
def quadratic_solver(x: list):
    a, b, c = x
    discriminant = (b**2 - (4*a*c))**(0.5)
    result_1 = (-b + (discriminant)) / (2*a)
    result_2 = (-b - (discriminant)) / (2*a)
    return {result_1, result_2}
print(quadratic_solver([2, -4, -6]))

#@6. Summary:
# 1. We have learned how to make good use of set ti avoid duplication
# 2. use in syntax in to check whether a variable belongs to a set
# 3. Notice that tuple is immutable and we learned how to convert tuple into list and vise versa.
# 4. We have learned key method and values method to convert dictionary into list
# 5. 