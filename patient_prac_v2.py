class Patient:
    '''
    Design of Patient
    '''
    def __init__(self, name: str, age: int, gender:str, condition: str, ID: int, admitted: bool):
        '''
        Constructor of Patient

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
        self.ID = self.set_ID(ID) #初始化期間就確認是否是valid ID, 是的話，才加入進去
        self.admittted = admitted
    
    def set_ID(self, ID):
        '''
        Setting the value of the attribute ID, if it's a valid one
        '''
        if type(ID) != int: #先轉換成str and list 才可以使用length, int 不能使用list
            print("Invalid ID, try again")
            return 
        str_ID = str(ID)
        if len(str_ID) != 7:
            print("Invalid ID, try again")
            return
        else: 
            for i  in range(3):
                if int(str_ID[i]) > 3: #必須是 int 和int 比大小; 注意：int 本身是是不可迭代的，因此它沒有索引（index的概念，但是由於我們需要index去定位前3個數值，因此得用str type，然後比對大小的時候再轉換為int
                    print("Invalid ID, try again")
                    return 
            print('Yay, valid ID')
            return ID                 
            
nadim = Patient('Nadim', 68, 'man', 'broken writst', 1238467, False)
JJ = Patient('JJ', 68, 'man', 'broken writst', 1278467, False)
print(nadim.ID)
print(JJ.ID)
        
    
        