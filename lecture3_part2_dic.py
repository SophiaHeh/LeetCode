'''
Create Dictionaries
'''

dict_movie = {"Nadim": "Harry", "Charlene": "Interstellar", "Tyler": "The Prestige", "CS5001": 2.75, "hi": {2: "yay"} }
charlene_fav_movie = dict_movie["Charlene"]
print(charlene_fav_movie)

#key in dict only can put 不可變data type, 但是value can put both 可變和不可變的data type
#所以"hi": {2: "yay"} 是對的， 但是{1: "woohoo"}: 2}是錯的
#Note: every key only can map only one value
