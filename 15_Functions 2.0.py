def a(number):
    if number%2==0:
       return "even"
    else:
        return "odd" 

for i in range(1,11):
    print(a(i))

#Arguments and Parameters
#Argument is the variable name and parameters is the variable's value

#Nested Function-->is a functioon inside a function
def f():
    print("f")
    def g():
        print("g")
    g()    
f()        
        