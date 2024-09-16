person = {
    "1": {"fornavn": "navn", "etternavn": "navnesen"},
    "2": {"fornavn": "navn2", "etternavn": "navnesen2"},
}

print(person["1"]["fornavn"])
print(person["2"]["etternavn"])

person["2"]["alder"] = 33
person["1"].pop("fornavn")

print(person)

[print(key) for key in person.keys()]
[print(value) for value in person.values()]
[print(key, value) for key, value in person.items()]  # returnerer en tuppel

tuppel = ("fornavn", "Per")
a = tuppel[0]
b = tuppel[1]
a, b = tuppel
