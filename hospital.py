class Hospital():
    '''
    Design of Hospital
    '''

    def __init__(self, name: str, location: str, departments: list, zipCode: int, staff: list, patients: list = []):
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
        self.departments = departments
        self.zipCode = zipCode
        self.staff = staff
        self.patients = patients

    def admit(self, patient):
        '''
        Admint a new patient to the hospital

        Arg:
            patient: Patient representing a new Patient joining the hospital

        '''
        #how about use if patient in self.patients? ans：不建議，這個方法是based on "object reference"但因為後期test的時候容易遇到同ID的病人但是屬于不同的object reference，會和我們的預期效果不一致，我們認為同一個ID就是同一個病人
        if patient.ID in self.get_IDs_patients():  # ()? ans:使用括號是因為呼叫函數，該函數會返回list
            print("Patient is already admitted")
        else:
            self.patients.append(patient)
            #should we need to import Patient class first? ans: yes
            patient.admitted = True  # ?? #因為儲存的是patient 這個object,所以可以access 到admitted 這個attributes

    def get_IDs_patients(self):
        '''
        Return a list of the patient IDs

        '''
        return [p.ID for p in self.patients]  # a list of object type patient
    
    def admit_from_list(self, patient_list: list):
        '''
        Admit many patient at once
        Arg:
            patient_list: list containning the patients to be admitted
        '''
        for p in patient_list:
            self.admit(p)
            
     def discharge(self, patient):
        '''
        Discharge a patient from the hospital
        
        Arg:
            patient: Patient that will be discharged
        '''
        if patient.ID in self.get_IDs_patients():
            self.patients.remove(patient) #remove 是remove object,會依據object reference
            patient.admitted = False
        
        else:
            print('Patient was already discharged')
    
    #所以如果是同名的病人，其在這個case中的ID是一樣的，所以可以進入 if patient.ID in self.get_IDs_patients():這個if statement，
    # 但是在remove 這個環節會出錯，因為remove是remove object不是ID,而在這個testcase中 同名的病人會初始化成不同的object reference,所以會在remove 環節跳出error
    
    #remove 和pop的區別：https://chatgpt.com/share/675363d0-1528-8001-a7c0-4af98e2bb2b4 
    #class Hospital(): 和class Hospital： 都可以 
    #解釋：https://chatgpt.com/share/67535fa4-983c-8001-8e94-ed21477f31bb
    