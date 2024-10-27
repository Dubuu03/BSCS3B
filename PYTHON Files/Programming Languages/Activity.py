def computation(number):
    if number < 1 or number > 99:
        return print("Out of Range")

    while number != 1:
        if number % 2 == 0:
            next_number = (number // 2)
            print(number, "/ 2 =", next_number)
        else:
            next_number = int(number * 3 + 1)
            print(number, "* 3 + 1 =", next_number)

        number = next_number


number = int(input("Enter a Number (1-99): "))
computation(number)