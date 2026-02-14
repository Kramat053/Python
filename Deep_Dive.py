#Aliasing inn Python
#It means having multiple names of a same data

a = 1
b = a
print(id(a))
print(id(b))# both variables have same id indicating that both points to the same object

#Reference Counter
#It is the method by which we count the number of reference to a data
import sys
print(sys.getrefcount(a))
 