
# def __str__ is a string representation, is also a dundres
class Food():
    '''
    Design of Food
    '''

    def __init__(self, flavor, texture, name):
        '''
        Constructor of Food

        Args:
            flavor:
            texture:
            name:

        '''
        self.flavor = flavor
        self.texture = texture
        self.name = name


hot_pot = Food()
