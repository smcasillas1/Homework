""" #1  Use the DateTime module to get Current Date and Time, and save it to a variable. 
Then extract just the Full month name form that variable. """
""" """ 

import datetime as dt_time

curr_dt = dt_time.datetime.now()
print(curr_dt)

print(curr_dt.strftime("%B"))


#2. Write a simple function that takes 2 parameters -- a first name and a day name. Have the function print out a greeting -- using the parameters -- that says something like "Hi first-name! Happy day-name!". 
# Remember to use the variables in the greeting to replace first-name and day-name.

   # Invoke this function with 2 variables.

def my_func(first_name, day_name):
    print("Hello, " + first_name + "! Happy " + day_name + "!")
my_func("Sam", "Sunday")
    
    # Invoke this function with 1 variable only.
def my_func2(day_name):
    print("Hello, Sam" + "! Happy " + day_name + "!")
my_func2("Sunday")

"""#3  Write a block of code to handle one of the most common Python exception errors. 
Select one of the common errors from the curriculum section on Python Exception handling.
Have your code example use
 the try,except, else, and finally components. """

#SyntaxError will be the Exception handling I will attempt

input_stmt = "hello"

try:
    prtin(input_stmt)
except:
    str(print("Please check your syntax"))
else:
    str(print(input_stmt))
finally:
    print("Thank you for practicing this exercise.")


