# Task
mydict_initial={"piekarnia": ["chleb","pączek","bułki"],
        "warzywniak": ["marchew", "seler","rukola"]}
mydict2=dict(mydict_initial)
print("Lista zakupów")
a=0
for x,y in mydict_initial.items():
    mydict2[x] = [a.capitalize() for a in mydict_initial[x]]
    print(f"Idę do {x.capitalize()} i kupuję tam {mydict2[x]}.")
    a = a+len(mydict2[x])
print(f"W sumie kupuję {a} produktów.")