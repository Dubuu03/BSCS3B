# L2=[1,2,3,4,"a","b","c", [11,22,33,"a"]]
# sum=0
# for i in L2:
#     if type(i) is list:
#         for x in i:
#             if type(x) is int:
#                 sum+=x
# print(sum)
#
MDL1 = [[ 1,2,3,[11,22,33]],
         [4,5,6],
         [7,8,9],
         [8,"drix",7]]

print(len(MDL1))
print(MDL1[0][1])
for i in MDL1:
    print(i)

for x in MDL1:
    for y in x:
        print(y,end="")
    print()

# for i in MDL1:
#     if type(i) is list:
#         for j in i:
#             if type(j) is list:
#                 print(j)

sum=0
row=1
for i in MDL1:
    if type(i) is list:
        for x in i:
            if type(x) is int:
                sum+=x
        print("Sum of Row",row ,"=",sum)
        row+=1
        sum=0


s="CSUCARIG"
print(s[3:])
print(s[:3])
print(s[3:5])

print(MDL1[0][3][1])