'''
Write some code with computes the prerimeter of a rectangle for 1 = 2, w = 5.2
'''

length = 2
width = 5.2
perim_rectangle = 2*(length + width)
#print(perim_rectangle)


def compute_perim_rect(length, width):
    '''
    Compute perimeter of any rectangle # keep only one line
    
    Args: 
        length: float representing the length of rectangle
        width: float representing the width of rectangle 
    Return:
        perim_rect: float representing the perimeter of a 
            rectangle 
    # can add more comment if needed so first line try to keep one line      
    '''
    perim_rect = 2*(length + width)
    return perim_rect # return 2*(length + width) 這個也可以！ 推薦！ 因為不用多存一個variable

#perim_rect_ex1 = compute_perim_rect(3, 5.2)
#print(perim_rect_ex1)

def compute_perim_area(length: float, width: float):
    '''
    Compute perimeter and area for any rectangle
    Args: 
        length: float representing the length of rectangle
        width: float representing the width of rectangle 
    Return:
        perim_rect: float representing the perimeter of a rectangle 
        area_rect: float representing the area of a rectangle
    
    '''
    perim_rect = 2*(length + width)
    area_rect = (length * width)
    return perim_rect, area_rect # create tuple by default 所以加不加()都可以，return結果是一樣的

print(compute_perim_area)
print(compute_perim_area(4.1, 7.2))
perim_rect, area_rect = compute_perim_area(4.1, 7.2) #unpacking
print(perim_rect)
print(area_rect)

