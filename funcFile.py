"""
What are the function?
Functions in Python group reusable code into a block that
can be executed by calling the function name. This helps
avoid repetition and makes programs modular and readable.
There are many in-build functions in python like print(), input()
len() etc.
But you can create your own function and they are called as
user defined functions. To make your own function you have
to use def keyword and then name the function. After this
you have to call the function using name() and paranthesis.

-> Function Parameters and Arguments <-
Parameters are variables listed inside the function definition.
For making the function we have to accept inside the
parenthesis of the function.

Arguments are the Values passed to a function when it is called
"""
# def greet():
#     print("Hello Good Morning !!!")

#greet() #Calling the function

def greet(name): #so name is parameter, while function definition, we are accepting the name
    print(f"Hello Good Morning !!! {name}")

greet("Udai") #Udai is arguments, we are giving to the function

#Postional Arguments, in parameters, if we given a and b, and in argument if we passing the 12, 13, so it will goes to a and b respectively
def sum(a,b):
    return a+b
print("The sum of two number: ", sum(12,15))

#Now, we talk about the key arguments
def hello(name, age):
    print(f"Hello your name is {name} and your age is {age}")
hello("udai", 27) #this will print udai and 27
hello(27, "udai") #so now this will print name 27 and age udai, which is wrong
#now here we use the key argument to pass value in parameter names wise using key
hello(age=27,name="udai") #this is will run same, evenif it argument position changed

#Default Arugument
def add(a,b=45): #this b is given default argument
    return a+b
print(add(35))

## Ques: Check the string is palindrome or not
def checkPalindrome(str):
    #now start the loop to from back of string and add into new one
    rev = ""
    for i in range(len(str)-1, -1, -1):
        rev += str[i]

    if rev == str:
        print("String is Palindrome")
    else:
        print("String is not Palindrome")

checkPalindrome("Udai")
checkPalindrome("naman")