"""

Kilder:
https://snl.no/Norge
https://snl.no/Sverige
https://snl.no/Malaysia
https://snl.no/Canada
"""

import random

svar = {
    "Norge": {
        "hovedstad": "Oslo",
        "naboland": ["Sverige", "Finland", "Russland"],
        "innbygjarar": 5.5,
    },
    "Sverige": {
        "hovedstad": "Stockholm",
        "naboland": ["Norge", "Finland", "Danmark"],
        "innbygjarar": 10.5,
    },
    "Malaysia": {
        "hovedstad": "Kuala Lumpur",
        "naboland": ["Indonesia", "Singapore", "Thailand", "Filippinene"],
        "innbygjarar": 32.7,
    },
    "Canada": {
        "hovedstad": "Ottawa",
        "naboland": ["USA", "Grønnland"],
        "innbygjarar": 38.2,
    },
}

fikk_feil = []
fikk_riktig = []

tilfeldig_land = random.choice(list(svar.keys()))
print(f"Kva er hovedstaden i {tilfeldig_land}?")
if input() == svar[tilfeldig_land]["hovedstad"]:
    fikk_riktig.append(1)
else:
    fikk_feil.append(1)


tilfeldig_land = random.choice(list(svar.keys()))
print(f"Kva naboland har {tilfeldig_land}?")
print(svar[tilfeldig_land]["naboland"])
naboland = input()
if naboland == svar[tilfeldig_land]["naboland"]:
    fikk_riktig.append(2)
else:
    fikk_feil.append(2)

tilfeldig_land = random.choice(list(svar.keys()))
print(f"Kor mange (millioner) innbygjarar er det i {tilfeldig_land}?")
while True:
    try:
        gjett = float(input().replace(",", "."))
    except ValueError:
        print("Du må skrive et desimaltall!")
        continue
    else:
        break

if gjett == svar[tilfeldig_land]["innbygjarar"]:
    fikk_riktig.append(3)
else:
    fikk_feil.append(3)


print("Sluttvurdering:")
antall_spørsmål = 3
antall_riktige = len(fikk_riktig)
match antall_riktige:
    case 1:
        vurdering = "mindre bra"
    case 2:
        vurdering = "bra"
    case 3:
        vurdering = "kjempebra"
    case _:
        vurdering = "dårlig"

print(
    f"Du fekk {antall_riktige} av {antall_spørsmål} riktige svar. Dette er {vurdering}."
)

def liste_til_tekst(liste) -> str:
    tekst = ""

    if len(liste) == 1:
        tekst = liste[0]
    else:
        for i in range(len(liste)):
            if i == len(liste) - 1:
                tekst += " og "
            elif i > 0:
                tekst += ", "
            tekst += str(liste[i])

    return tekst


if len(fikk_feil) == antall_spørsmål:
    print("Du svarte feil på alle spørsmålene.")
elif len(fikk_riktig) == antall_spørsmål:
    print("Du svarte riktig på alle spørsmålene!")
else:
    print(f"Du svarte feil på spørsmål {liste_til_tekst(fikk_feil)}, og riktig på spørsmål {liste_til_tekst(fikk_riktig)}.")
