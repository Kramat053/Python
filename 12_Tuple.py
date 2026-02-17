                    #Tuples in Python
#Creating Tuples
#It is the same as lists apart from some key differences
a = (1,2,3,4)#it is created with round brackets
b = (1)#Here it is declared as string due to the single member
c = (1,)#To overcome the above problem we add comma after the single element
d = tuple([1,2])
print(type(a))
print(type(b))
print(type(c))
print(type(d))

#Accessing tuples
#It is the exact same as lists
a1 = (1,2,3,4)
a2 = (1,2,(3,4))
print(a1[0])
print(a1[-1])
print(a2[2][0])
print(a1[0:])
print(a1[:3])

#Editing Tuples
#Tuples are unchangeable so both editing and addining could not be done
#a1[0] = 100
#a1.append(100)
#Both the above will give error

#Deleting Tuple
#In tuples we cannot delete a single item but we can delkete the whole tuple by the del keyword
x = (1,2,3,4)
del x

#Operations in Tuples
#It is alo exactly same as in list
b1 = (1,2,3,4)
b2 = (5,6,7,8)
print(b1+b2)
print(b1*2)
for i in b1:#This is loop
    print(i)
print(1 in b1)#This is membership operator

#Functions in Tuples
#Functions in list
y = (1,2,3,4)
print(len(y))
print(max(y))
print(min(y))
print(sorted(y))
print(sorted(y,reverse=True))#It sorts the value in reverse
