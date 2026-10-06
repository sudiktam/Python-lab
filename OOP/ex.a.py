class Employee:
    def __init__(self,name, dob, salary, skill_sets):
        self.name = name 
        self.dob = dob 
        self.salary = salary 
        self.skill_sets = skill_sets

    def get_age(self):
        age = 2026- self.dob
        return age

ram = Employee("Ram", 2004, 50000, ["Python", "Java"])
print(ram.get_age())

class Developer(Employee):
    def __init__(self,name, dob, salary, skill_sets,git_hub,is_fullstack):
        super().__init__(name, dob, salary, skill_sets)
        self.git_hub = git_hub
        self.is_fullstack = is_fullstack

    def get_profile(self):
        skill_names = ', '.join(self.skill_sets)
        profile = f"{self.name} has skills {skill_names}. GitHub: {self.git_hub}, Fullstack: {self.is_fullstack}"
        return profile

ram = Developer("ram", 2000, 60000, ["Python", "JavaScript"], "https://github.com/ram", True)
print(ram.get_profile())