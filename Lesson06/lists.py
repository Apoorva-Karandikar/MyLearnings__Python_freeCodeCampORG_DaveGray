users = ['Apoorva','Madakini','Bhaskar']
data = ['Apoorva', 48, True]
emptylist = []

print()

print("Apoorva" in users)
print("Apoorva" in data)
print("Apoorva" in emptylist)

print()
print(users[0])
print(users[-1])
print(users[-2])
""" print(users[3]) # out of index error
print(users[-4]) """

print()
""" print('Index position of Apoorva is : ' + (users.index('Apoorva')))
TypeError: can only concatenate str (not "int") to str """

print(users.index('Apoorva'))
print(users[0:2])
print(users[0:])
print(users[-3:-1])

print()
print(users[0:-1])
print(users[:-1])
print(users[-3:0])
print(users[:0])

print()
""" print("Length of list is : " + len(data))
TypeError: can only concatenate str (not "int") to str """

print(len(data))

print('\n ~~~~  Appending to end of list  ~~~~ \n')
users.append('Premala')
print(users)

users += ['Harishchandra']
print(users)

users += 'Naina'    # each character considered separate string without the []
print(users)

users.extend(['Uma','Shivaram'])
print(users)
print()

print('\n ~~~~  Concatinating lists ~~~~ \n')
users.extend(data)
print(users)
print()

print('\n ~~~~ Inserting / Updating at a specific index ~~~~ \n')
users.insert(5, 'Aniruddha')
print(users)

users[6:6] = ['Jane', 'John']   # insert at a position 
print(users)

users[6:8] = ['Jenny', 'Johnny']    # replace specific positions (range is called slice)
print(users)
print()

print('\n ~~~~  Deleting from lists ~~~~ \n')
users.remove('Johnny')
print(users)

print(users.pop())
print(users)

""" users = users.remove(users.pop())
ValueError: list.remove(x): x not in list """

del users[-1]
print(users)

print()
print(data)

""" del data
print(data)
NameError: name 'data' is not defined """

data.clear()
print(data)
print()

print("\n ~~~~  Sorting lists   ~~~~ \n")

""" data += ['Sort']
print(data)
data.extend(users.sort())
TypeError: 'NoneType' object is not iterable
print(data) """

print()

""" print("\n\n")
print(data)
data += sorted(users, key=str.lower)
print(data)
print(users)
print("\n\n") """

users.sort()    # Sorts using ASCII values. Hence first, all starting with numerals first, followed by all starting with capital letters, lastly all starting with lower case letters       # Modifies the original list with sorted values 
print(users)

users.sort(key=str.lower)
print(users)
print()


nums = [48, 4, 84, 8, 44]
print(nums)
nums.reverse()  # reversers contents of list based on index value / position 
print(nums)
print()

""" nums.sort(reverse=True) # sorts in reverse order based on the values of the items in the list 
print(nums)
print() """

print(sorted(nums, reverse=True))  # Prints sorted values from the list without making any changes to the actual list
print(nums)
print()

print("\n ~~~~  Copying lists   ~~~~ \n")
numscopy = nums.copy()
mynums = list(nums) # creating a copy of a list using a constructor function 
mycopy = nums[:]    # slice and copy only a certain index range

print(nums)
print(numscopy)
print(mynums)
print(mycopy.sort())
print(mycopy)
print(nums)
print()

print("\n ~~~~  Checking the data type of a list   ~~~~ \n")
print(type(nums))

mylist1 = list([1, 'Single quotes', False])
print(mylist1)
print(type(mylist1))
mylist2 = list([2, "Double quotes", True])
print(mylist2)
print(type(mylist2))
print()


print("\n\n !~~~! Tuples  !~~~! \n")

myConstructorTuple = tuple(('Apoorva', 84, False))
anotherTuple = (444, 888, 444, 'Naina', 444, 484, 848, 'Naina') # assigning values to a tuple is called 'packing the tuple' 
print(myConstructorTuple)
print(type(myConstructorTuple))
print(anotherTuple)
print(type(anotherTuple))
print()

print("\n ~~~~  Modifying tuples    ~~~~ \n")
# tuples cannot be modified directly 
newlist = list(myConstructorTuple)
newlist.append('Naina')
newtuple = tuple(newlist)

print(newlist)
print(type(newlist))
print(newtuple)
print(type(newtuple))
print(myConstructorTuple)   # original tuple remains unchanged 
print()

print("\n ~~~~  Unpacking tuples    ~~~~ \n")
print(anotherTuple)
(one, *two, hey) = anotherTuple
print(one)
print(type(one))
print(two)
print(type(two))
print(hey)
print(type(hey))
print()

print("\n ~~~~  Functions on lists and tuples   ~~~~ \n")
print(anotherTuple.count(444))
print(anotherTuple.count('Naina'))



print()
