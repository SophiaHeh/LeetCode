# class: decide what the thing will look like(design)
# function within a class is called a method
# def __init__ 是一種dundres, dundres 都包含self字眼
# def __str__ is a string representation, is also a dundres
class Food:
    '''
    Design of Food
    '''
    # self 是什麼意思？
    # Method (function within a class)
    # function of __init__是一個特別的函數，可以讓我initialize attributes
    # 注意函數定義的參數如果設有初始值,initialized value的話，必須放在最後面，不然會報錯！
    # 例如：color_broth和texture_broth要放在最後！

    def __init__(self, name: str, taste: str, price: float, ingredients: list, edible: bool, texture: str,
                 color_broth: str = None, texture_broth: str = None):
        '''
        Consructor  of Food
        Initialize the attributes of an object of type Food
        #attribute: variable within a class
        '''
        # Attributes of a class (variables within a class)
        self.name = name
        self.taste = taste
        self.price = price
        self.ingredients = ingredients
        self.edible = edible
        self.texture = texture
        self.color_broth = color_broth
        self.texture_broth = texture_broth

    def __str__(self):  # 如果不加self於參數位置的話，會出現error
        '''
        Mofify str representation of a Food object
        '''
        return f"This is a {self.name}"


hot_pot = Food('hot_pot', 'spicy', 50,  [
               'tofu', 'mushrooms', 'potato', 'pork', 'beef strip', 'lamb'], True, 'anything', 'red', 'liquid')
fried_chicken = Food('fried_chicken', 'spicy', 20, [
                     'chicken', 'flour', 'cheese', 'onion', 'oil'], True, 'crispy')

# print(fried_chicken.ingredients)
# print(hot_pot.color_broth)
# print(hot_pot.taste)
# print(hot_pot.ingredients)


# fried_chicken.ingredients =['chicken, 'flour', 'cheese', 'onion', 'oil']
# fried_chicken.price = 20
# fried_chicken.texure = 'cripsy'
# print(fried_chicken.price)

print(fried_chicken)
print(hot_pot)
