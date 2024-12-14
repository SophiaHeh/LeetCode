import pandas as pd
import numpy as np

data = pd.read_csv('classification_data.csv')
data_cleaned = data.iloc[1:, 1:]  # 是row, colummn的順序
# print(type(data_cleaned))
data_cleaned = np.array(data_cleaned)
rows, cols = data_cleaned.shape

# print(data_cleaned)

# Count the number of accepted perfume that have a concentrated x1 = 1


# (法2)--老師方法
def count_product_x_val(x_val, status_product, col_val):
    '''
    Count number of products with x_{col_val} = x_val, either accepted
    or rejected

    Arg:
        x_val: int representing the concentration of x

        status_product: bool representing whether the peoduct is accepted
        or not
        col_val: int representing the chemical product in consideration
                which should be {1,2,3,4,5}

    Return:
        int representing the number of products 
        satisfying x_{col_val} = x_val depending on status_product
    '''
    count = 0
    for i in range(rows):
        # if data_cleaned[i, 0] == 1 and data_cleaned[i: -1]:
        # 注意是[,] 而不是[][]格式
        if data_cleaned[i, col_val-1] == x_val and data_cleaned[i, -1] == status_product:
            count += 1
    return count


# 注意col_val-1 要減1
def generate_count_x(col_val):
    '''
    Generate list containing number of product for different values
    of x_val for a specific column


    Arg:
    col_val: int representing the chemical product in consideration
                which should be {1,2,3,4,5}

    Return:
        list containing the count of x_{col_val} = x_val for 
        x_val = {1,2,3,4,5}

    '''
    count_x = [0] * 5
    for x_val in range(1, 6):
        # 中間參數的1是accepted 情況
        count_x[x_val - 1] = count_product_x_val(x_val, 1, col_val)

    return count_x


vals_col1 = generate_count_x(1)
print(vals_col1)
# [927, 821, 920, 652, 882] 代表的意思？是不是x1 的concentration 1 to 5?


'''
Checking the correctness of the code
'''


def generate_table(rows: int = 6, cols: int = 5):
    '''
    Generate matrix containning the count of accepted products satisfying 
    xi = j, for i = 1,....6 and j = 1,...,5

    Return:
        2D numpy array with the counts
    '''
    # 因為np.zeros（）只能接受一個參數，所以我只能以tuple的形式傳入
    table_count = np.zeros((rows, cols))
    for i in range(1, rows+1):  # i represent col_val, which x I choose
        for j in range(1, cols+1):  # j represent x_val, the concentration
            table_count[i-1, j-1] = count_product_x_val(j, 1, i)

    return table_count


table_count = generate_table()
print(table_count)

'''
    [ 1 2 3 4 5 
     x1
     x2
     x3
     x4
     x5
     x6   

    ]
    '''


sum_all = 0
for i in range(1, 6):  # 範圍是x1到x5
    for j in range(2):  # 只有0和1的結果
        sum_all += count_product_x_val(i, j, 2)

print(sum_all)
#print(count_product_x_val(1, 1))
print(count_product_x_val(1, 1, 2))

# data_cleaned[i, -1] == 1 可以寫成data_cleaned[i, -1]


# (法1)
# count = 0

# for i in range(len(data_cleaned)):
#     if data_cleaned.iloc[i, 0] == 1 and data_cleaned.iloc[i, 6] == 1:
#         count += 1

# print(count)
# （法3）--朋友


# def count():
#     data = pd.read_csv('classification_data.csv')
#     data_cleaned = data.iloc[1:, 1:]
#     # there are "NaN" in our original dataset, we don't want them.
#     # So we use list slicing to choose the start and end point for our desired dataset.
#     data_cleaned = np.array(data_cleaned)
#     # Transform a table into 2-D numpy array

#     res = 0
#     for i in range(len(data_cleaned)):
#         if data_cleaned[i][0] == 1 and data_cleaned[i][-1] == 1:
#             res += 1
#     return res


# print(count())
