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
print(12/4) #3.0

now_name = "Udai Chauhan"
now_age = 27
print("Hello My Name is ", now_name, "and my age is", now_age) #this is one way
print(f"Hello My Name is {now_name} and my age is {now_age}") #tihis is how we use f formated string, to have calculation in string only

"""Taking Inputs
But the main question is how to ask user for some
information.
-> For example there is a user and you want to ask the age of that user, how can you do so, it’s easy using
-> Now the default data type of input is always string reason is simple you can store anything in string.
-> You have to manually convert the data type of input statements.

"""

age = input("Enter Your Age ")
print(f"This is your age {age} and typeof this var is {type(age)}") #so by default it will be String
age = int(age)
print("Now the type of age is ", type(age))

#Take the number change the int now from Input
your_number = int(input("Enter your lucky number "))
print(f"This is your selected number {your_number} and typeof this var is {type(your_number)}")