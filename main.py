print("Hello Badhoo, Learning Python")
#This is single Line comment in PYTHON
#In python, we cant use multi line comments, But we can use the Doc String triple """"""
""""Hello This is multi Line Comment """

#In Python, you simple use Name as varibles, you can put the number, special char and space in starting of Varibale
#In Python you can use three way of Variable Naming convention
#1. Cammel Case :- yourName
#2. Pascal Case :- YourName
#3. Snake Case :- your_name

yourName = "Udai Chauhan" #cammel case
YourName = "Sandesh" #Pascal Case
your_name = "Baby Love" # Snake Case

# Data Types
# -> Numbers : All the numbers excluding decimal places and fraction.
your_age = 26

# -> Float : All the decimal numbers and fraction values are Float.
your_percentage = 89.90
your_number = 12/3
print(type(your_number))

# -> Complex : Numbers with real and imaginary parts are complex.
something_imaginer = 45j #as a imaginery number i need to use only j 
print('Type of Complex one', type(something_imaginer))

# -> String : This is used to store anything in python, literally anything that are available on your keyboard.
#You have to use quotes to store anything and it will be considered as string. You can use double Quotes (“”) or single quotes (‘’) to store both works same.
your_name = "Udai Chauhan. How are you, nice to meet you" #string
print(your_name)
print("type of string", type(your_name))

# -> Boolean : true or false
isAllowed = True #boolean data type
isAllowed = False
print(isAllowed) 
print("Type of Boolean ", type(isAllowed))

""" --> Strings <-- 
-> You know what strings are but you must also know string
take more space than other data types like int, float etc
-> This happens because String stores every character with
their own Unicode is a universal character encoding standard that
assigns a unique number (code point) to every character,
regardless of language Like “A” unicode is 65 and “ ” this emoji unicode is 128522,
you can check them by using ord() function in python and
convert them back using chr() function.
"""
char_var = "a"
print(ord(char_var))
unicode_var = 65
print(chr(unicode_var))

""" -> String Indexing 

You must have thought there are so many characters in a
string but can you access everyone. 
-> Yes thats possible using indexing. Indexing starts from 0 and
goes till the number of characters you have. 
-> There is negative indexing as well and it starts from -1, but
the starting position is from the back of the string
: eg - a = “Hello” print(a[0]) ==> output - “H

: eg - a = “Hello” print(a[-1]) ==> output - “o”

"""
name = "Udai Chauhan"
print("First Char of letter: " , name[0])
print("Thrid Char of letter: ", name[2])
print('Last Char of letter: ', name[-1])
print('Second Last char of letter: ', name[-2])

"""
-> String Slicing

Slicing means cutting out a slice from string and this is also
done using index values
-> So here we have start , stop and steps position and keep a
note if we use stop at 4 it will slice till 3 only.
"""
name = "Udai Chauhan"
print("First name:" , name[0:4:1]) #start: end: steps
print("First name something different way:", name[0:4:]) #we can left steps, by default it will be 1
print("Second Name:", name[5::1]) #if we want till last, we can skip the end value
print("Second Name some other way: ", name[5::]) # we can leave both blank by defalt it will goes till last and one steps

# -> Type Converstion
a = 12
print(type(a))
a = str(a)
print(type(a))

b = 12
print("divide: ", type(12/2)) #ans 6.0, type: float

# We have 7 falsy value => false, 0, 0.0, "", (), [], {}

#Implict Type Converstion, Python automatically convert behind the scene
#print(12/4) #3.0

#now_name = "Udai Chauhan"
#now_age = 27
#print("Hello My Name is ", now_name, "and my age is", now_age) #this is one way
#print(f"Hello My Name is {now_name} and my age is {now_age}") #tihis is how we use f formated string, to have calculation in string only

"""Taking Inputs
But the main question is how to ask user for some
information.
-> For example there is a user and you want to ask the age of that user, how can you do so, it’s easy using
-> Now the default data type of input is always string reason is simple you can store anything in string.
-> You have to manually convert the data type of input statements.

"""

#age = input("Enter Your Age ")
#print(f"This is your age {age} and typeof this var is {type(age)}") #so by default it will be String
#age = int(age)
#print("Now the type of age is ", type(age))

#Take the number change the int now from Input
#your_number = int(input("Enter your lucky number "))
#print(f"This is your selected number {your_number} and typeof this var is {type(your_number)}")


"""Operators
-> Arithmetic operators perform mathematical operations like
    addition, subtraction, multiplication, division, etc
-> There are 7 types of arithmetic operator.
addition +
subtraction -
multiplication *
division /
Floor division //
modulus %
Exponentiation **
"""
a = 10
b = 20
print("Addition ", a+b)
print("Substration ", a-b)
print("Multiplication ", a*b)
print("Division ", b/a, "type of this ", type(b/a))

