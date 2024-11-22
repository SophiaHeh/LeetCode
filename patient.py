class Patient():
    '''
    Design of Patient
    '''

    def __init__(self, name: str, age: int, gender: str, condition: str, ID: int, admitted: bool):
        '''
        Constructor of the class Patient

        Args:
            name: str indicating patient's name
            age: int representing patient's age
            gender: str indecating patient's gender
            condition: str indecating patient's condition
            ID: int indicating the price's ID
            admitted: bool indicating patient's admitted status

        '''
        self.name = name
        self.age = age
        self.gender = gender
        self.condition = condition
        self.ID = self.set_ID(ID)
        self.admitted = admitted

    def set_ID(self, ID):
        '''
        Setting the value of the attributes ID, if it is a valid one
        '''
        if type(ID) != int:
            print("Invallid ID, try again")
            return
        str_ID = str(ID)
        if len(str_ID) != 7:
            print('Invalid ID, try again')
            return  # 代表是return nothing(none), 錯誤的ID就不會被記錄
        else:
            for i in range(3):  # loop 三次就好
                if int(str_ID[i]) > 3:
                    print("Invalid ID, try again")
                    return
            print("Yay, valid ID")
            return ID


# guarantee to be positive integer?


# length does not work with integer, only work with str and list

nadim = Patient('Nadim', 68, 'Man', 'Broken wrist', 1718658, False)


print(nadim.ID)
