def insertion_sort(my_list):
    '''
    Sort a list using insertion sort
    Arg:
        my_list: list containning some numbers
    Return:
        my_list: list containning sorted numbers in ascending order
    
    '''
    for i in range(1, len(my_list)):
        val = my_list[i]
        j = i - 1
        while j >= 0 and my_list[j] > val:
            my_list[j + 1] = my_list[j]
            j -= 1
        my_list[j + 1] = val
    return my_list

my_list  = [5, 4, 3, 2, 1]
print(insertion_sort(my_list))
        