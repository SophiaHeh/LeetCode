# 7 line for one function

# function that sort the list
# divide the list into two half
# sort the list
# combine the list

def combine_list(list1, list2):
    i, j = 0, 0
    merged_list = []
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1

    return merged_list


def merge_sort(nums: list):
    '''
    Sort a list using merge sort

    Arg:
        nums: list of numbers
    Return:
        sorted version of nums
    '''
    n = len(nums)
    # m = (n+1) // 2
    # list1 = nums[:m]
    # list2 = nums[m:]

    # base case
    # print(n == 1) # find bug!!!
    if n == 1:
        return nums
    else:
        part1 = nums[:n//2]  # [0: int(n/2)]
        part2 = nums[n//2:]  # [int(n/2):]
        # print(part1)  # find bug!!!
        # print(part2)  # find bug!!!
        # assert(0 > 1)  # find bug!!!,assert之前代碼的都会执行
        sorted_part1 = merge_sort(part1)
        sorted_part2 = merge_sort(part2)
        return combine_list(sorted_part1, sorted_part2)


print(merge_sort([5, 2, 1, 8, 7, 11, 6, 3, 9]))

# funciton that combine the sorted list


# when n 等於 1的時候，我們可以確認time complexity 是2, one for n == 1的比較， one for return nums這個操作
