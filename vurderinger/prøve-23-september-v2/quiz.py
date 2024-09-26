"""
Kilder:
https://snl.no/Norge
https://snl.no/Sverige
https://snl.no/Malaysia
https://snl.no/Canada
"""

import random

fakta = {
    "norge": {
        "hovedstad": "oslo",
        "naboland": ["sverige", "finland", "russland"],
        "innbygjarar": 5.5,
    },
    "sverige": {
        "hovedstad": "stockholm",
        "naboland": ["norge", "finland", "danmark"],
        "innbygjarar": 10.5,
    },
    "malaysia": {
        "hovedstad": "kuala lumpur",
        "naboland": ["indonesia", "singapore", "thailand", "filippinene"],
        "innbygjarar": 32.7,
    },
    "canada": {
        "hovedstad": "ottawa",
        "naboland": ["usa", "grønnland"],
        "innbygjarar": 38.2,
    },
}

spørsmål = {
    "hovedstad": "Kva er hovedstaden i",
    "naboland": "Kva naboland har",
    "innbygjarar": "Kor mange (millioner) innbygjarar er det i",
}

fikk_feil = []
fikk_riktig = []

def still_spørsmål() -> bool:
    tilfeldig_land = random.choice(list(fakta.keys()))
    tilfeldig_spørsmål = random.choice(list(spørsmål.keys()))
    svar = fakta[tilfeldig_land][tilfeldig_spørsmål]

    print(f"{spørsmål[tilfeldig_spørsmål]} {tilfeldig_land}?")

    gjett = ""
    match tilfeldig_spørsmål:
        case "innbygjarar":
            try:
                gjett = float(input().replace(",", "."))
            except ValueError:
                # gir feil svar om ikke et tall
                return False 
            if gjett == svar:
                print("Jammen du er god med tall")
            if gjett > svar * 0.9 and gjett < svar * 1.1:
                return True

        case _:
            gjett = input().lower()

    return gjett == svar

antall_spørsmål = 3
for i in range(1, antall_spørsmål + 1):
    if still_spørsmål():
        fikk_riktig.append(i)
    else:
        fikk_feil.append(i)


print("Sluttvurdering:")
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
    if len(liste) == 1:
        return liste[0]

    tekst = ""
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
