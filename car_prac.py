# class Car:
#     '''
#     Design of car
#     '''
#     def __init__(self, make: str, model: str, year: int, color: str, price: float, engine: str, features: list= []):
#         '''
#         Constructor of car
#         '''
#         self.make = make
#         self.model = model
#         self.year = year
#         self.color = color
#         self.engine = engine
#         self.features = features
#         self.price = self.update_price(price) #不能直接用self.price = price
#         #不然就不會呼叫update_price，那麼self.price就不會儲存最終的總價格
        
#     def update_price(self, price):
#         '''
#         Update price attribute if additional features are requested
#         '''
#         feature_to_price = {"leather_seats": 3000,
#                             "bullet_proof": 8000, "auto_pilot": 10000, "fly": 200000}
#         for feature in self.features:
#             price += feature_to_price[feature]
#         return price                    

#     def __str__(self):
#         '''
#         Modify str representation of Car
#         '''
#         return f"This car is a {self.make}, {self.model}, manufactured in {self.year}, which costs {self.price}"


# # car1 = Car("Tesla", "cybertruck", 2024, 'grey', 80000, 'the one with noise', [
# #            'leather_seats', 'bullet_proof', 'auto_pilot', 'fly'])

# car1 = Car("Tesla", "cybertruck",2024,'grey', 80000, 'the one with noise')
# car2 = Car("Tesla", "cybertruck", 2024, 'grey', 80000, 'the one with noise', [
#            'leather_seats', 'bullet_proof', 'auto_pilot', 'fly'])
    

# #這個版本的code是不論update_price()函數使用幾次，features不變的話，總價不會變
# print(car1)
# print(car2)
# print(car2.price)
# print(car2.price)
# print(car2.update_price(80000)) #其中update_price（）中的參數是放置a starting price(汽車的原價)
# print(car2.update_price(80000))
# print(car2.price)


# #版本2-老師講義上的版本，有bug,update_price()函數會使features上的價格疊加，因為沒有把update_price()函數寫在 __init__裡面
# import numpy as np
# class Car:
#     '''
#     Design of car
#     '''
#     def __init__(self, make, model, year, price, new_features):
#         '''
#         Constructor of car
#         '''
#         self.make = make
#         self.model = model
#         self.year = year
#         self.price = price
#         self.new_features = new_features
#         self.feature_prices = {"leather_seats": 5000, "speaker": 1000,"air_suspension": 10000, "new_color": 2000}
        
#     def update_price(self):
#         '''
#         Update price attribute if additional features are requested
#         '''
#         self.price += np.dot(self.new_features,np.array(list(self.feature_prices.values())))
                 

#     def __str__(self):
#         '''
#         Modify str representation of Car
#         '''
#         return "This car is a {} {} manufactured in {} costing {}.".format(self.make, self.model, self.year, self.price)
    
    
# car1 = Car("honda", "civic", 2010, 10000, np.array([1, 0, 0, 1]))
# car2 = Car("toyota", "camry", 2015, 25000, np.array([0, 1, 1, 0]))
# car1.update_price()
# car2.update_price()
# car2.update_price()
# print(car1)
# print(car2)

#版本3-自己想的-如果創建完car對象後，該car對象，有更新的feature,進而影響最終的price的話，該怎麼實現？
class Car:
    '''
    Design of a Car
    '''

    def __init__(self, make: str, model: str, year: int, color: str, price: float, engine: str, features: list = []):
        '''
        Constructor of the class Car

        Args:
            make: str indicating which company made the car
            model: str representing the model of the car
            year: int indicating in what year the car was manufactured
            color: str indicating the color of the car
            price: float indicating the price of the car
            engine: str indicating the type of engine
            features: list containing the additional features implemented to the car
        '''
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.engine = engine
        self.features = features
        self.base_price = price  # Store the base price separately
        self.price = self.update_price(price)

    def update_price(self, price):
        '''
        Update price attribute if additional features are requested
        '''
        feature_to_price = {"leather_seats": 3000,
                            "bullet_proof": 8000, "auto_pilot": 10000, "fly": 200000}
        for feature in self.features:
            price = price + feature_to_price.get(feature, 0)  # Avoid KeyError if feature is not in dictionary
        return price

    def add_features(self, new_features):
        '''
        Add new features to the car and update the price
        '''
        self.features.extend(new_features)  # Add new features to the existing list
        self.features = list(set(self.features))  # Remove duplicates
        self.price = self.update_price(self.base_price)  # Recalculate price based on base price and updated features

    def __str__(self):
        '''
        Modify str representation of Car
        '''
        return f"This car is a {self.make}, {self.model} manufactured in {self.year} which costs {self.price}"


# Example Usage
car1 = Car("Tesla", "cybertruck", 2024, 'grey', 80000, 'the one with noise', [
           'leather_seats', 'bullet_proof'])

print(car1)  # Initial car object
print("Initial price:", car1.price)

# Add new features
car1.add_features(['auto_pilot', 'fly'])
print(car1)  # Updated car object
print("Updated price:", car1.price)
