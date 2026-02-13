                      #Sets in Python
#It is also one of the built in data types use to store data
# 1.Sets do not allow duplicate
# 2.Sets have no  indexing/slicing
# 3.Sets do not allow mutable data types
# 4.Sets itself is mutable

#Creating Sets
a = set()#empty set can be created using only this method
print(type(a))
print(a)
b = {1,2,3,4}
print(type(b))
print(b)
c = {1,"Ali",3.5,True}
print(type(c))
print(c)
d = {1,1,2,2}
print(d)#Output will be {1,2} as sets do not allow duplicates
#e = {[1,2]}Here the ouput will give error as sets do not allow mutable data types
f = {(1,2)} 
print(f)

#Hashing in Sets 
#It is a technique which determines the position of elements of a set

#2D Sets
#set1 = {1,2,{3,4}This will give error as we cannot make 2D sets because sets itself is mutable and mutable data types are not allowed in sets

#Accessing Set items
#We cannot access set items as indexing is not allowed in sets

#Editing in Sets
#same as accessing sets cannot be edited due to unavailiblity of it indexing

#Addition in Sets
set2= {1,2,3}
set2.add(4)
print(set2)

#Deletion in Sets
a1 = {1,2,3}
del a1#Remember that we cannot delete single item of a set because of the restiction to indexing\
a2 = {1,2,3}
a2.remove(1)#To remove a single item in a set we should use the remove keyword
print(a2)
a3 = {1,2,3}
a3.pop()
print(a3)#it will not exactly delete 3 due to hashing 

#Operations in Sets
#Sets don't have the addition or multiplication operation
#But it do have the Loops
b1 = {1,2,3}
for i in b1:
    print(i)
#Also it ha the membership operator
print(3 in b1)  

#Functionss in Sets
b2 = {1,2,3,4}
print(len(b2))
print(max(b2))
print(min(b2))
print(sorted(b2))
print(sorted(b2,reverse=True))#It sorts the value in reverse
#Functions only specific for Sets
x = {1,2,3,4}
y = {3,4,5,6}
print(x.union(y))
print(x.intersection(y))
print(x.diffference(y))
print(y.diffference(x))
print(x.symmetric_difference(y))
print(x.issubset(y))
print(x.isdisjoint(y))
print(x.issuperset(y))







