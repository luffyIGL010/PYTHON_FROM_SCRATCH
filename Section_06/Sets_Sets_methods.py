# Sets are unordered ,unique collections(no duplications)..
S={3,4,5}
print(S,type(S))
S.add(33)
print(S)
print(S.remove(4))



# Set_operations

a={1,2,3,4,5}
b={3,4,6,7,8,9}
c=a.union(b)
d=a.intersection(b)
e=a.difference(b)
f=a.symmetric_difference(b)
print(c)
print(d)
print(e)
print(f)