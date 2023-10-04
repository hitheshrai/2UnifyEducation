# Module 1: Variables,Data Types (Strings, integers, lists, Boolean), Arithmetic Operators    


# Data types, variables and Strings Review
input(
    """
So you've learned a bit about imperative programming and data types.
Let's take a deeper look.
Click enter to progress through each statement.
    """
)

# Data types
# Strings
input(
    """
As you learned, variables are elements in programming that can represent a certain data type and can be changed.
Let's focus on strings.
""")
input(
    """
Strings are a sequence of characters that can contain letters and numbers but they must ALWAYS start and end with quotation marks.
They can be used to represent text in programs and other applications.
    """
)

input(
    """
We can print these strings using the 'print()' function, with our string variable inside the print function. 
These words you're reading are being generated using the print function.

Look at the code snippet below for example.

my_string = "Hello, my name is Bob."
print(my_string)

This code here would output the variable 'my_string', which has the assigned value of "Hello, my name is Bob."
"""
)

input(
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
Imagine this on a much larger scale with bigger programs, and you'll see what variables are so necessary
"""
)


#DIVIDER
# First group of exercises
answer = input(
    """ Ok, let's practice. What would this program output?

    Program 1:
        string1 = "I love programming"
        print(string1)
        """
    ).lower()       

if  answer == "i love programming":
    input("That's correct! Great Job!")
else:
    input(
        """"
        Sorry that was incorrect.
        The correct answer was: I love programming
        Make sure you have correct spacing, capitalization and punctuation (strings output exactly as they are written).
        """)


answer = input(
    """ Ok, next question. What would this program output?

    Program 2:
        string2="I like coding"   
        print("string2")
        """
    ).lower()     

if  answer == "string2":
    input("That's correct! Great Job!")
else:
    input(
        """"
        Sorry that was incorrect.
        The correct answer was: string2
        Remember that if something is in quotation marks inside the print function it will print what is in the quotations exactly.
        In this case string2 was in quotations, so it printed string2 as a string rather than the variable string2.
        """)


answer = input(
    """ Ok, last question. What would this program output?

    Program 3:
        string3=I am learning about strings   
        print(string3)
        """
    ).lower()

if  answer == "error" or answer == "nothing":
    input(""""That's correct! Great Job!
            You didn't fall for the trick""")
else:
    input(
        """"
        Sorry that was incorrect.
        The correct answer was: error OR Nothing
        When the variable string3 was being made, the phrase I am learning about strings was never put in quotation marks, so it was never made correctly
        """)
    

# DIVIDER

# Integers
input(
    """Our next data type is integers, the same type you've learned about in your math class.
    We can store integers in variables and do arithmetic operations on these variables.

The basic arithmetic operations are as follows
    Addition: + adds two numbers together
    Subtraction: subtracts one number from another
    Multiplication: * multiplies two numbers together
    Division: / divides a number by another, (Double check) rounds down to a whole number
    Modulus: % this returns the remainder of a division operation
      """)

answer = input(""""
               
    Take a look at this basic Program:
      
      x = 3
      y = -20

      print(x + y)
               
    What should the aboce program output?""").lower()

if answer == -17:
    input("Yes that is correct. The print statement outputs the sum of the two integers")
else:
    input("Sorry, that is incorrect. The print statement outputs the sum of the two integers: -17")



answer = input("""
Let's do some more practice
What will be printed out by this program?
            
               
    x = 7
    y=5
    z = 4
    print(x*y*z)
      """).lower()

if answer == 140:
    input("Yes that is correct!")
else:
    input("Sorry, that is incorrect. The correct answer is 140.")


answer = input("""
What will be printed out by this program?
            
               
    x = 7
    y=5
    z = 4
    print("x - y + z")
      """).lower()

if answer == "x - y + z":
    print("Yes that is correct! You remembered that anything in quotes gets printed as is by the print function. Good job")
else:
    print("""Sorry, that is incorrect. The correct answer is x - y + z. 
          Remember that if something is in quotes inside the print statement that it gets printed out as is """)




#DIVIDER
#Booleans
input("""
      Our next data type is called a boolean
      A boolean represents one of two values: True or False. 
      """
)

input("""
      These data structures are usually used to tell another strip of code whether to execute or not
      Take the following piece of code as an example:

    
    isFound = False

    if isFound:
        //some code

The above code checks for something and then executes some other code based on what it finds in "isFound"
      """
      )

# Exercises
answer = input("""
               Let's do an exercise
Program 1:
               
isBlue  = False
               
if (isBlue):
    //....
               

Will the code in the if statement execute?
               """).lower()

if answer == "no":
    input("Correct! The 'if' statement requires a Boolean value of true to execute, but the Boolean 'isBlue' is set to False.")
else:
    input("Sorry, that's incorrect. The 'if' statement requires a Boolean value of true to execute, but the Boolean 'isBlue' is set to False.")


# DIVIDER
# Lists
input("""
Our next data type is called a list. 
In programming, this data structure is called an array, but in Python specifically it is called a list.
Lists are data structures that can hold multiple elements of any data type
      """)

input(
    """Here are some example lists:
    list1 = [1, 2, 4, 7, 8 , 9]
    list2 = ["Tom", 3, "Abbey" 5, isFound]
    
    Notice that you can have lists containing one data type or multiple"""
)

input(
    """Some important methods for lists are:
    insert(): inserts an element into a list at a specific index
    remove(): removes the first instance of a specific element in a list
    append(): adds an element to the end of a list
    pop(): removes the element at the end of the list
    """
)

#exercises for lists

answer = input("""
Ok, let's practice
Program 1:
        myList = [1,2,3,4,5]
        myList.append(6)
        myList.append(7)
        myList.append(8)
        myList.pop()

What is the last element in this list after all the code above is executed?
               """).lower()

if answer == 7:
    input("Correct!")
else:
    input(""""Sorry that is incorrect. 
          We added 6, 7, and 8 to the end of the list, but then popped off the last element at the end which is 8,
        so the answer is 7""")
    


answer = input("""
Program 2:
               
        
        listA = [1, 1, 2, 2, 3, 4, 5]
        listA.remove(1)
        listA.remove(2)
               
        What is the first element in this list after all the code above has executed?
               """).lower()

if answer == 1:
    input("Correct!")
else:
    input(""""Sorry that is incorrect. 
          Remember the remove function only removes the first instace of an element from a list""")





# DIVIDER
# exercises to integrate all these concepts


answer = input("""
               Let's combine everything we have learned in this module

               Program 1:

               seven = True
               list_a = [1, 2, 3, "4", "five", 6, seven, 8, 9, 10]

               
               Take a look at the above code snippet.
               How many variables of the data type integer are in the list?
               """
               )

if answer == 7:
    input("Correct!")
else:
    input("Sorry that is incorrect (explanation later)")

answer = input("How many strings are in the list")

if answer == 2:
    input("Correct!")
else:
    input("Sorry that is incorrect.")

answer = input("How many Booleans are in the list")

if answer == 1:
    input("Correct!")
else:
    input("Sorry that is incorrect.")


input(""""Ok let's breakdown the code snippet")
The first 3 elements of the list are clearly integers
The element after that is a string because it is in quotations.
Then 6 is an integer as well.
seven is a boolean because it is initialized as a boolean right above the list")
And then the last 3 elements are integers as well""")


answer = input("""Ok Next exercise:
Program 2:
               x = 4
               y = 7 
               list_b = [2*3,4*5,x*y]
               print(list_b)

               What would the above code snippet output?
               """
               )

if answer == [6,20,28]: # check
    input('Correct!')
else:
    input("Sorry, that is incorrect")


input("""Let's break down this code snippet
x is set to 4 and y is set to 7")
The list then evaluates each arithmetic expression before outputting the list
      """)


print("Thank you for paying attention and learning some imperative programming today!")

exit()




    













