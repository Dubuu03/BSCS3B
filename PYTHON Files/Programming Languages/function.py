
def displayName():
    print("Juan Dela Cruz")

def displayName1(n,x):
    print(n,x)

def displayName2(n1,n2):
    s=n1,n2
    return s

def displayAge(a):
    return a

def genAve(p,m,f):
    return (p+m+f)/3

def grade(g):
    if g>74:
        r="Passed"
    else:
        r= "Failed"
    return r



displayName()
displayName1("Juan" ,"Dela Cruz")
print(displayName2("aaa","bbb"))
print("Age:",displayAge(20))
print("Grade: {0:2f}".format(genAve(97,98,95)))
print(grade(98))

l1=lambda x: print(x)
l1("Juan")
l2=lambda x:x+5
l3=lambda x,y:x*y
l4 = lambda g: "Passed" if g>74 else "Failed"
l5 = lambda f: "A" if f>95 \
                else "B" if f>90 \
                else "Failed"
print(l2(4342))
print(l3(7,9))
print(l4(74))
print(l5(93))


