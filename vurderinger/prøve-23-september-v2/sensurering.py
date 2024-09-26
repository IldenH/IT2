import random

stygge_ord = {
    "fis": "promp",
    "fisen": "prompen",
    "fisens": "prompens",
    "stygtord1": "sniltord1",
    "stygtord2": "sniltord2",
    "stygtord3": "sniltord3",
    "stygtord4": "sniltord4",
    "stygtord5": "sniltord5",
}
aksepterte_ord = ["FIS"]
sensur_tegn = ["#", "&", "%"]


def skal_sensureres(ord: str) -> bool:
    if ord in aksepterte_ord:
        return False
    return ord.lower() in stygge_ord


def tilfeldig_sensurert(ord: str) -> str:
    sensurert = ""
    for _ in range(len(ord)):
        sensurert += random.choice(sensur_tegn)

    return sensurert


def sensur_uleselig(tekst: str) -> str:
    for ord in tekst.split():
        if skal_sensureres(ord):
            tekst = tekst.replace(ord, tilfeldig_sensurert(ord.lower()))

    return tekst


def sensur_erstatning(tekst: str) -> str:
    for ord in tekst.split():
        if skal_sensureres(ord):
            tekst = tekst.replace(ord, stygge_ord[ord.lower()])

    return tekst


test_data = [
    "Den som fisen først er var, den er fisens rette far",
    "FIS globally governs skiing and snowboarding and oversees over 7000 events annually in Alpine, Cross-Country, Ski Jumping, Nordic Combined and many more.",
    'Fiskal blir benyttet om det som har med statskassen eller regnskap å gjøre, som for eksempel "fiskale avgifter" (statlige avgifter), eller "det fiskale året 2005" (regnskapsåret 2005). Fiskale skatter og avgifter har til formål å skaffe inntekter til staten.',
    "Oppskrifter med fisk og sjømat for alle, til middag, lunsj og fest. Lær om behandling av fisk og sjømat.",
]


print("Tekstene uten sensurering:")
for setning in test_data:
    print(setning)

snike_seg_unna_tegn = ["#", "_", "*"]
for i in range(len(test_data)):
    for tegn in snike_seg_unna_tegn:
        test_data[i] = test_data[i].replace(tegn, "")

print("\nTekstene med uleselig sensurering:")
for setning in test_data:
    print(sensur_uleselig(setning))


print("\nTekstene med erstadende sensurering:")
for setning in test_data:
    print(sensur_erstatning(setning))
