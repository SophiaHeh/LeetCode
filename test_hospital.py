import unittest
from hospital import Hospital  # from file name import specific class
from patient import Patient

# inherit TestCase class, that include many method for you to test


class TestHospital(unittest.TestCase):  # inherit TestCase class
    '''
    Testing the Hospital class
    '''

    def setUp(self):
        '''
        Initialize some test case
        '''
        self.northeastern_hospital = Hospital('Northeastern', 'San Jose', ['ER', 'HR', 'Gastro', 'ICU'], 95120, ['Yarina', 'Xinyi', 'Sophia', 'Rache'], [])  # 最後[]是代表每一次初始化為empty list,這個[]代表patients list; patients: list=[]這種寫法是默認值的寫法，如果patients沒有值的話就設為empty list，但是如果有數值的話就會直接使用不會
        # 為何不用self.nadim? ans:https://chatgpt.com/share/6753b783-ab24-8001-bf79-cee59304c42d 
        nadim = Patient('Nadim', 68, "Man", "Broken wrist", 128658, False)
        midan = Patient('midan', 76, "Man", "Broken wrist", 128658, False)
        adnim = Patient('adnim', 50, "Man", "Broken wrist", 128658, False)
        # 這裡的self 是TestHospital class 的object
        self.patients_test = [nadim, midan, adnim]
        # 為何這裡的創建的patient 不使用self呢？ 是不是因為Hospital class中本身就沒有patient這個attribute 只有patients這個attribute的原因嗎？ ans:https://chatgpt.com/share/6753b783-ab24-8001-bf79-cee59304c42d

    # northeastern_hospital 是TestHospital class中的attributes,這個attributes的data type是Hospital
    # 這裡的self都是TestHospital的object，因為我們在class TestHospital中定義的
    # 每次run test method的時候都會先run setUP()函數
    # run test method的次序是按字母順序(從a開始)

    def test_init(self):
        '''
        Test constructor
        '''
        name = "Northeastern"
        location = "San Jose"
        departments = ["ER", "HR", "Gastro", "ICU"]
        zip_code = 95120
        staff = ["Yarina", "Xinyi", "Sophia", "Rachel"]
        self.assertEqual(name, self.northeastern_hospital.name, "Name is incorrect")
        self.assertEqual(location, self.northeastern_hospital.location, "Location is incorrect")
        self.assertEqual(departments, self.northeastern_hospital.departments, "Departments are incorrect")
        self.assertEqual(zip_code, self.northeastern_hospital.zip_code, "Zip code is incorrect")
        self.assertEqual(staff, self.northeastern_hospital.staff, "Staff is incorrect")

    def test_admit(self):  # 測試這個的時候剛剛3個病人不是已經初始化了嗎ans:在setUp初始化的只會影響TestHospital的object的屬性但是不會影響northeastern_hospital這個hospital object的屬性
        '''
        Test admit method
        '''
        self.northeastern_hospital.admit(self.patients_test[2]) #adnim
        self.assertEqual(1, len(self.northeastern_hospital.patients))
        self.northeastern_hospital.admit(self.patients_test[2])
        self.assertEqual(1, len(self.northeastern_hospital.patients))
        

    def test_admit_from_list(self):  # 測試時的函數順序？ans: 字母順序
        '''
        Test admit_from_list() method
        '''
        self.northeastern_hospital.admit_from_list(self.patients_test) #patients_test有三個病人
        self.assertEqual(3, len(self.northeastern_hospital.patients))
        self.northeastern_hospital.admit_from_list(self.patients_test)
        self.assertEqual(3, len(self.northeastern_hospital.patients))

   def test_discharge(self):
        '''
        Test discharge method
        '''
        self.northeastern_hospital.admit(self.patients_test[0]) #why we need to admit first? instead of check whether inside the list?
       # 在initialize patient的時候是否已經initialize 3位patient了？？ 不是，initialize hospital的時候，patients會初始為[]
        self.assertEqual(1, len(self.northeastern_hospital.patients), f"Number of patients is incorrect, the hospital has {len(self.northeastern_hospital.patients)}")
        self.northeastern_hospital.discharge(self.patients_test[0])
        self.assertEqual(0, len(self.northeastern_hospital.patients), f"Number of patients is incorrect, the hospital has {len(self.northeastern_hospital.patients)}")
        # print(len(self.northeastern_hospital.patients))
       
      
       
# evertime I call test it will call setup() again!

unittest.main()

# set_up -> test_admit -> set_up -> test_init
# 為何 test的時候會呼叫def set_ID(self, ID)？  ans: 这来自 patient.py 的代码。创建 nadim 对象时，调用了 set_ID()
# 每一次test 新的method之前，會先運行setUp method,每一次setUp(self)都會重新創建3個patient object
# 每一次呼叫def setUp(self)會打印出"Yay, valid ID"三次因為上面創建了
# nadim = Patient('Nadim', 68, "Man", "Broken wrist", 128658, False)
# midan = Patient('midan', 76, "Man", "Broken wrist", 128658, False)
# adnim = Patient('adnim', 50, "Man", "Broken wrist", 128658, False)
# 每次set up 會創建新的三個病人，新的reference number
# admin method 是使用ID 去識別需不需要加入病人，也就是說一個病人重建的時候有相同的ID但是有不同的object reference
# 不懂def test_discharge(self)函數中的self.patients_test[0]代表什麼意思？為何用index 0? ans:因為是加入patients_test這個list中的第一個patient
# 不懂def test_discharge(self)函數內部是如何執行導致它能識別出要dischage 的nadim其對應的object reference 
# when testing method is done will show a '.'

#在setUp中， nadim = Patient('Nadim', 68, "Man", "Broken wrist", 128658, False)和
# self.nadim = Patient('Nadim', 68, "Man", "Broken wrist", 128658, False)的區別：
#https://chatgpt.com/share/6753b783-ab24-8001-bf79-cee59304c42d (有self -> 实例变量);
#沒有self -> 局部变量, 不論哪一個都會在執行任何一個測試method之前被初始化