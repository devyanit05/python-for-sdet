num1 = 100
num2 = 20

def swap(num1, num2):
    try:
        num1 = num1 + num2 #120
        num2 = num1 - num2 #100
        num1 = num1 - num2 #20
        return num1, num2
    except TypeError:
        return "Invalid input"

print(swap('num1', 'num2'))
num1, num2 = swap(num1, num2)
print(num1, num2)

