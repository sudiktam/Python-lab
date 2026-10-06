class HR:
    def __init__(self,name, dob, salary, skill_sets):
        self.name = name 
        self.dob = dob 
        self.salary = salary 
        self.skill_sets = skill_sets

    def get_age(self):
        age = 2026 - self.dob
        return age 


class Employee(HR):
    def __int__(self,name, dob, salary, skill_sets,is_manager, onboard_rate):
        super().__init__(self,name, dob, salary, skill_sets)
        self.is_manager = 

