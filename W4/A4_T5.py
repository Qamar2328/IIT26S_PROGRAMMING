print("Program starting.")

start = int(input("Insert starting point: "))
stop = int(input("Insert stopping point: "))
inspection = int(input("Insert inspection point: "))

valid = True

if start >= stop:
    print("Starting point value must be less than the stopping point value.")
    valid = False

if inspection < start or inspection > stop:
    print("Inspection value must be within the range of start and stop.")
    valid = False

if valid:
    print("First loop - inspection with break:")
    first = []
    for i in range(start, stop):
        if i == inspection:
            break
        first.append(str(i))
    print(" ".join(first))

    print("Second loop - inspection with continue:")
    second = []
    for i in range(start, stop):
        if i == inspection:
            continue
        second.append(str(i))
    print(" ".join(second))

print("Program ending.")
