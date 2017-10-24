largest = None
smallest = None
values = []
while True:
    num = input("Enter a number: ")
    if num == "done" : break

    else:
        try:
            testNum = int(num)
        except:
            print('Invalid input')
            continue

    if largest is None:
        smallest = testNum
        largest = testNum
        values.append(smallest)
    else:
        values.append(testNum)

for numbertime in values:
    if numbertime < smallest:
        smallest = numbertime
    if numbertime > largest:
        largest = numbertime

print("Maximum is", largest)
print("Minimum is", smallest) 