#Floor Division is help us to remove the float value after the division, or simply it will change to int
print("Floor Division ", b//a, "type of this ", type(b//a))

print("Exponentiation ", 5**2) #5pow2, 5^2 = 25

print("Modulus ", 32%5) #this will give the reminder only 5*6=30, 2 left

"""
Assignment operators are used to assign values to variables.
Python also provides compound assignment operators that
perform operations like addition, subtraction, multiplication,
etc
A basic assignment operator is simple =.

Compound assignment operator combines arithmetic
operations with assignment
But first you have to understand how things work when we
reassign variables in python and also reassigning variables
with addition, subtraction etc
To understand watch the video carefully
Using compound assignment operators the reassigning
works better
+= Add and assigD
-= Subtract and assigD
*= Multiply and assignA
/= Divide and assigD
//= Floor divide and assigD
%= modulus and assigD
**= Exponentiation and assign
"""
assgn = 34 #simply assigning the 34 to variable

#Compound
a = 30
a += 10
a -= 10
a *= 5
a /= 6
a //= 5
print(a)
a %= 2

print(a)


"""
Comparison operators, also called relational operators, are
used to compare two values. Comparison operators will always provide Boolean result that
is True and False
-> comparison operators are as follow
== Equal t<
!= Not Equal to3
> Greater than3
< Less than 3
>= Greater than or equal t<
<= Less than or equal t<
Comparison operators will work with numbers but you can
use them with strings as well. Strings will be comparing the Ascii values of string.
"""
# print(10 == 10)
# print(10 != 10)
# print(6 > 4) #greater, True
# print(4 < 6) #lesser, True
# print(10 >= 10)
#print("A" > "B") #we can also compare string also in Python, compare the ASCII value, 65 > 66, false

"""
Logical operators in Python are used to combine multiple
conditions and return a Boolean result (True or False)
-> There are 3 types of logical operator3
and - Return True if both condition are Tru\
or - Return True if at least one condition is True
not - Reverse the boolean value
"""
# print(123 > 100 and 34 == 34) #True
# print(123 > 100 and 34 != 34) #False
# print(1234 > 100 or 34 != 34) #True, why because one is True

# print(not 12 == 12) #not True => False
# print((456 == 456) != (235 == 236)) #True
# print(12 < 10 or 45 == 56 or 69 > 70 or 15 != 13) #True
# print(True and bool(0)) #False


"""
-> Condition Statement

if - Executes if the condition is True*
5 if-else - Executes if True, another if Fals3
5 if-elif-else - Checks multiple condition in sequence.

"""
#If condition, excute something if the condition is true
# a = 9
# if a > 10:
#     print('Now A is greater than 10 means i am executing Task A') #see after colon this print start from after 5 space, this is indentation
# else:
#     print("Now a is not greater than 10 means i am executing Task B")

#IF ELSE
# money_given = int(input("Please Give me money: "))
# if money_given > 10:
#     print("Yeah Now I will buy the good ice creame")
# else:
#     print("Oh NO, I need to buy the little choco only")

#Now if-elif-else
# if money_given == 10:
#     print("I will buy ChocoBar Icecream")
# elif money_given == 20:
#     print('I will buy cone butter stoch icecream')
# else:
#     print('I need to go with Mongo Dolly')


#Q1. Accept two numbers and print the greatest between them.
# num_one = int(input("Enter Number One "))
# num_two = int(input("Enter Number Two "))
# if num_one > num_two:
#     print(f"Number One:{num_one} is greater than number two:{num_two}")
# elif num_two > num_one:
#     print(f"Number Two:{num_two} is greater than number one:{num_one}")
# else:
#    print("Both are the same")

# Q2. Accept the gender from the user as char and print the respective greeting message
#Ex - Good Morning Sir (on the basis of gender)
# your_gen = input("Please Enter Only Char of Your Gender (M or F)")
# if your_gen == 'M' or your_gen == 'm':
#     print("Good Morning Sir")
# elif your_gen == 'F' or your_gen == 'f':
#     print("Good Morning Maam, Have a Beautiful Day")
# else:
#     print('Please enter M or F only')

#Q3. Accept an integer and check whether it is an even number or odd.
# enter_number = int(input("Enter Your Number "))
# if enter_number%2 == 0:
#     print("This is even number")
# else:
#     print('This is odd number')

#Q5. Accept a year and check if it a leap year or not (google to find out what is a leap year)
#century year 2000, 3000, 1900, should be modulu by 100 and 400
# year = int(input("Enter Your Year"))
# if year%100 == 0 and year%400 == 0:
#     print('Its a Leap Year')
# elif year%100 != 0 and year%4 == 0:
#     print('Its a Leap Year')
# else:
#     print('Its a normal year')


# take the input of temperature in celsiusX
# @ Below 0°C → "Freezing Cold b
# @ 0°C to 10°C → "Very Cold b
# @ 10°C to 20°C → "Cold b
# @ 20°C to 30°C → "Pleasant b
# @ 30°C to 40°C → "Hot b
# @ Above 40°C → "Very Hot "
#temp = int(input("Enter the Temp in Cel: "))
# if temp < 0:
#     print('Freezing Cold')
# elif temp >= 0 and temp <= 10:
#     print('Very Cold')
# elif temp >= 10 and temp <= 20:
#     print('Cold')
# elif temp >= 20 and temp <= 30:
#     print('Pleasant Temp')
# elif temp >= 30 and temp <= 40:
#     print("Now its getting HOT")
# elif temp >= 40:
#     print("We get fucked!!, So HOTTTTT")
# else:
#     print('I dont know')