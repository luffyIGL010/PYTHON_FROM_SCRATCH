name="Harry"
print(name)


#Indexing
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[-1])
print(name[-2])


#String_Slicing
name="Python is High level Language"
print(name[0:4])

name_1="Harry"
print(name_1[2:-2])

print(name[0:10:2])
print(name[0:10:4])

print(name_1[:4])
print(name_1[1:])



#String_Methods

name="Harry"
a=len(name)
print(a)
print(name.upper())
print(name.capitalize())
print(name.lower())
print(name.lstrip())
print(name.rstrip())
print(name.strip())

print(name.replace("Harry","fun"))


text="I love coding"
print(text.split(","))


# String_formatting

template="Dear {}, You are awesome.Take this {}$ bag"
a="Saurav"
a1=100
b="AKXH"
b1=399

s1=template.format(a,a1)
print(s1)

print(f"{a} you are awesome and take this {a1}$ bag")