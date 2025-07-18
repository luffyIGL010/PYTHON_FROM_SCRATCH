class Employee:
    def __init__(self,salary,name,Work_Experience):
        self.salary=salary
        self.name=name
        self.Work_Experience=Work_Experience
    
    
    def get_salary(self):# self is the way to refer the objects of a given class>>>>>
        return self.salary
    
    def user_info(self):
        print(f"The name of the employee is {self.name},His salary is {self.salary} and working for {self.Work_Experience}")

e_1=Employee(45000,"Saurav",4)
print(e_1.get_salary())
e_1.user_info()