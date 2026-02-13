#String Functions
a = "Karachi"
print(a.upper())#Changes the letters to uppercase
print(a.lower())#Changes the letters to lowercase
print(a.title())#It capatilizes the first letter of every word
print(a.capitalize())#It capatilizes the first letter of the first word
print(a.swapcase())#Changes the uppercase to lowercase and lowercase to uppercase
print(a.count("a"))#counts the number of times a specific letter occur
print(a.find("c"))#Finds the position of a specifc letter. -1 is returned when invalid letter is entered
print(a.index("c"))#same as find but gives an error when invalid letter is entered
print(a.endswith("i"))#gives True/False for the entered ending value
print(a.startswith("K"))#gives True/False for the entered starting value
print("Hello my name is {} and I am {}.".format("Ali",21))
print("Hello my name is {0} and I am {1}.".format("Ali",21))
print("Hello my name is {name} and I am {age}.".format(name ="Ali",age = 21))
print("ali099".isalnum())#checks whether its alphanumeric or not
print("ali".isalpha())#checks whether its alphabet or not
print("099".isdigit())#checks whether its a digit or not
print("ali_099".isidentifier())#checks whether its identifier or not
print("9".isdecimal())#checks whether its decimal or not
print("Pakistan is an agrobased country".split())#Converts to a list
print("Pakistan is an agrobased country".split("an"))#Converts to a list while partitioning words before and after the word in the split bracket
print(" ".join(["how", "are", "you"]))#its the opposite of split it join a list into a single unit
print("/".join(["how", "are", "you"]))
print("-".join(["how", "are", "you"]))
print("My name is Ali".replace("Ali","Raza"))#replaces a word pointed with another word given
print("    ali    ".strip())#removes the characters(usually spaces)before and after the main word
#Common Functions
b = "Islamabad"
print(len(b))
print(max(b))
print(min(b))
print(sorted(b))
print(sorted(b,reverse=True))#It sorts the value in reverse
