# Module 1: Variables,Data Types (Strings, integers, lists, Boolean), Arithmetic Operators    
import time

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

print(
    """Our next data type is integers, the same type you've learned about in your math class.
    We can store integers in variables and do arithmetic operations on these variables.
      """)
time.sleep(3)
print(
    """The basic arithmetic operations are as follows
    Addition: + adds two numbers together
    Subtraction: subtracts one number from another
    Multiplication: * multiplies two numbers together
    Division: / divides a number by another, (Double check) rounds down to a whole number
    Modulus: % this returns the remainder of a division operation
      """)
time.sleep(3)
print("""
Take a look at this basic Program:
      
      x = 3
      y = -20

      print(x + y)
      """)

answer = input("What should the above program output?\n")

if answer == -17:
    print("Yes that is correct. The print statement outputs the sum of the two integers")
else:
    print("Sorry, that is incorrect. The print statement outputs the sum of the two integers: -17")

time.sleep(3)

print("Let's do some more practice")
answer = input("""
What will be printed out by this program?
            
               
    x = 7
    y=5
    z = 4
    print(x*y*z)
      """)

if answer == 140:
    print("Yes that is correct!")
else:
    print("Sorry, that is incorrect. The correct answer is 140.")

time.sleep(3)

answer = input("""
What will be printed out by this program?
            
               
    x = 7
    y=5
    z = 4
    print("x - y + z")
      """)

if answer == 140:
    print("Yes that is correct! You remembered that anything in quotes gets printed as is by the print function. Good job")
else:
    print("""Sorry, that is incorrect. The correct answer is x - y + z. 
          Remember that if something is in quotes inside the print statement that it gets printed out as is """)


#Booleans
print("""
      Our next data type is called a boolean
      A boolean represents one of two values: True or False. 
      """
)
time.sleep(3)

print("""
      These data structures are usually used to tell another strip of code whether to execute or not
      Take the following piece of code as an example:

    
    isFound = False

    if isFound:
        //some code
"""
)

time.sleep(3)

print("""
The above code checks for something and then executes some other code based on what it finds in "isFound"
      """
      )

print(
    """
"""
)

# Lists
print("""
Our next data type is called a list. 
In programming, this data structure is called an array, but in Python specifically it is called a list.
Lists are data structures that can hold multiple elements of any data type
      """)

time.sleep(3)



print(
    """Here are some example lists:
    list1 = [1, 2, 4, 7, 8 , 9]
    list2 = ["Tom", 3, "Abbey" 5, isFound]
    
    Notice that you can have lists containing one data type or multiple"""
)

# exercises to integrate all these concepts
print("""Let's combine everything we have learned today
      """)

answer = input("""
               Program 1:

               seven = True
               list_a = [1, 2, 3, "4", "five", 6, seven, 8, 9, 10]

               
               Take a look at the above code snippet.
               How many variables of the data type integer are in the list?
               """
               )

if answer == 7:
    print("Correct!")
else:
    print("Sorry that is incorrect (explanation later)")

answer = input("How many strings are in the list")

if answer == 2:
    print("Correct!")
else:
    print("Sorry that is incorrect.")

answer = input("How many Booleans are in the list")

if answer == 1:
    print("Correct!")
else:
    print("Sorry that is incorrect.")


print("Ok let's breakdown the code snippet")
time.sleep(3)
print("The first 3 elements of the list are clearly integers")
time.sleep(3)
print("The element after that is a string because it is in quotations")
time.sleep(3)
print("The same reasoning applies to the element after that")
time.sleep(3)
print("Then 6 is an integer as well")
time.sleep(3)
print("seven is a boolean because it is initialized as a boolean right above the list")
time.sleep(3)
print("And then the last 3 elements are integers as well")

time.sleep(3)

answer = input("""
Program 2:
               x = 4
               y = 7 
               list_b = [2*3,4*5,x*y]
               print(list_b)

               What would the above code snipper output?
               """
               )

if answer == [6,20,28]: # check
    print('Correct!')
else:
    print("Sorry, that is incorrect")


time.sleep(3)
print("Let's break down this code snippet")
time.sleep(3)
print("x is set to 4 and y is set to 7")
time.sleep(3)
print("The list then evaluates each arithmetic expression before outputting the list")


time.sleep(3)



print("Thank you for paying attention and learning some imperative programming today!")





    













