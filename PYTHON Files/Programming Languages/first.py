import datetime as dt

print("Cagayan State University\n")

a=45.41232
b=56412231
c=56.5656
d="CSU"
e=-45

print("Fisrt: " +  str(a) + "\nSecond: "+str(b)+"\nThrid: " + str(c) + "\nFourth: "+ d)
print("\nA: {} B: {:,} C: {} D: {}" .format(a,b,c,d))
print("A: {1} B: {3} C: {2} D: {0}" .format(a,b,c,d))
s1="A: {2:.2f} B: {0: .2f} C: {1} D: {3}"
print(s1.format(a,b,c,d))

print("\nThe {z} jumps {y} the rainbow" .format(z="dog",y="over"))

print("\nThe {0:>10} is far".format(d))
print("The {0:<10} is far".format(d))
print("The {0:^10} is far".format(d))

print("\n{0:=10} petot".format(e))
print("{0:-10} petot".format(e))

d=dt.datetime.now();
print("\nDate and Time")
print("A: ", d.strftime("%A"),"\t\t\t\ta: ",d.strftime("%a"))
print("B: ", d.strftime("%B"),"\t\t\tb: ",d.strftime("%b"))
print("C: ", d.strftime("%C"),"\t\t\t\t\tc: ",d.strftime("%c"))
print("D: ", d.strftime("%D"),"\t\t\td: ",d.strftime("%d"))
print("F: ", d.strftime("%F"),"\t\t\tf: ",d.strftime("%f"))
print("G: ", d.strftime("%G"),"\t\t\t\tg: ",d.strftime("%g"))
print("H: ", d.strftime("%H"),"\t\t\t\t\th: ",d.strftime("%h"))
print("I: ", d.strftime("%I"))
print("\t\t\t\t\t\tj: ", d.strftime("%j"))
print("M: ", d.strftime("%M"),"\t\t\t\t\tm: ",d.strftime("%m"))
print("\t\t\t\t\t\tp: ", d.strftime("%p"))
print("R: ", d.strftime("%R"),"\t\t\t\tr: ",d.strftime("%r"))
print("S: ", d.strftime("%S"))
print("T: ", d.strftime("%T"))
print("U: ", d.strftime("%U"),"\t\t\t\t\tu: ",d.strftime("%u"))
print("V: ", d.strftime("%V"))
print("W: ", d.strftime("%W"),"\t\t\t\t\tw: ",d.strftime("%w"))
print("X: ", d.strftime("%X"),"\t\t\tx: ",d.strftime("%x"))
print("Y: ", d.strftime("%Y"),"\t\t\t\ty: ",d.strftime("%y"))
print("Z: ", d.strftime("%Z"),"\t\t\t\t\tz: ",d.strftime("%z"))

print("\nBackslash")
print("a: \a A")
print("b: \b B")
print("f: \f F")
print("n: \n N")
print("r: \r R")
print("t: \t T")
print("v: \v V")










