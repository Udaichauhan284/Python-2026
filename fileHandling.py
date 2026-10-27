"""
-> File Handling <-
File handling means Creating, Reading, Updating, Deleting(CRUD) operations that we can perform in files.
- We have to use open() function to open a file in python.

'r' -> Read (default) – file must exist.

'w' -> Write – creates file or overwrites.

'a' -> Append – adds to end of file.

'x' -> Create – creates a new file, fails if it exists
"""
# file = open(r'/Users/udaichauhan/Development/Python 2026/testing.txt')
# print(file.read())

# file = open("superman.txt", 'w') #this will create the new file, or overwrites it
file = open("superman.txt", 'a') #this will append the data into file
file.write("Hello I am in this file, And i am writing from main.py file. I hope you doing good. Hello this is append line")
file.close()