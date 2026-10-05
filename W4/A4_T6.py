print("Program starting.")

n = int(input("Insert a positive integer: "))

print(n, end="")
steps = 0

while n != 1:
    if n % 2 == 0:
        n //= 2
    else:
        n = 3 * n + 1
    print(f" -> {n}", end="")
    steps += 1

print()
print(f"Sequence had {steps} total steps.")
print("Program ending.")