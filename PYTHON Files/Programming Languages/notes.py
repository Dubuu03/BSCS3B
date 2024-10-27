word=input("Enter Word: ")
vwl=0
cnst=0

for letter in word:
    if letter in "aeiouAEIOU":
        vwl+=1
    elif letter !=" ":
        cnst+=1

print("Vowel:",vwl)
print("Consonant:",cnst)

