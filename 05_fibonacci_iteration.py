# fibonacci sequence is a sequence of numbers where each number is the sum of the two preceding ones, starting from 0 and 1.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

# code through iteration
fibonacciList = []

def fibonacci(index):
    num1 = 0
    num2 = 1
    for i in range(0,index):
        num3 = num1 + num2
        fibonacciList.append(num3)
        num1 = num2
        num2 = num3
    return fibonacciList

index = int(input("Enter the index of the fibonacci sequence upto which you want to print: "))

newList =fibonacci(index)
print(newList)