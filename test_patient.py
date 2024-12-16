import unittest
from patient import Patient


class TestPatient(unittest.TestCase):
    '''
    Design to test the class Patient
    '''

    def setUp(self):
        '''
        Method that allows me to initialize some test cases for Patient

        '''
        self.patient1 = Patient('Nadim', 68, 'Man', 'Broken wrist',1218658, False)

    def test_init(self):
        '''
        Method to test the constructor
        '''
        ID = 1218658
        self.assertEqual(self.patient1.ID, ID, "The  attribute make is initialized incorrectly")  # 第三個參數是信息
    

unittest.main()

#為何我使用unittest.main() 在終端出現的結果會打印出ID號碼呢？此外. 這個句號是表示什麼是setUp函數執行完後會返回的結果，還是執行完test_init函數執行完後的結果？
#解釋：https://chatgpt.com/share/675357c7-5238-8001-a1eb-679cb9a4794b
