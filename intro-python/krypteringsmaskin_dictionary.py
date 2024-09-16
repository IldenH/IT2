"""
Lag en ordbok som følger dette mønsteret: krypter = { "a": "c", "b": "d", "c": "e", … }. (Alle nøklene gir en bokstav som ligger to bokstaver etter i alfabetet.)
"""

krypter = {
    "a": "c",
    "b": "d",
    "c": "e",
    "d": "f",
    "e": "g",
    "f": "h",
    "g": "i",
    "h": "j",
    "i": "k",
    "j": "l",
    "k": "m",
    "l": "n",
    "m": "o",
    "n": "p",
    "o": "q",
    "p": "r",
    "q": "s",
    "r": "t",
    "s": "u",
    "t": "v",
    "u": "w",
    "v": "x",
    "w": "y",
    "x": "z",
    "y": "a",
    "z": "b",
}

tekst = "en veldig fin og lang tekst som ikke inneholder bokstaver utenfor det latinske alfabetet."
kryptert_tekst = ""

for bokstav in tekst:
    if bokstav in krypter:
        kryptert_tekst += krypter[bokstav]
    else:
        kryptert_tekst += bokstav

print(tekst)
print(kryptert_tekst)
