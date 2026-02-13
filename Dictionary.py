#Dictionary in Python
#It is a built in data type to store key:value pairs data
#Dictionary has no indexing
#It is mutable
#Keys are immutable and values are mutable
#Keys should be unique

#Creating Dictionary
a = {}
b = {"Name":"Ali"}
#c = {{1,2}:"Ali"} -->This gives error as keys are immutable
c = {(1,2):"Hassan"}
print(c)
d = {"Name":"Kami","Name":"Ahmed"}
print(d)
e = {"Name":"Asif","Grade":11,"Marks":{"eng":90,"math":80}}#2D Dictionary

#Accessing in Dictionary
#It is done by writing the key and the value is displayed
print(b["Name"])
