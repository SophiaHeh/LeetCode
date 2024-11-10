import numpy as np

roll1 = np.array([2, 5, 6, 4, 3])  # 記得提供list數列格式的參數
roll2 = np.array([4, 1, 3, 5, 2])


num_tosses = 1000000
toss_coin = np.random.randint(0, 2, num_tosses)

# np.random.randint
#toss_coin = np.random.randint(0, 2, 6)
# print(toss_coin)
print(roll1+roll2)

count_heads = 0

for num in toss_coin:
    if num:  # if  num == 1:
        count_heads += 1  # [1 1 0 0 1 0 ] becomes 3
print(count_heads)


# np.sum()用來對數組（或矩陣）中的元素進行加總操作。這個函數可以作用於多維數組，並允許沿著指定的軸進行加總。
count_heads_other = np.sum(toss_coin)

# print(toss_coin)
# print(count_heads/num_tosses) #Need check, calculate probability
# print(count_heads)
# print(count_heads_other)


# roll two dice

# 我的numpy版本和pro不同
# numpy : machine learning use numpy a lot
