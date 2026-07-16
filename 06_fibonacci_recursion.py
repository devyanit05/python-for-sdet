# fibonacci sequence is a sequence of numbers where each number is the sum of the two preceding ones, starting from 0 and 1.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

# simple recursive fibonacci

def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

index = int(input("Enter the index of the fibonacci sequence up to which you want to print: "))
myList = []
for i in range(0,index):
    myList.append(fibonacci(i))
print(myList)

