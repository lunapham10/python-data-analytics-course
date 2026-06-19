print("Calculator")
first_number = int(input("Give the first number: "))
second_number = int(input("Give the second number:"))

while True:
    print("(1) +")
    print("(2) -")
    print("(3) *")
    print("(4) /")
    print("(5)Change numbers")
    print("(6)Quit")
    print(f"Current numbers: {first_number} {second_number}")
    select_number = int(input("Please select something (1-6): "))
    if select_number == 6:
        print("Thank you!")
        break
    elif select_number == 1:
        print(f"The result is: {first_number+second_number}")
    elif select_number == 2:
        print(f"The result is: {first_number-second_number}")
    elif select_number == 3:
        print(f"The result is: {first_number*second_number}")
    elif select_number == 4:
        print(f"The result is: {first_number/second_number}")
    elif select_number == 5:
        first_number = int(input("Give the first number: "))
        second_number = int(input("Give the second number: "))
    else:
        print("Selection was not correct.")
