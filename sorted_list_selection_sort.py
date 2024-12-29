
# Find min value in some subpart of the list
# Swap the elements

def find_min(nums):
    '''
    Find minimum of nums
    Arg:
        nums: list of unsorted number
    Return:
        index_min: the index of min value of nums
    '''
    min_value = min(nums)
    return nums.index(min_value) #注意有個.index()的method
    #Time: O(N) ; 
    
    
def selection_sort(nums):
    '''
    Sort list using selection sort 
    
    Arg:
        nums: list containning unsorted numbers
    
    Return:
        nums: sorted version of the original list
    '''
    for i in range(len(nums)):
        index_min = find_min(nums[i:])
        nums[i], nums[index_min + i] = nums[index_min + i], nums[i]
    
    return nums
    #Time: O(n^2)
    #Space: O(1) memory(Auxiliary)
    
    
def sort(s):
    s = [10, 5, 2, 6, 7, 1, 3]
    for i in range(len(s)):
        for j in range(s[i+1:]):
            if s[i] < s[j]:
                s[i], s[j] = s[j], s[i]
    return s

            
            

            
            