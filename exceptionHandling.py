"""
Exception Handling

-> Error: Errors occur due to mistakes in the code that prevent it from running. These can be syntax errors or logical errors.
    - Syntax Error:
        print("Hello Error" #here not given the closing bracket, this give me the syntax error
    - Indentation Errors:
        def func():
        print("Hello") #start with given any space or indentation
    There is one more tab error when you mix tabs and spaces.
    These error we cannot handled, but we can handle Exception.

-> Exception <-
Exceptions are unexpected events or errors that occurs
during the execution of a program, which disrupts the normal
flow of the program

try -> Wrap the block of code that might cause an exception.

except -> Handle the exception if it occurs

else -> Run code only if no exception occurs

finally -> Run code no matter what, whether there’s an exception or not

raise -> Manually throw an exception

"""
# print("Start")
# print(10/0) #this will give error ZeroDivisionError: division by zero
# print("End") #so this will never be exceuted
# num = int(input("tell your number: "))
# #now keep the division in try, because it can cause an exception
# try:
#     print(10/num)
# #now we dont know what kind of error will be there
# #except ZeroDivisionError:
# except Exception as err: 
#     print("This is your error which came: ", err)
# else:
#     print("This will run, when except block will not run")
# finally:
#     print("This will run, no matter what happen, this will run at last")

#Lets take about maunally raising the Error
age = int(input("Enter the Age: "))
try:
    if age < 10 or age > 18:
        raise ValueError("Your age must be in between 10 to 18")
    else:
        print("Welcome to the Club")
except Exception as err:
    print(f"An error occurred: {err}")
else:
    print("The Club will start soon")
