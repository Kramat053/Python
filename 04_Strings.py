#Creating strings
a = "Ali"
print(a)

#Indexing strings(extracting a character at a specific index(location))
print(a[0])
#There are two types of Indexing
#Positive Indexing(from left to right)
print(a[1])
#Negative Indexing(from right to left)
print(a[-1])

#Slicing in Strings(extracting multiple characters from a string by giving a range)
b = "Hello World"
print(b[0:7])
print(b[:3])
print(b[3:])
print(b[0:8:2])#[start:end:step]


#Editing and Deleting Strings
#Strings in Python are immutable(means once created it cannot be changed or edited)
c = "Pakistan"
del c #This is the syntax for deletion(remember deletion can only be done to a whole variable not single character)
print(c)