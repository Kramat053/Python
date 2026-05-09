#Recursion in Python
#It is a technique in python when a function calls itself

def mul(a,b):
 if b==1:
  return a
 else:
  return a+mul(a,b-1)
print(mul(5,6))

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))

#Fibonacci sequence
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
print(fib(5))

#Memoization
#It is essentially giving the function a "notepad" to write down answers it has already found
memo = {0: 0, 1: 1}
def fib_memo(n):
    if n in memo:
        return memo[n]
    result = fib_memo(n - 1) + fib_memo(n - 2)
    memo[n] = result
    return result
print(fib_memo(50))

#Lamda Function
#It is an anonymus mostly one line function that does not have a name
#It is created using the Lambda keyword
#Its syntax is-->  lambda arguments : expression
#It automatically returns the result
x=lambda x : x*x
print(x(9))
#It is mostly used in High Order Function

#High Order Function
#It is a function that requires an other function to work as it takes a function as input or returns a function as an output
def square(x):
    return x * x
numbers = [1, 2, 3, 4]
# map is the higher-order function here
squared_numbers = list(map(square, numbers)) 
print(squared_numbers) # Output: [1, 4, 9, 16]
 