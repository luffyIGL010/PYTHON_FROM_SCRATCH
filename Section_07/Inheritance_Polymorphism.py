class Animal:# Parent class....
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("Generic Animal sound")
        
class Dog(Animal): #This is how inheritance works
    def speak(self):
        super().speak()
        print("Woof..Woof...Woof...Woof...Woof..Woof...")
        
        
#a=Animal("Dog")
D=Dog("Tom")
D.speak()




#Calling Parent Constructor with super()

class Bird(Animal):
    def __init__(self, name,wingspan):
        super().__init__(name)
        self.wingspan=wingspan
        
        
bird_01=Bird("Woodpeaker",10)
print(bird_01.name)
print(bird_01.wingspan)