#Generators
#It is a simple way of creating Iterators
def simple_generator():
    print("Starting...")
    yield 1
    print("Resuming...")
    yield 2
    print("Ending...")

gen = simple_generator()

print(next(gen)) # Output: Starting... 1
print(next(gen)) # Output: Resuming... 2

#Range Function using Generator
def mera_range(start,end):
     for i in range(start,end):
         yield i
gen = mera_range(1,11)
for i in gen:
     print(i)
         