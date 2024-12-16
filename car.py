
# 問一下self到底是什麼？？
#ans:https://chatgpt.com/share/67525f50-8c30-8001-acd7-ee7b780ea505

class Car():
    '''
    Design of Car

    '''

    def __init__(self, make: str, model: str, year: int, color: str, price: float, engine: str, features: list):
        '''
        Constructor of the class Car

        Args:
            make: str indicating which company made the car
            model: str representing the model of the car
            year: int indecating in what year the car was manufactured
            color: str indecating the color of the car
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
        # ** why put features before price?  ans: because 先有features才能執行update_price（）
        self.price = self.update_price(price)
        # Write a function which updates the price of the car if it were to have additional features

    def update_price(self, price):
        '''
        Update price attribute if additional features are requested
        '''
        feature_to_price = {"leather_seat": 3000,
                            'bullet_proof': 8000, 'autopilot': 10000, 'fly': 2000000}

        for feature in self.features:
            price = price + feature_to_price[feature]
        return price
        # return self.price  這一行不需要！

        # Write a str representation  under which will include the updated price of the car
    def __str__(self):
        '''
        Modify str representation of Car
        '''

        return f"The car is a {self.make}, {self.model} manufactured in {self.year} which costs {self.price}"


car1 = Car("Tesla", "cybertruck", 2024, "grey", 80000, 'the one with noise', [
           'leather_seat', 'bullet_proof', 'autopilot', 'fly'])
print(car1)

# 如果call function 的話，不要加在def __str__,否則每次打印都會call function,有可能出錯
# 最好在def __init__ 裡面call function

# class is the design of a data type that you want to create

# object is the instance of a class
# ex:
# str  -> class
# a = 2 -> object
# [2,3,4,5,6] -> object
# tuple -> class
