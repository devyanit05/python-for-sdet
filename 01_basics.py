# message = 'Devyaniiiiiiiiiii'

# multiline_message = '''This
# It can span multiple lines.'''

# print(message[-6])
# print(message[3])
# print(message[0:6])
# print(multiline_message[4:10])
# print(multiline_message[4:15:2]) # first 10 characters, every second character
# print(message.lower())
# print(message.upper())
# print(message.replace('D', 'd'))
# print(message.split('y'))
# print('find: ' + str(message.find('vya'))) # returns the index of the first occurrence of the substring
# print(message.startswith('Dev'))
# print(message.endswith('ani'))
# print(len(message))
# print(message.count('i'))
# print(message.isalnum()) # checks if all characters are alphanumeric
# print(message.isalpha()) # checks if all characters are alphabetic
# print(message.isdigit()) # checks if all characters are digits

# greeting = 'Good morning,'
# name = input('Enter your name: ')
# formatted_message = '{} {}. Welcome!'.format(greeting, name)
# print(formatted_message)

# formatted_message_f = f'{greeting} {name.upper()}. Welcome!'
# print(formatted_message_f)

# number = 10

# print(dir(number)) # returns a list of all the attributes and methods of the object

# print(help(int.bit_length)) # returns the documentation of the object

# print(dir(name)) # returns a list of all the attributes and methods of the object

# print(help(str.find)) # returns the documentation of the object

# # ---------------------------------------------------------------------
# # Intergers and Floats
# # ---------------------------------------------------------------------

# num = 10
# print(type(num)) # returns the type of the object
# num = 10.5
# print(type(num)) # returns the type of the object

# # Arithmetic Operators
# a = 10
# b = 3
# print('Add: ' + str(a + b)) # addition
# print('Subtract: ' + str(a - b)) # subtraction
# print('Multiply: ' + str(a * b)) # multiplication
# print('Divide: ' + str(a / b)) # division
# print('Floor Divide: ' + str(a // b)) # floor division
# print('Modulus: ' + str(a % b)) # modulus
# print('Exponentiation: ' + str(a ** b)) # exponentiation
# print('Power: ' + str(pow(a, b))) # power
# print('Absolute: ' + str(abs(-a))) # absolute value
# print('Round: ' + str(round(3.14159, 2))) # round to 2 decimal places
# print('Round: ' + str(round(3.14159))) # round to nearest integer
# print('Round: ' + str(round(3.14159, 0))) # round to nearest integer
# print('Round: ' + str(round(3.14159, -1))) # round to nearest 10, explaination - rounding to the nearest 10 means that we are looking for the closest multiple of 10 to the number. In this case, 3.14159 is closer to 0 than it is to 10, so it rounds down to 0.
# print('Round: ' + str(round(3.14159, -2))) # round to nearest 100, explaination - rounding to the nearest 100 means that we are looking for the closest multiple of 100 to the number. In this case, 3.14159 is closer to 0 than it is to 100, so it rounds down to 0.
# print('Round: ' + str(round(32.14159, -1)))

# # Comparison Operators
# a = 10
# b = 20
# c = 'vjsv'
# d = 'ac'
# print('Equal: ' + str(a == b)) # equal to
# print('Not Equal: ' + str(a != b)) # not equal to
# print('Greater Than: ' + str(a > b)) # greater than
# print('Less Than: ' + str(a < b)) # less than
# print('Greater Than or Equal To: ' + str(a >= b)) # greater than or equal to
# print('Less Than or Equal To: ' + str(a <= b)) # less than or equal to

# # Logical Operators
# a = True
# b = False
# print('And: ' + str(a and b)) # and
# print('Or: ' + str(a or b)) # or
# print('Not: ' + str(not a)) # not

# # Bitwise Operators
# a = 10 # 1010
# b = 4  # 0100
# print('Bitwise AND: ' + str(a & b)) # bitwise and
# print('Bitwise OR: ' + str(a | b)) # bitwise or
# print('Bitwise XOR: ' + str(a ^ b)) # bitwise xor
# print('Bitwise NOT: ' + str(~a)) # bitwise not
# print('Bitwise Left Shift: ' + str(a << 1)) # bitwise left
# print('Bitwise Right Shift: ' + str(a >> 1)) # bitwise right

# # Assignment Operators
# a = 10
# b = 20
# a += b # a = a + b
# print('Addition: ' + str(a))

# # -------------------------------------------------------------------------
# # Lists
# # -------------------------------------------------------------------------

# courses = ['Python', 'Java', 'C++', 'JavaScript']
# courses_2 = ['Go', 'Rust', 'Kotlin'] 


# print(courses)
# print(courses[0]) # first element
# print(courses[-1]) # last element
# print(courses[0:2]) # first two elements
# print(courses[::2]) # every second element
# print(courses[::-1]) # reverse the list
# print(len(courses)) # length of the list
# print(courses.append('C#')) # add an element to the end of the list
# print(courses.insert(1, 'Go')) # add an element at a specific index

# courses.insert(1, courses_2) # add a list at a specific index
# print(courses)

# courses.extend(courses_2) # add a list to the end of the list
# print(courses)

# courses.remove('Java') # remove an element from the list
# print(courses)

# courses.pop() # remove the last element from the list
# print(courses)

# print(courses.pop()) 
# print(courses)

# courses.pop(1) # remove an element at a specific index
# print(courses)

