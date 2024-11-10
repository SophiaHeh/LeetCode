'''
Printing elements of a list
'''
list_nums = [5, -2, 6, 7, 1, 5, 4, 3]

# representation 1 and representation2 represents the same output

# representation 1: go over each position in len(list_nums)
# for i in range(len(list_nums)):
#     print(list_nums[i])

# representation 2 :go over each element in list_nums
# for num in list_nums:
#     print(num)


def count_occurence_number(num: int, list_nums: list):
    '''
    Count occurence of num in list_nums

    Args:
        num: int representing the number we are counting
        list_nums: list containing all the numbers

    Return:
        count: int representing the number of occurences of num
    '''
    count = 0
    for i in list_nums:
        if i == num:
            count += 1
    return count


example_nums = [6, 9, 7, 11, 31, 10, 24, 1024, 10, 31, 31, 4]

num = 12

print(count_occurence_number(31, example_nums))


def compute_factorial(n: int):
    '''
    Compute factorial of n 

    Args:
        n: int reprenting the input for which we compute its factorial

    Return:
        fact: int representing the factorial of n 
    '''
    if n < 0:
        #print("STOPPP NO NEGATIVE")
        return "STOPPP NO NEGATIVE"
    else:
        fact = 1
        for i in range(1, n+1):
            fact = fact * i
        return fact


print(compute_factorial(0))  # try n = 5, -5, 0
