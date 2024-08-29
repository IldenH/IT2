import random

mulige_trekk: list[str] = ["stein", "saks", "papir"]


def spiller_vant(trekk: str, datamaskin_trekk: str) -> bool:
    return (
        (trekk == "stein" and datamaskin_trekk == "saks")
        or (trekk == "saks" and datamaskin_trekk == "papir")
        or (trekk == "papir" and datamaskin_trekk == "stein")
    )


def print_mulige_trekk():
    print("Velg en av:")
    for trekk in mulige_trekk:
        print(trekk, end=",\n")


poeng = 0
poeng_datamaskin = 0

while poeng < 3 or poeng_datamaskin < 3:
    datamaskin_trekk: str = mulige_trekk[random.randint(0, 2)]

    while True:
        print_mulige_trekk()
        trekk: str = input("\n").lower()

        try:
            mulige_trekk.index(trekk)
        except:
            continue
        else:
            break

    print(f"\nDu valgte: {trekk}, jeg valgte: {datamaskin_trekk}\n")

    if trekk == datamaskin_trekk:
        print("Uavgjort, ingen fikk poeng.")
    elif spiller_vant(trekk, datamaskin_trekk):
        print("Du fikk et poeng!")
        poeng += 1
    else:
        print("Du tapte og jeg fikk et poeng.")
        poeng_datamaskin += 1

    print(f"Du har: {poeng} poeng.")
    print(f"Jeg har: {poeng_datamaskin} poeng.\n")

if poeng > poeng_datamaskin:
    print("Du vant!")
else:
    print("Du tapte og jeg vant.")
