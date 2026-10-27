"""
-> In-built Data Structure <-
Data structures are used to store, organize, and manipulate
data efficiently. Python provides several built-in data
structures
- And for storing multiple values we will again use variablesD
- Now in python we have 4 types of in-build data structure List, Tuple, Dictionary, Set.

-> Custom Data Structure <-
-Now there are some custom data structures as well like Stack, Queue, Linked List, Graph etc.
- And around these data structures there are some algorithms like searching algorithms, sorting algorithms.

-> List Powers <-

Before starting we need to understand some of the
terminology.
- Mutability refers to whether an object's value can be changed after creation. And List allows this.
- we know data structures are used to store multiple values so duplicates means same value occuring multiple time. List allows this
- List maintains ordered data structure maintains the sequence of elements as they were inserted. This means you can access elements using their position (index)
- List have heterogenous nature that means we can have multiple data types inside the list.
"""
numbersList = [11, 12, 13, 14]
print(numbersList)
print("Show the Index 1 value: ", numbersList[1])
#Modifing the value of list, means we can Mutate
numbersList[1] = 22
print(numbersList) #[11,22,13,14]
print(type(numbersList))

#We can also have list of different type of value
# new_list = [11,12,14,True,"hello"]
# print(new_list)

#1st way to traverse on the list, this traverse is by range method and on Index
# for i in range(len(numbersList)):
#     print(numbersList[i])

#2nd way to traverse on the list is directly on list
# for val in numbersList:
#     print(val) 
print("--------------------------------")
""" Method of List """
#l = [11,12,13,14,10]
#l.append(15) #append the value at last of the list

#l.insert(0,10) #give the index where you want to insert, this will insert 10 at 0indx

#l.extend([15,16,17]) #this simple add this list at last to the main list

#l.remove(11) #remove the first occurrence of 11, only first occurrence

# popped_item = l.pop(3) #pop the element at index 3 and store into var
# print(popped_item)

# index = l.index(13) #this will tell the index of 13, which is 2
# print(index) #2

# count12 = l.count(12) #count the occurrence of the 12, which is 1
# print(count12) #1

#l.sort() #sort the list in asscending order

# new_list = l.copy() #simply create the copy of the list to new var
# print(new_list)

#l.clear() #Remove all the elements from the list
#print(l) #after the clear this will give the []

#Ques: Print Positive and Negative Number from the list
# l = [-1,10,-11,20,-2,45,-89,0,1,100,-101,101]
# pos_list = []
# neg_list = []
# for i in range(len(l)):
#     if(l[i] < 0):
#         neg_list.append(l[i])
#     else:
#         pos_list.append(l[i])
# print(f"This is list of positive number {pos_list} and this is of neg number {neg_list}")


# Ques: Mean of List elements
# l = [1,2,3,4,9,10,15]
# sum = 0
# for val in l:
#     sum += val
# print("The Meam of List: ", (sum//len(l)))

# Ques: Find the greatest element and print its index too?
# l = [10,1,34,678,999,11,15]
# largest = l[0] #take the first eleme as your largest elem
# idx = 0
# for i in range(len(l)):
#     if l[i] > largest:
#         largest = l[i] #so current elem is greater from the largest elem, change it
#         idx=i
# print(f"This is your greatest elem from list {largest} and this is your index {idx}")

# Ques: Find the second greatest element
# l = [12,16,13,19,17]
# largest = l[0]
# second_largest = l[0]
# for val in l:
#     if val > largest:
#         #now curr val is greater than the previous largest, so give this value to largest
#         #before that, leave the largest value to second largest
#         second_largest = largest
#         largest = val
#     elif val > second_largest:
#         second_largest = val

# print(second_largest, largest)

#From Geeks for Geeks
def getSecondLargest(self, arr):
        # code here
        largest = -1
        second_largest = -1
        for val in arr:
            if val > largest:
                second_largest = largest
                largest = val
            elif val > second_largest and val != largest: #this is to remove the duplicate
                second_largest = val
        if second_largest == -1:
            return -1
        else:
            return second_largest

# Ques: Check the list is sorted or not
#here we also learn, if break will run, for's else will not work and break will not work, else will work
# l = [12,13,14,15,16,1]
# for i in range(len(l)-1): #here i will go till len-1, because for checking we need to check the next index
#     if l[i] < l[i+1]:
#         continue #continue the loop as you are doing
#     else:
#         print("Your list is not sorted")
#         break
# else:
#     print("Your list is sorted")

print("-------- Tuples ----------")
"""
Before starting we need to understand some of the
terminology.
- Tuples are not mutable you cannot change the values of tuple -> Immutable
- You can have duplicate values in tuple there are no restriction
- Set are ordered and you can access them through index values
- Set also have heterogenous nature and can have different types of data structure in tuple.

syntax: a = ()

- Tuples are traversed in the same manner as List are traversed
- Tuples are same as String, String also immutable
"""
a = (1,2,3,4)
print(type(a)) #this will be shows as tuple <class 'tuple'>
print(a[1]) #this will print 2

t = (1,2,3,4,5,6)
print("Index of 6 in tuple: ", t.index(6)) #this will give the index of first occurrence of 6
print("Count of 3 in tuple: ", t.count(3)) #this will give the count of occurrence of 3

#Unpacking of tuple, into variable
a,b,c,d = (1,2,3,4)
print("a,b,c,d", a,b,c,d)

