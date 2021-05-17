#!/usr/bin/env python3

# Author: Jamie Giannini

# Objectives: Create if statements using these logical conditionals below. Each statement should print information to the screen depending on if the condition is met:
# [X] Equals: a == b
# [X] Not Equals: a != b
# [X] Less than: a < b
# [X] Less than or equal to: a <= b
# [X] Greater than: a > b
# [X] Greater than or equal to: a >= b
# [X] Create an if statement using a logical conditional of your choice and include elif keyword that executes when other conditions are not met.
# [X] Create an if statement that includes both elif and else to execute when both if and elif are not met.
# Extra
# [X] Create an if statement with two conditions by using and between conditions.
# [X] Create an if statement with two conditions by using or between conditions.
# [X] Create a nested if statement.
# [X] Create an if statement that includes pass to avoid errors.
            
def if_func(a_val, b_val):
    try:
        # Converts A into integer (if possible)
        val_a = int(a_val)
    except ValueError:
        print("A entry is not a number, please try again.")
        quit() 
    
    try:
        # Converts B into integer (if possible)
        val_b = int(b_val)
    except ValueError:
        print("B entry is not a number, please try again.")
        quit()  
    
    if type(val_a) == int and type(val_b) == int:
        if val_a == 0 or val_b == 0:
            print("What did the 0 say to the 8? Nice belt!")
        elif val_a != val_b:
            print("A and B are not equal, and fun fact...")
            if val_a == 2 * val_b:
                print("A is twice the size of B!")
            elif val_b == 2 * val_a:
                print("B is twice the size of A!")
            elif val_a < val_b:
                print("A is less than B!")
            elif val_a > val_b:
                print("A is greater than B!")
        elif val_a == val_b:
            print("A is equal to B!") 
        #elif val_a <= val_b:
            #print("A is less than or equal to B!") 
        #elif val_a >= val_b:
            #print("A is greater than or equal to B!") # Neither will this
        else:
            print("Could not evaluate, please try again with different values.")
    else:
        pass # Testing pass

# Call function 

a_val = input('Enter a number (A): ')
b_val = input('Enter another number (B): ')

if_func(a_val, b_val)
