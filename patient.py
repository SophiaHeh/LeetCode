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
            ID: int indicating the patient's ID
            admitted: bool indicating patient's admitted status

        '''
        self.name = name
        self.age = age
        self.gender = gender
        self.condition = condition
        # 不太懂這個設定，是不是因為這裡設定為self.set_ID(ID)後續set_ID 函數的參數才有ID;
        # self.set_ID(ID) 是呼叫類別中的函數 set_ID 的動作。；# 初始化時使用 set_ID 進行驗證
        self.ID = self.set_ID(ID) #初始化期間就確認是否是valid ID, 是的話，才加入進去
        self.admitted = admitted

    def set_ID(self, ID):  # 不懂參數ID是怎麼獲取的？？ ans:https://chatgpt.com/share/6744e64e-04f0-8001-b2bf-6909ae8397f3
        '''
        Setting the value of the attributes ID, if it is a valid one
        '''
        if type(ID) != int: #先轉換成str and list 才可以使用length, int 不能使用list
            print("Invallid ID, try again")
            return
        str_ID = str(ID)
        if len(str_ID) != 7: # length does not work with integer, only work with str and list
            print('Invalid ID, try again')
            return  # 代表是return nothing(none), 錯誤的ID就不會被記錄
        else:
            for i in range(3):  # loop 三次就好
                if int(str_ID[i]) > 3: #注意是要先轉換回integer才能比較大小;#必須是 int 和int 比大小; 注意：int 本身是是不可迭代的，因此它沒有索引（index的概念，但是由於我們需要index去定位前3個數值，因此得用str type，然後比對大小的時候再轉換為int
                    print("Invalid ID, try again")
                    return
            #print("Yay, valid ID")
            return ID


# guarantee to be positive integer?

#****重點
# length does not work with integer, only work with str and list
#len() 函數是專門用於測量可迭代對象（例如字符串、列表、元組或字典）的長度，而整數不是可迭代對象，因此無法直接使用 len() 函數。
#在 Python 中，整數（int）數據類型是 不可迭代的，因此它 沒有索引（index） 的概念(https://chatgpt.com/share/6753508f-f29c-8001-9c7e-9cd8ca87dafd)

nadim = Patient('Nadim', 68, 'Man', 'Broken wrist',1218658, False)
print(nadim.ID)


# if __name__ == "__main__":
#     nadim = Patient('Nadim', 68, 'Man', 'Broken wrist', 1218658, False)
#     print(nadim.ID)
