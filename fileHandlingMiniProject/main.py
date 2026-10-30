from pathlib import Path #here we are importing file, to know about th e current path
import os

def readFileAndFolder():
    #path = Path('') #this will give the current path
    #items = list(path.rglob('*')) #this rglob, this will read all file and make a list and put into items

    #this will give current folder
    path = Path('fileHandlingMiniProject')
    items = list(path.iterdir())
    for i, item in enumerate(items):
        print(f"{i+1} : {item}")


#In this function we will create the file, but before that we list down all the file which is present in folder
BASE_DIR = Path('fileHandlingMiniProject')
def createFile():
    try:
        readFileAndFolder()
        name = input("Enter the name of your file: ")
        p = BASE_DIR/name

        #here i am checking the file name duplicate
        if p.exists():
            print("This file already exists.")
            return
        
        with open(p, 'w') as fs:
            data = input("Write what you want to write in file: ")
            fs.write(data)
    except Exception as err:
        print(f"An error occurred as {err}")
    else:
        print("File Created Succesfully")



def readFile():
    readFileAndFolder()
    name = input("Enter the file which you want to read: ")
    p = BASE_DIR/name

    if p.exists() and p.is_file():
        with open(p, 'r') as fs:
            print(fs.read())
    
        print("File Read Successfully")
    else:
        print("File doesnot exists")

def updateFile():
    readFileAndFolder()
    try:
        name = input("Tell which file you want to update :- ")
        p = BASE_DIR / name

        if not (p.exists() and p.is_file()):
            print("Sorry, this file does not exist.")
            return

        print("Press 1 for changing the name of your file")
        print("Press 2 for overwriting the data of your file")
        print("Press 3 for appending some content to your file")

        res = int(input("Tell Me Your Response :- "))

        if res == 1:
            name2 = input("Tell your new file name :- ")
            p2 = BASE_DIR / name2
            if p2.exists():
                print("A file with that name already exists.")
                return
            p.rename(p2)
            print("FILE RENAMED SUCCESSFULLY")

        elif res == 2:
            data = input("Tell what you want to overwrite :- ")
            with open(p, 'w') as fs:
                fs.write(data)
            print("FILE OVERWRITTEN SUCCESSFULLY")

        elif res == 3:
            data = input("Tell what you want to append :- ")
            with open(p, 'a') as fs:
                fs.write(" " + data)
            print("DATA APPENDED SUCCESSFULLY")

        else:
            print("Invalid option. Please choose 1, 2 or 3.")

    except ValueError:
        print("Please enter a number (1, 2 or 3).")
    except PermissionError:
        print("You don't have permission to modify this file.")
    except OSError as err:
        print(f"Something went wrong with the file: {err}")

def deleteFile():
    readFileAndFolder()
    name = input("Which file you want to delete :- ")
    p = BASE_DIR / name
    if not (p.exists() and p.is_file()):
        print("This file name is not exsists in sytem")
    else:
        os.remove(p)
        print("file removed successfully")

print("Hello! Welcome to File Handling Mini Project.")

print("Press 1 for creating a file: ")
print("Press 2 for reading a file: ")
print("Press 3 for updating a file: ")
print("Press 4 for deleting a file: ")

num = int(input("Please Tell Your Response:- "))

if num == 1:
    createFile()
elif num == 2:
    readFile()
elif num == 3:
    updateFile()
elif num == 4:
    deleteFile()
else:
    print("Please enter the correct Number")