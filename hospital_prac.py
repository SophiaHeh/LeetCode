class Hospital:
    '''
    Design of a hospital
    '''
    def __init__(self, name: str, location: str, department:list, zipCode: int, staff: list, patients: list = []):
        '''
        Constructor of the class Hospital

        Args:
            name: str indicating hospital's name
            location: str representing Hospital's location
            departments: str indecating Hospital's departments
            zipCode: int indecating Hospital's zipCode
            staff: list indecating Hospital's staffs
            patients: list indecating Hospital's patients, patient is an patient object


        '''
        self.name = name
        self.location = location
        self.department = department
        self.zipCode = zipCode
        self.staff = staff
        self.patients = patients
        
    def admit(self, patient): #此時的patient 是？接收外部傳遞回來的參數？ 注意：patient這個參數是一個patient的data type,一個patient的object
        '''
        method
        '''
        if patient.ID in self.get_IDs_patients():  #注意，一定要記得()，不然沒有呼叫函數，無法返回list
            print('patient is already in the hospital')
        
        else:
            self.patients.append(patient)
            patient.admitted = True
        
    def get_IDs_patients(self):
        '''
        Return a list of the patient IDs
        '''
        return [p.ID for p in self.patients]
    
    
    def admit_form_list(self, patient_list: list):
        '''
        Admit many patients at once
        Args:
            patient_list: list containing the patients to be admitted
        '''
        for p in patient_list:
            self.admit(p)
            
    def discharge(self, patient):
        if patient.ID in self.get_IDs_patients():#注意，一定要記得()，不然沒有呼叫函數，無法返回list
            self.patients.remove(patient)
            patient.admitted = False
            
        else:
            print("Patient was already discharged")
                 
    #此時的patient 是？接收外部傳遞回來的參數？
    #ans: 
    #patient 作為 admit 方法中的參數，僅代表外部傳入的 Patient 對象，與 Hospital 類內部屬性（如 self.patients）沒有直接的關係