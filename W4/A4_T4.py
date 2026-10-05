print("Program starting.")

words = 0
chars = 0

while True:
    word = input("Insert word (empty stops): ")
    if word == "":
        break
    words += 1
    chars += len(word)

print("You inserted:")
print(f"- {words} words")
print(f"- {chars} characters")
print("Program ending.")