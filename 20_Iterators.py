#Iteration
#iteration is the process of repeating a set of instructions over and over again.
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(f"I am eating a {fruit}")
#Iterator
#iterator is the specific object that performs the work of stepping through the items.
#Iterators works smartly by taking only the required data in the memory and replace it with the next when its work is finished so this way lots of memory is saved
#Iterable
#It is the data over which iteration is done

#Making own For Loop
def my_for_loop(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break    
a = ("Ali","Ahmad","Hassan")
my_for_loop(a)