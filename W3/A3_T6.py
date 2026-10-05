def main():
    print("Program starting.")
    print("Welcome to the unit converter program!")
    print("Follow the menu instructions below.")
    print()
    print("Options:")
    print("1 - Length")
    print("2 - Weight")
    print("0 - Exit")
    main_choice = input("Your choice: ")
    if main_choice == "1":
        print()
        print("Length options:")
        print("1 - Meters to kilometers")
        print("2 - Kilometers to meters")
        print("0 - Exit")
        sub_choice = input("Your choice: ")
        if sub_choice == "1":
            val = float(input("Insert meters: "))
            res = val / 1000.0
            print(f"{val:.1f} m is {res:.1f} km")
        elif sub_choice == "2":
           val = float(input("Insert kilometers: "))
           res = val * 1000.0
           print(f"{val:.1f} km is {res:.1f} m")
        elif sub_choice == "0":
            print("Exiting...")
        else:
            print("Unknown option.")

    elif main_choice == "2":
        print()
        print("Weight options:")
        print("1 - Grams to pounds")
        print("2 - Pounds to grams")
        print("0 - Exit")
        sub_choice = input("Your choice: ")
        if sub_choice == "1":
            val = float(input("Insert grams: "))
            res = val / 453.59237
            print(f"{val:.1f} g is {res:.1f} lbs")
        elif sub_choice == "2":
            val = float(input("Insert pounds: "))
            res = val * 453.59237
            print(f"{val:.1f} lbs is {res:.1f} g")
        elif sub_choice == "0":
            print("Exiting...")
        else:
            print("Unknown option.")
    elif main_choice == "0":
        print("Exiting...")
    else:
        print("Unknown option.")

    print()
    print("Program ending.")

if __name__ == "__main__":
    main()