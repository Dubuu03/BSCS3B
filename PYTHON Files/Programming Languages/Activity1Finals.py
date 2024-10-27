L1=[1,2,3,5.1,5.2,5.3,"aaa","bbb","ccc",["ddd", 2, 3.5], [4, 5.5, "eeee", True], [7, "hhh", 9.5],True,False]

sList=[]
c1=0
c2=0
c3=0
c4=0

sum1=0
sum2=0

print("Output 1:")
for i in L1:
    if type(i) is int:
        c1+=1
        sum1=sum1+i
print("Total:", c1)
print("Sum:", sum1)
print()

print("Output 2:")
for i in L1:
    if type(i) is list:
        for j in i:
            if type(j) is bool:
                c2+=1
print("Total:", c2)
print()

print("Output 3:")
for i in L1:
    if type(i) is str:
        c3+=1
        sList.append(i)
    elif type(i) is list:
        for j in i:
            if type(j) is str:
                c3 += 1
                sList.append(j)

print("Total:", c3)
print("String:",sList)
# print("String: ",end="")s
# for i in sList:
#     print(i,"",end="")
print(),

print("Output 4:")
for i in L1:
    if type(i) is bool:
        c4+=1
    elif type(i) is list:
        for j in i:
            if type(j) is bool:
                c4 += 1
print("Total:", c4)
print()

c5=0
print("Output 5:")
for i in L1:
    if type(i) is float:
        c5+=1
        sum2+=i
    elif type(i) is list:
        for x in i:
            if type(x) is float:
                c5+=1
                sum2+=x

print("Total:", c5)
print("Sum",sum2)
