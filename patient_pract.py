class Patient:

    '''
    Design a patient
    '''

    # __init__是初始化的函數，只會自動運行一次是什麼意思？
    def __init__(self, name: str, age: int, gender: str, condition: str, ID: int, admitted: bool):
        '''
        Constuctor of patient
        Args:
            name: str representing the name of the Patient
            age: int representing the age of the Patient
            gender: str representing the gender of the Patient
            condition: str representing the condition of the Patient
            ID: int representing the ID of the patient
            admitted: bool indicating whether the patient is admitted to a hospital

        '''
        self.name = name
        self.age = age
        self.gender = gender
        self.condition = condition
        # self.set_ID(ID) 是呼叫類別中的函數 set_ID 的動作。；# 初始化時使用 set_ID 進行驗證
        self.ID = self.set_ID(ID)
        self.admitted = admitted

    def set_ID(self, ID):  # 為何參數需要ID, 而不是在函數內直接使用self.ID?
        '''
        Setting the value of the attribute ID, if it is a valid one
        '''
        if type(ID) != int:
            print("Invalid ID, try again")
            return

        str_ID = str(ID)

        if len(str_ID) != 7:
            print("Invalid ID, try again")
            return
        else:
            for i in range(3):
                if int(str_ID[i]) > 3:
                    print("Invalid ID, try again")
                    return
            print("Yay, valid ID")
            return ID


nadim = Patient("Nadim", 68, "Man", "broken wrist", 1218658, False)
print(nadim.ID)


# 備註：__init__ 在對象實例化時自動執行一次，之後不會自動再次調用，除非你手動顯式地調用它
# https://chatgpt.com/share/674d484c-a930-8001-92af-80b4f815244c
