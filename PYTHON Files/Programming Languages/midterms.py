print("Dustin Drix M. Narciso")

num=int(input("Enter a number (1-4): "))

st=9
f_end=5
s_end = 5
start = 0

if(num<1 or num>4):
    print("Invalid")
else:
    for i in range (num+1,1,-1):

        for spc in range (1,num+2-i):
            print(" ", end="")
        for j in range(1,f_end):
            print(st,"", end="")
            st-=1
        f_end-=1
        print()

    if num==4:
        start=1
    elif num==3:
        start=2
    elif num==2:
        start=3
    elif num==1:
        start=4

    for x in range (start,s_end):
        ##Print Space
        if num==3:
            for s in range (1,num+2-x):
                print(" ", end="")
        elif num==2:
            for s in range (1,num+3-x):
                print(" ", end="")
        else:
            for s in range (1,num+1-x):
                print(" ", end="")
        ##Print Column
        for z in range(1,x+1):
            print("*","", end="")
        s_end+=1
        print()


        

  
