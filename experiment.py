'''
Arithmetic Operations
Add the numbers and the base motor will rotate first 45 then 60 and then finally 135 degrees
Picking up items and then adding them. 
For example, picking up an item 2 times and then picking up 
and dropping it 3 times and then picking and dropping it 5 times. 

import xarm

arm = xarm.Controller('USB')

def additive_rotating(first_degrees, second_degrees):
    degrees_sum = first_degrees + second_degrees
    arm.setPosition(2, degrees_sum)

def subtractive_rotating(first_degrees, second_degrees):
    degrees_difference = first_degrees - second_degrees
    arm.setPosition(2, degrees_difference)

def mulitplicative_rotating(first_degrees, multiplier):
    degrees_product = first_degrees * multiplier
    arm.setPosition(2, degrees_product)

def subtractive_rotating(first_degrees, divider):
    degrees_quotient = first_degrees // divider
    arm.setPosition(2, degrees_quotient)

'''








