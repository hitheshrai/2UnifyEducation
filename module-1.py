'''

Module 1:

Variables,

Data Types (
    Strings,
    integers, 
    lists
    Boolean
),

Arithmetic Operators    

'''

import time

#while (True):
print(
    """
Hello, there.
Today, we'll be learning some of the basics of programming through the language Python.
Let's Begin
    """
)
time.sleep(3)
# Data types
# Strings
print(
    """
We will begin with basic data types and variables
Variables are elements in programming that can represent a certain data type and can be changed.
The first data type we will look at is called strings.
    """
)

time.sleep(3)

print(
    """
Strings are a sequence of characters that can contain letters and numbers but they must ALWAYS start and end with quotation marks.
They can be used to represent text in programs and other applications.
    """
)

time.sleep(3)

print(
    """
We can print these strings using the 'print()' function, with our string variable inside the print function. 
These words you're reading are being generated using the print function.

Look at the code snippet below for example.

my_string = "Hello, my name is Bob."
print(my_string)

This code here would output the variable 'my_string', which has the assigned value of "Hello, my name is Bob."
"""
)

time.sleep(3)

print(
    """
Variables help keep data more manageable and code easier to read.
Take these two programs below.

Program 1:
my_string = "Hello, my name is Bob"
print(my_string)
print(my_string)
print(my_string)
print(my_string)
print(my_string)


Program 2:
print("Hello, my name is Bob.")
print("Hello, my name is Bob.")
print("Hello, my name is Bob.")
print("Hello, my name is Bob.")
print("Hello, my name is Bob.")

Although the outputs for both of these are the exact same, it's pretty obvous which one is easier to read, understand and manage. 
Imagine this on a much larger scale with bigger programs, and it only makes more sense why we use variables (FIX THIS WORDING)
"""
)

time.sleep(3)

print("""
Ok, let's practice. What would this program output?
"""

)

answer = input(
    """ Program 1:
        string1 = "I love programming"
        print(string1)
        """
    )       

if  answer == "I love programming":
    print("That's correct! Great Job!")
else:
    print(
        """"
        Sorry that was incorrect.
        The correct answer was: I love programming
        Make sure you have correct spacing, capitalization and punctuation (strings output exactly as they are written).
        """)

time.sleep(3)

print("""
Ok, next question. What would this program output?
"""
)

answer = input(
    """ Program 2:
        string2="I like coding"   
        print("string2")
        """
    )       

if  answer == "string2":
    print("That's correct! Great Job!")
else:
    print(
        """"
        Sorry that was incorrect.
        The correct answer was: string2
        Remember that if something is in quotation marks inside the print function it will print what is in the quotations exactly.
        In this case string2 was in quotations, so it printed string2 as a string rather than the variable string2.
        """)
    
time.sleep(3)


print("""
Ok, last question. What would this program output?
"""
)

answer = input(
    """ Program 3:
        string3=I am learning about strings   
        print(string3)
        """
    )       

if  answer == "error" or answer == "Nothing":
    print(""""That's correct! Great Job!
            You didn't fall for the trick""")
else:
    print(
        """"
        Sorry that was incorrect.
        The correct answer was: error OR Nothing
        When the variable string3 was being made, the phrase I am learning about strings was never put in quotation marks, so it was never made correctly
        """)
    
time.sleep(3)


# Continue on
# Integers










