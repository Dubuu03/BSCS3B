print("Problem 1\n")

name=(input("Enter Name of Customer: "))
num=int(input("K/watts Consumed: "))

if num<5:
    amount = num * 5
    sur = 0
    total = amount + sur
    print("Amount",amount)
    print("Surcharge: " , sur)
    print("Total Amount: ", total)

elif num < 10:
    amount = num * 7
    sur = 0
    total = amount + sur
    print("Amount",amount)
    print("Surcharge: " , sur)
    print("Total Amount: ", total)

elif num < 15:
    amount = num * 9
    sur = 0
    total = amount + sur
    print("Amount",amount)
    print("Surcharge: " , sur)
    print("Total Amount: ", total)

elif num > 14:
    amount = num * 10
    sur = amount * 0.05
    total = amount+sur
    print("Amount",amount)
    print("Surcharge: " , sur)
    print("Total Amount: ", total )






