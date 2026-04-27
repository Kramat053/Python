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

#Lambda Function
#It is a one line code anonymous function that 
#its syntax is--> lambda arguments : expression
add_ten_lambda = lambda x: x + 10
print(add_ten_lambda(5))

#High Order Function
#It is a function that takes a function as input or returns a function as an output
#There are two types one is user derived and the other is built in
 