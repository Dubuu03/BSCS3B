

roman = {
     'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
}

invalid = [ "IIII", "VV", "XXXX", "LL", "CCCC", "DD", "MMMM", "IL", "IC", "ID", "IM", "VX", "VL", "VC",
            "VD", "VM", "XD", "XM", "LC", "LD", "LM", "DM", "IIV", "IIX", "XXC", "XXL", "CCD", "CCM"]



while True:

    total = 0
    prev_value = 0

    toconvert = input("Enter a Roman numeral: ").upper()

    if any(pattern in toconvert for pattern in invalid):
        print("Invalid Roman numeral. Please try again.")
        continue

    if not all(char in roman for char in toconvert):
        print("Invalid Roman numeral. Please try again.")
        continue

    for char in reversed(toconvert):
        current = roman[char]
        if current < prev_value:
            total -= current
        else:
            total += current
        prev_value = current

    print(total)

