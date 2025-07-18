# Lists are ordered ,mutable collections of items.

marks=[22,44,56]
mixed=["HII",3.5,44]
print(marks)
print(mixed)

print(marks[0])
print(marks[0:3])

#Common lists Methods

marks.append(67)
print(marks)


marks.pop()
print(marks)
print(marks.count(44))


a=6
Table=[]
for i in range (1,11):
    Table.append(5*i)
    
print(Table)


# List_ Comprehension>>>>>>>


Table_05=[5*i for i in range(1,11)]
print(Table_05)


Squred=[i*i for i in range(1,10)]

print(Squred)
