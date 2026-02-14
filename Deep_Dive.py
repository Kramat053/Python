#Aliasing inn Python
#It means having multiple names of a same data

a = 1
b = a
print(id(a))
print(id(b))# both variables have same id indicating that both points to the same object

#Reference Counter
#It is the method by which we count the number of reference to a data
a = 1
b = a
print(id(a))
print(id(b))
import sys
print(sys.getrefcount(a))

#Garbage Collector
#It is an automated memory management system that finds and deletes objects that are no longer being used by your program to free up computer memory.
#For example if we delete both the variables pointing to the objects the objecty is still present in the memory so to clear the memory garbage collector works