import unittest
from car import Car
#第一個car 是file 的意思嗎？
#setUp函數的解釋：https://chatgpt.com/share/67529fa0-331c-8001-9837-8d392378b780 

class TestCar(unittest.TestCase):
    '''
    Design to test the class Car
    '''
    def setUp(self): #類似於__init__函數
        '''
        Method that allows me to initialize some test cases for Car
        
        '''
        self.car1 = Car("Tesla", "cybertruck", 2024, "grey", 80000, 'the one with noise', [
           'leather_seat', 'bullet_proof', 'autopilot', 'fly'])
        
    def test_init(self):
        '''
        Method to test the constructor
        '''
        make, model = "Tesla", "cybertruck"
        self.assertEqual(self.car1.make, make, "The  attribute make is initialized incorrectly")#第三個參數是信息
        self.assertEqual(self.car1.model, model, "The attribute model is initialized incorrectly")

    def test_update_price(self):
        '''
        Method to test the update_price method
        '''
        price = 301000
        self.assertEqual(self.car1.price, price, "The price is not computed correctly")
    
#這裡的main是什麼意思    
unittest.main()
        
        