# String data types

print('')
print('***  String data types   ***')
print('')

    # literal assignment

print('')
print('~~~~  Literal Assignment (eg : Name)  ~~~~')
fname = "Apoorva"
lname = "DK"

print(fname)
print(type(fname))
print(type(fname) == str)
print(isinstance(fname, str))
print('')

    # constructor function 

print('')
print('~~~~ Constructor Function (eg : Paratha) ~~~~')
paratha = str("Aloo")

print(paratha)
print(type(paratha))
print(type(paratha) == str)
print(isinstance(paratha, str))
print('')

    # concatination 

print('')
print('~~~~ Concatination   ~~~~')
fullname = fname + " " + lname
print(fullname)

fullname += " !"
print(fullname)
print('')

    # Casting a number to a string 

print('')
print('~~~~ Casting a number to a string    ~~~~')
decade = str(2000)
print(type(decade))
print(decade)

statement = "I like folk music from the " + decade + "s."
print(statement)
print('')

    # Multiple lines

print('')
print('~~~~ Multiple lines  ~~~~')
multiline = '''

Hey! How are you?           
    Just checking in...
            All good?

'''
print(multiline)
print('')

    # Escaping special characters 

print('')
print('~~~~ Escaping special characters ~~~~')
sentence = 'Hey! \n I\'m back to work. \n By the way, \t where\'s this at\\located?'
print(sentence)
print('')

    # String methods 

print('')
print('~~~~ String methods  ~~~~')
print(fname)
print(fname.lower())
print(fname.upper())
print(fname)

print('')
print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)

print('')
print(len(multiline))
multiline += "      "
print(len(multiline))
multiline = "           " + multiline
print(len(multiline))

print('')
print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))
print('')

    # Build a menu 

print('')
print('~~~~ Build a menu    ~~~~')
print()
title = " menu ".upper()
print(title.center(24, "-"))
print("")
print("Filter coffee ".ljust(28, "_") + "Rs. 20".rjust(8))
print("Wada pav ".ljust(28, "_") + "Rs. 15".rjust(8))
print("Rava cake ".ljust(28, "_") + "Rs. 30".rjust(8))
print('')

    # String index values 

print()
print("~~~~ String index values ~~~~")
print(fname)
print(fname[0])
print(fname[-1])
print(fname[1:-1])
print(fname[1:])
print()

    # Some methods return Boolean data 

print()
print('~~~~ Some methods return Boolean data    ~~~~')
print(fname.startswith("A"))
print(fname.startswith("a"))
print(fname.startswith("K"))
print(fname.endswith("a"))
print()

# Boolean data type 

print()
print('***  Boolean data type   ***')
myTvalue = True
myFvalue = bool(False)  # constructor function 
print(myFvalue)
print(type(myFvalue))
print(myTvalue)
print(isinstance(myTvalue, bool))
print()

# Numeric data types 

print()
print('***  Numeric data types  ***')

    # Integer

print('~~~~ Integer ~~~~')
price = 80
best_price = int(40)
print(price)
print(type(price))
print(best_price)
print(isinstance(best_price, int))
print()

    # Float

print('~~~~ Float   ~~~~')
gpa = 9.04
gpa_func = float(8.84)
print(gpa)
print(type(gpa))
print(gpa_func)
print(isinstance(gpa_func, float))
print()

    # Complex type

print('~~~~ Complex type    ~~~~')
comp_val = 4+8j
print(comp_val)
print(type(comp_val))
print(isinstance(comp_val, complex))
print(comp_val.real)
print(comp_val.imag)
print()

    # Built-in functions for numbers 

print()
print('~~~~ Built-in functions for numbers  ~~~~')
print(gpa)
print(abs(gpa))
print(gpa * -1)
print(abs(gpa * -1))
print(round(gpa))
print(round(gpa, 1))
print()

    # Built-in math module 

import math

print()
print('~~~~ Built-in math module    ~~~~')
print(math.pi)
print(math.sqrt(64))
print(gpa)
print(math.ceil(gpa))
print(math.floor(gpa))
print()

    # Casting a string to a number 

print()
print('~~~~ Casting a string to a number    ~~~~')
zipcode = "48007"
print(zipcode)
print(type(zipcode))
zip_val = int(zipcode)
print(zip_val)
print(type(zip_val))
print()

    # Error if you attempt to cast incorrect data
print()
print('~~~~ Error casting improper string to a number    ~~~~')
zip_value_err = int("Bengaluru")
print()
