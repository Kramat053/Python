                  #List in Python
#List is a built in data type that holds a collection of data of same or different type.
list1 = [1,2,3,4,5]#homogeneous list
list2 = [1,"Hello",3.4,True]#heterogeneous list
list3 = []#empty list 

#2D List(List within list)
list4 = [1,2,3,[4,5]]
list5 = [1,"Ali",[True,3.5]]

#3D List
list6 = [1,2,["ali",[True]]]

list7 = [[[1,2],[3,4],[5,6]]]

list8 = list("Ali")
print(list8)

#Accessing list items
print(list1[0])
print(list4[3])
print(list6[2])
print(list1[-1])
print(list4[3][0])
print(list7[0][1][-1])

#Editing Lists(as Lists in Python are changeable)
#Editing the existing items
list1[0] =-1
print(list1)
list1[-1] =-1
print(list1)
list1[0:4] =1,2,3,4
print(list1)
#Adding new items to the list
list1.append(10)#adds single item
print(list1)
list1.extend([10,20])#adds multiple items
print(list1)
list1.insert(0,1000)
print(list1)

#Deleting list in python
a = [1,2,1,2]
# del a #Deleting whole list
print(a)
b = [1,2,2,1]
del b[0]
print(b)

c = [1,"hello",2]
c.remove("hello")#it is used when we don't know the index of the element we want to delete 
print(c)

d= [1,1,2,2]
d.pop()#it deletes the last element of the list
print(d)

e= [1,2,0,1]
e.clear()#it cleares the whole list and makes it empty
print(e)

#Operations in Lists
a1 = [1,2,3,4]
b1 = [5,6,7,8]
print(a1+b1)
print(a1*2)
for i in a1:#This is loop
    print(i)
print(1 in a1)#This is membership operator


#Functions in list
c1 = [1,2,3,4]
print(len(c1))
print(max(c1))
print(min(c1))
print(sorted(c1))
print(sorted(c1,reverse=True))#It sorts the value in reverse




