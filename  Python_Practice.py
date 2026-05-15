#Finding the Oldest age 
age1 = input("Enter age 1")
age2 = input("Enter age 2")
age3 = input("Enter age 3")

if (age1>age2) and (age1>age3):
    print(age1,"is the oldest")
if (age2>age1) and (age2>age3):
    print(age2,"is the oldest")    
if (age3>age2) and (age3>age1):
    print(age3,"is the oldest")    