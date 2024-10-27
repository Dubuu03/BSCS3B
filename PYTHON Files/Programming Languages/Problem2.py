print("Problem 2\n")

quantity=int(input("Enter Quantity to order: "))
amount=int(input("Enter amount per quantity: "))

if quantity==1:
    charge = amount * 0
    actual = amount - charge
    full = actual * quantity
    print("Actual Amount: ",actual)
    print("Total Amount: ",full)

elif quantity==2:
    charge = amount * 0.05
    actual= amount-charge
    full = actual * quantity
    print("Actual Amount: ",actual)
    print("Total Amount: ",full)

elif quantity==3:
    charge = amount * 0.07
    actual= amount-charge
    full = actual * quantity
    print("Actual Amount: ",actual)
    print("Total Amount: ",full)

elif quantity>3:
    charge = amount * 0.1
    actual = amount - charge
    full = actual * quantity
    print("Actual Amount: ", actual)
    print("Total Amount: ",full)