a = (1) #this will treat as simple int, because it gets implicit unpack
# print(type(a))
#if i add comma after one, Pyhton will know, you are creating tuple, and dont want to unpack
a = (1,)
# print(type(a))

print("-------- Set --------")
"""
Before starting we need to understand some of the
terminology.I
- Sets are mutable you can change the values of set.
- You cannot have any duplicate values in set that means every element will be unique
- Sets are unordered and you cannot access them through index values
- Set is semi-heterogenous it can store some data types like string, numbers, tuples but not everything

Each value in a set is hashed using a hash function (hash() in Python)
- The hash is used as an index to store the element in memory
- Since hashing does not maintain order, sets are unordered
- Only immutable (hashable) objects can be stored in a set
(e.g., numbers, strings, tuples). Mutable objects like lists and
dictionaries are not allowed

-> Set Traversing
A set cannot be traversed using the index values cause it is unordered and has no index
but yeah when we print the set, it can give the random order value, because it save data into hash form
"""
s = {} #this simple empty curly bracket is dictonary
s = {1,2,3,4,5,5,6,4}
print(s) #this is set, so it will remove duplicate 5 and 4
print(type(s))

# for val in s:
#     print(val)

"""
Now set methods are very powerful cause you don’t have
any indexing you cannot change the values but set is
mutable so we use methods for this
"""
#s.remove(2) #this will remove the 2, but will give the error, if not found
print("After removing of 2: ", s)
s.discard(2) #this is same as remove, it will also remove 2, but if not found, it wont give error
print("After discarding of 2: ", s)

# s.pop() this will remove the Random element in s
s.clear() #this will clear set
print("After the clear of set: ", s) 

a = {1,2,3}
b = {3,4,5}
#union_set = a.union(b) #{1,2,3,4,5}
#Or
# union_set = a | b
# print(union_set)

#intersection_set = a.intersection(b) #{3}, only 3 is common in both
#OR
# intersection_set = a&b
# print(intersection_set)

# difference_set = a.difference(b) #{1,2}
# difference_set2 = b - a #{4,5}
# print(difference_set2)

#symmetric_diff = a.symmetric_difference(b) #{1,2,4,5}, this will remove the common one
# symmetric_diff = b^a #still same {1,2,4,5}
# print(symmetric_diff)

print("--------- Dictionary ----------")
"""
Before starting we need to understand some of the terminology.

- Dictionaries are mutable, meaning you can change, add, or remove key-value pairs after creation
- Keys must be unique, but you can have duplicates in values
- Dictionary follows insertion order
- A dictionary can store different types of keys and values, like integers, strings, lists, or even another dictionary.

- Now we know we have to use key and value pairs to store values in dictionary
- And the keys in dictionary acts like index values that we use in List.
- we can perform CRUD(create, read, update, delete) operations on values but not all on keys cause the keys cannot be changed after creation.
"""
d = {}
print(type(d)) #<class 'dict'>
d = {"name": "udai", "age":27} #we cannot change the key, value can be change, we cant have the duplicate keys, but we have duplicate values
print(d)
print(d["name"])

"""
- We can traverse both keys and values in dictionary, but default loop is set on keys and you can access the values because of keys.
- So technically you can traverse on both keys and values at
the same time.
"""
numbers = {1:10, 2:20, 3:30, 4:40}
# for i in numbers:
#     print(f"Your key {i} : value {numbers[i]}")

#We can also change the vlaue of key, means we can mutate the dictonary
numbers[2] = 200 #updating
print(numbers) #{1: 10, 2: 200, 3: 30, 4: 40}

#now creating new key:value 
numbers[50] = 500
print(numbers) #{1: 10, 2: 200, 3: 30, 4: 40, 50: 500}

#deleting key of dict
del numbers[50]
print(numbers) #{1: 10, 2: 200, 3: 30, 4: 40}

#Traversing on only values of Dict, we can use the values()
# for val in numbers.values():
#     print(f"The value of numbers: {val}")

#Deep and Shallow Copy
a = [10,11,12,13,15]
#b = a #when we simply assign a to b, this means we are doing the Deep Copy, so if we change anything in b, it will reflect in a also

#Shallow Copy
# b = a.copy() #this is how we do Shallow Copy
# b[0] = 100 #here I have change in b, now i am printing a
# print(a)

# dict = {1:10, 2:20, 3:30, 4:40}
# dict.update({2:100})
# print(dict)
# print(dict.items())

#Ques: Write a Python script to merge two Python dictionaries?
d1 = {1:10,2:20,3:30}
d2 = {3:60, 4:40,5:50,6:60}
#This is one way to update the dictinary
# d1.update(d2) 
# print(d1)
#Second Way
# for val in d2:
#     d1[val] = d2[val]
# print(d1) 

#Ques: Write a Python program to sum all the values in a dictionary
sum = 0
for val in d1:
    sum += d1[val]
print("Sum of D1: ", sum)

#Ques: Count the frequency of each element
lst = [1,1,1,1,2,3,4,4,5,6,6,3,2]
countFrq = {}
for val in lst:
    if val in countFrq.keys():
        countFrq[val] += 1
    else:
        countFrq[val] = 1
print("Frequency of Number: ", countFrq)

#Ques: Write a Python program to combine two dictionary by adding values for common keys.
for i in d2:
    if i in d1.keys():
        d1[i] += d2[i]
    else:
        d1[i] = d2[i]
print("Combine Dict: ", d1)
