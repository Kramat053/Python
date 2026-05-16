#Finding the Oldest age 
age1 = input("Enter age 1\n")
age2 = input("Enter age 2\n")
age3 = input("Enter age 3\n")

if (age1>age2) and (age1>age3):
    print(age1,"is the oldest age")
if (age2>age1) and (age2>age3):
    print(age2,"is the oldest age")    
if (age3>age2) and (age3>age1):
    print(age3,"is the oldest age")    