#Dictionary in Python
#It is a built in data type to store key:value pairs data
#Dictionary has no indexing
#It is mutable
#Keys are immutable and values are mutable
#Keys should be unique

#Creating Dictionary
a = {}
b = {"Name":"Ali","Class":"Inter"}
#c = {{1,2}:"Ali"} -->This gives error as keys are immutable
c = {(1,2):"Hassan"}
print(c)
d = {"Name":"Kami","Name":"Ahmed"}
print(d)
e = {"Name":"Asif","Grade":11,"Marks":{"eng":90,"math":80}}#2D Dictionary

#Accessing in Dictionary
#It is done by writing the key and the value is displayed
print(b["Name"])
print(e["Marks"]["math"])#for accesssing anitem in 2D dictionary

#Editing in Dictionary
b["Name"]="Arif" #This is how we edit an item in a dictionary
print(b)

#Adding in Dictionary
b["age"]=18#This is how we add a new item to a dictionary
print(b)

#Deleting in Dictionary
del a #This is how we delete an entire dictionary
del b["Class"] #Thios is how we delete an item from a dictionary
a1 = {"a":"b"}
a1.clear() #Doing this we can clear a dictionary and the output will be empty
print(a1)

#Operations in Dictionary
#There are no addition or multiplication operation in Dictionary
#But there are loops
for i in e:
    print(i)#Note that the output will be the keys not the values
#Membership opeartor
#this operator will only work according to the key not the value
print("Name" in e)
print("Asif" in e)

#Functions in Dictionary
x = {"Name":"Aman","age":"22"}
print(len(x))
print(max(x))
print(min(x))
print(sorted(x))
print(sorted(x,reverse=True))#It sorts the value in reverse

#Functions only specific for Dictionary
print(x.keys())
print(x.values())

