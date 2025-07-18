def avg(a,b,c):
    average=(a+b+c)/3
    print(average)
    
    
avg(2,3,4)

#keyword_arguments
def Student(name,age):
    print(name,age)
    
Student(name="Saurav",age="17")

#Lmbda functions
square=lambda x:x*x
print(square(5))



sum =lambda x,y,z:x+y+z
print(sum(3,4,5))