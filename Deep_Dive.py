#Aliasing inn Python
#It means having multiple reference of a same data

a = 1
b = a
print(id(a))
print(id(b))# both variables have same id indicating that both points to the same object

#Garbage Collector
#It is an automated memory management system that finds and deletes objects that are no longer being used by your program to free up computer memory.
#For example if we delete both the variables pointing to the objects the objecty is still present in the memory so to clear the memory garbage collector works

#Reference Counter
#It is the method by which we count the number of reference to a data
x = [1,2,3]
y = x
import sys
print(sys.getrefcount(x))

#Weird Behaviours in Python
#1)Integer Interning (Pre-built Numbers)
#Note that in the above concept of reference counter if we had taken a variable of value 2 then do aliasing and then do the reference counter the result will be a huge number just because python has already in built values like these to make the programs run fast so due to that the reference counter will be high
print(sys.getrefcount(a))
#2)The same integer interning is the reason that values between -5 to 256 have same memory addreses and other values have different
c = 256
d = 256
print(id(c))
print(id(d))
e = 257
f = 257
print(id(e))
print(id(f))
#3)String Interning
#We would have same IDs for two same valid Identifiers but different IDs for two same but not valid identifiers
a1 = "Catch_Me"
a2 = "Catch_Me"
print(id(a1))
print(id(a2))
b1 = "1Catch_Me"
b2 = "1Catch_Me"
print(id(b1))
print(id(b2))

#List Storage in Python
#Python store lists as a contiguous block of memory addresses (pointers) rather than the actual objects themselves, allowing them to hold multiple data types efficiently.
#To ensure high performance, Python uses over-allocation, grabbing more memory than needed during an append() so that future additions are nearly instantaneous.
#This structure allows for O(1) random access, meaning Python can jump to any index in the list immediately by calculating its offset in memory.

#Mutability
#It refers to the ability to change or edit a data in its location
#List	    ✅ Yes	list.append(), list.pop(), list[0] = x
#Tuple	    ❌ No	Cannot change; must create new_tuple = old + (x,)
#String	    ❌ No	str.replace() returns a new string object.
#Dictionary	✅ Yes	dict["key"] = "new_value"
#Sets       ✅ Yes   set.add(), set.remove(), set.clear()
# In immutable data type when you "add" elements, Python doesn't modify the original; it creates an entirely new object at a different memory address.
#In contrast, mutable objects like lists allow in-place changes, meaning their ID remains constant even as their content grows or shrinks.

#Side Effects of Mutability
#The main side effect of mutability is aliasing, where multiple variables point to the same memory address, leading to unexpected changes across your program.
#For example if you modify list_b, list_a changes automatically because they share the same ID.