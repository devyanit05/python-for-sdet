message = 'Devyaniiiiiiiiiii'

multiline_message = '''This
It can span multiple lines.'''

print(message[-6])
print(message[3])
print(message[0:6])
print(multiline_message[4:10])
print(multiline_message[4:15:2]) # first 10 characters, every second character
print(message.lower())
print(message.upper())
print(message.replace('D', 'd'))
print(message.split('y'))
print('find: ' + str(message.find('vya'))) # returns the index of the first occurrence of the substring
print(message.startswith('Dev'))
print(message.endswith('ani'))
print(len(message))
print(message.count('i'))
print(message.isalnum()) # checks if all characters are alphanumeric
print(message.isalpha()) # checks if all characters are alphabetic
print(message.isdigit()) # checks if all characters are digits

greeting = 'Good morning,'
name = input('Enter your name: ')
formatted_message = '{} {}. Welcome!'.format(greeting, name)
print(formatted_message)

formatted_message_f = f'{greeting} {name.upper()}. Welcome!'
print(formatted_message_f)

number = 10

print(dir(number)) # returns a list of all the attributes and methods of the object

print(help(int.bit_length)) # returns the documentation of the object

print(dir(name)) # returns a list of all the attributes and methods of the object

print(help(str.find)) # returns the documentation of the object

# ---------------------------------------------------------------------
# Intergers and Floats
# ---------------------------------------------------------------------

num = 10
print(type(num)) # returns the type of the object
num = 10.5
print(type(num)) # returns the type of the object

# Arithmetic Operators
a = 10
b = 3
print('Add: ' + str(a + b)) # addition
print('Subtract: ' + str(a - b)) # subtraction
print('Multiply: ' + str(a * b)) # multiplication
print('Divide: ' + str(a / b)) # division
print('Floor Divide: ' + str(a // b)) # floor division
print('Modulus: ' + str(a % b)) # modulus
print('Exponentiation: ' + str(a ** b)) # exponentiation
print('Power: ' + str(pow(a, b))) # power
print('Absolute: ' + str(abs(-a))) # absolute value
print('Round: ' + str(round(3.14159, 2))) # round to 2 decimal places
print('Round: ' + str(round(3.14159))) # round to nearest integer
print('Round: ' + str(round(3.14159, 0))) # round to nearest integer
print('Round: ' + str(round(3.14159, -1))) # round to nearest 10, explaination - rounding to the nearest 10 means that we are looking for the closest multiple of 10 to the number. In this case, 3.14159 is closer to 0 than it is to 10, so it rounds down to 0.
print('Round: ' + str(round(3.14159, -2))) # round to nearest 100, explaination - rounding to the nearest 100 means that we are looking for the closest multiple of 100 to the number. In this case, 3.14159 is closer to 0 than it is to 100, so it rounds down to 0.
print('Round: ' + str(round(32.14159, -1)))

# Comparison Operators
a = 10
b = 20
c = 'vjsv'
d = 'ac'
print('Equal: ' + str(a == b)) # equal to
print('Not Equal: ' + str(a != b)) # not equal to
print('Greater Than: ' + str(a > b)) # greater than
print('Less Than: ' + str(a < b)) # less than
print('Greater Than or Equal To: ' + str(a >= b)) # greater than or equal to
print('Less Than or Equal To: ' + str(a <= b)) # less than or equal to

# Logical Operators
a = True
b = False
print('And: ' + str(a and b)) # and
print('Or: ' + str(a or b)) # or
print('Not: ' + str(not a)) # not

# Bitwise Operators
a = 10 # 1010
b = 4  # 0100
print('Bitwise AND: ' + str(a & b)) # bitwise and
print('Bitwise OR: ' + str(a | b)) # bitwise or
print('Bitwise XOR: ' + str(a ^ b)) # bitwise xor
print('Bitwise NOT: ' + str(~a)) # bitwise not
print('Bitwise Left Shift: ' + str(a << 1)) # bitwise left
print('Bitwise Right Shift: ' + str(a >> 1)) # bitwise right

# Assignment Operators
a = 10
b = 20
a += b # a = a + b
print('Addition: ' + str(a))

# -------------------------------------------------------------------------
# Lists
# -------------------------------------------------------------------------

courses = ['Python', 'Java', 'C++', 'JavaScript']


print(courses)
print(courses[0]) # first element
print(courses[-1]) # last element
print(courses[0:2]) # first two elements
print(courses[::2]) # every second element
print(courses[::-1]) # reverse the list
print(len(courses)) # length of the list


