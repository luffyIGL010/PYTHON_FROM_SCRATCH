#Classe:Class is a blueprint or a template.eg.form for an exam that contains name,age,father's name etc.

# Objects:Specific instance created from the template (clas.).eg.form which contains the data for Saurav


class Employee:
    company="HP"
    def get_salary(self):# self is the way to refer the objects of a given class>>>>>
        return 23000
    def role(self):
        print("Data-Scientist")
    
    
e_1=Employee()# employee is created here!
print(e_1.get_salary()) # employee e_1 salary method is called
print(e_1.role())