# courses.sort() # sort the list in ascending order
# print(courses)

# courses.sort(reverse=True) # sort the list in descending order
# print(courses)

# cour  ses.reverse() # reverse the list
# print(courses)

# sorted_courses = sorted(courses) # sort the list in ascending order and return a new list
# print(sorted_courses)

# print(min(courses)) # return the minimum element in the list
# print(max(courses)) # return the maximum element in the list

# print(courses.index('Python')) # return the index of the first occurrence of the element

# print('Python' in courses) # check if the element is in the list
# print('Java' not in courses) # check if the element is not in the list

# for item in courses: # iterate through the list
#     print(item)

# for item in courses: # iterate through the list with index
#     print(courses.index(item), item, item.upper())

# courses = ['Python', 'Java', 'C++', 'JavaScript']

# for item in enumerate(courses): # iterate through the list with index
#     print(item)

# course_str = ', '.join(courses) # join the list into a string
# print(course_str)

# course_split = course_str.split(', ') # split the string into a list
# print(course_split)

# courses.clear() # remove all elements from the list
# print(courses)

# # -------------------------------------------------------------------------
# # Tuples
# # -------------------------------------------------------------------------

# # Lists are mutable and Tuples are immutable. Tuples are faster than lists. Tuples can be used as keys in dictionaries. 
# # Tuples can be used to return multiple values from a function.

# list1 = [1, 2, 3, 4, 5]
# tuple1 = (1, 2, 3, 4, 5)
# list2 = list1
# tuple2 = tuple1

# print(list1)
# print(list2)

# print(tuple1)
# print(tuple2)

# list1[0] = 10 # change the first element of the list
# print(list1)
# print(list2) # list2 is also changed because it is a reference to list1

# # tuple[0] = 10 # change the first element of the tuple
# print(tuple1) # this will give an error because tuples are immutable
# print(tuple2) # tuple2 is not changed because it is a reference to tuple1


# # -------------------------------------------------------------------------
# # Sets (sets are unordered collections of unique elements)
# # -------------------------------------------------------------------------

# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# print(set1)

# set3 = set2
# print(set3)

# set5 = {'Python', 'TypeScript', 'C#', 'JavaScript'}
# print(set5)

# set6 = {'Python', 'Java', 'C++', 'JavaScript', 'Python'} # duplicate elements will be removed
# print(set6)

# print('Python' in set5) # check if the element is in the set
# print('TypeScript' in set6) # check if the element is in the set

# print(set5.intersection(set6)) # intersection of two sets
# print(set5.difference(set6)) # difference of two sets
# set4 = set1.union(set2) # union of two sets
# print(set4)

# set5.add('Go') # add an element to the set
# print(set5)

# # set is used to store unique elements. It is unordered and unindexed. 
# # It is mutable but cannot contain mutable elements like lists or dictionaries.

# #-----------------------------------------------------------

# # Create an empty list, tuple, and set
# empty_list = []
# empty_list = list() # using the list constructor
# empty_tuple = ()
# empty_tuple = tuple() # using the tuple constructor
# empty_set = {} # this creates an empty dictionary, not a set
# empty_set = set() # using the set constructor

# # -------------------------------------------------------------------------
# # Dictionaries (dictionaries are unordered collections of key-value pairs)
# # -------------------------------------------------------------------------

# dictionary = {'name': 'Devyani', 'age': 25, 'city': 'New York', 'is_student': False, 'skills': ['Python', 'Java', 'C++', 'JavaScript'], 'worksAt': 'Regnology', 'address': {'street': '123 Main St', 'city': 'New York', 'state': 'NY', 'zip': '10001'}, 'phone_numbers': ['123-456-7890', '987-654-3210'], 'email': 'devyani@example.com', 1: 'true'}
# print(dictionary)
# print(dictionary['name']) # access the value of the key 'name'
# print(dictionary.get('age')) # access the value of the key 'age'
# print(dictionary.get('gender', 'Not specified')) # access the value of the key 'gender', if it doesn't exist, return 'Not specified'
# print()
# print(dictionary.keys()) # return a list of all the keys in the dictionary
# print()
# print(dictionary.values()) # return a list of all the values in the dictionary
# print()
# print(dictionary.items()) # return a list of all the key-value pairs in the dictionary

# dictionary['age'] = 26 # change the value of the key 'age'
# print(dictionary)

# dictionary.pop('city') # remove the key 'city' and return its value
# print(dictionary)

# dictionary.popitem() # remove the last key-value pair and return it
# print(dictionary)

# dictionary.update({'city': 'Los Angeles', 'is_student': True}) # update the dictionary with new key-value pairs
# print(dictionary)

# for key, value in dictionary.items(): # iterate through the dictionary
#     print(key, value)

# for value in dictionary:
#     print(value) # iterate through the keys of the dictionary

# for key in dictionary:
#     print(key) # iterate through the keys of the dictionary

# for value in dictionary.values():
#     print(value) # iterate through the values of the dictionary

# for v in dictionary.items():
#     print(v) # iterate through the key-value pairs of the dictionary

# print()

# for key in dictionary.keys():
#     print(key) # iterate through the keys of the dictionary
# print()
# for key, value in dictionary.items():
#     print(f'Key: {key}, Value: {value}') # iterate through the key-value pairs of the dictionary
# print()
# for key, value in dictionary.items():
#     print(value)