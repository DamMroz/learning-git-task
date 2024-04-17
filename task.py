# Task
mydict_initial={"piekarnia": ["chleb","pączek","bułki"],
        "warzywniak": ["marchew", "seler","rukola"]}
mydict2=dict(mydict_initial)
print("Lista zakupów")
element=0
for x,y in mydict_initial.items():
    mydict2[x] = [element.capitalize() for element in mydict_initial[x]]
    print(f"Idę do {x.capitalize()} i kupuję tam {mydict2[x]}.")
    element = element+len(mydict2[x])
print(f"W sumie kupuję {element} produktów.")
