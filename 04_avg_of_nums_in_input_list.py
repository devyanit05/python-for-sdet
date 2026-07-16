def avg(totalNums):
    total = 0
    try:
        for i in range(0,totalNums):
            total = total + myList[i]
            print("Current index: " + str(i))
            print("Current total: " + str(total))
        return float(total / totalNums)
    except TypeError:
        return "Invalid input"

myList = []

totalNums = int(input("How many numbers do you want to enter?"))

for i in range(0,totalNums):
    myList.append(float(input("Enter " + str(i+1) + "th number: ")))
    print("Current list: " + str(myList))

print(avg(totalNums))
