#Stores the key-value pairs and allow fast lookups.
marks={"Harry":34,
       "Kira":54}
print(marks)
print(marks["Harry"])
marks["Harry"]=55
print(marks)
print(marks.keys())

#Dictionary_Comprehension

square={x:x*x for x in range(1,11)}
print(square)