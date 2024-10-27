D1= {
    "section": "BSCS 2B",
    "male": 20,
    "female": 22,
    "school":"CSU CARIG",
}
D1.pop("section")
D1["male"]= 26
D1["telno"]=232.23223
print(D1["school"])
print(D1["male"])
print(D1["telno"])

for x in D1.keys():
    print(x)
for y in D1.values():
    print(y)
for k, v in D1.items():
    print(f"Key: {k}, Value: {v}")
