mydict={"piekarnia": ["chleb","pączek","bułki"],
        "warzywniak": ["marchew", "seler","rukola"]}
mydict2=dict(mydict)
print("Lista zakupów")
a=0
for x,y in mydict.items():
    mydict2[x] = [a.capitalize() for a in mydict[x]]
    print(f"Idę do {x.capitalize()} i kupuję tam {mydict2[x]}.")
    a = a+len(mydict2[x])
print(f"W sumie kupuję {a} produktów.")