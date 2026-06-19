def checking_even():
    while True:
        number = int(input("Give a number: "))
        if number % 2 == 0:
            print("The given number was even.")
            break

if __name__ == "__main__":
    checking_even()
