num = int(input("Enter number to check: "))

if num > 50:
    print("The number is greater than 50")
    if num % 2 == 0:
        print("and it's even.")
    else:
        print("and its odd.")
else:
    print("The number is less than 50")