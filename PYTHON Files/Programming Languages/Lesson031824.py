
y = int(input("\nEnter a number: "))
z = y
u=y
v=y
x = 1
c = 2

print("Activity 1")
for k in range(1,y+1):
    print (" "*(u-1), end="")
    for l in range(k,0,-1):
        print (l,end="")
    print()
    u=u-1

print()

print("Activity 2")
for x in range(1, y + 1, 2):
    print(" " * (y-1), end="")
    for i in range(1, x + 1):
        print(i, end="")
        print(" ", end="")

    print()
    y = y - 2

for a in range(z - 2, 0, -2):
    print(" " * c, end="")
    c = c + 2
    for b in range(1, a + 1):
        print(b, end="")
        print(" ", end="")
    print()
print()

print("Activity 3")
for q in range(1, v + 1):
    for w in range(1, v+ 1):
        if q == 1 or q == v:
            print(w, end="")
        else:
            spc = v - 4
            print(w, " " * spc, v, end="")
            break
    print()


1

