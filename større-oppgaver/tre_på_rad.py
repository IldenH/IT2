rader = 3
koloner = 3

brett = [[" " for _ in range(koloner)] for _ in range(rader)]


def kolonne_og_rad_input(spiller):
    print(f"Spiller {spiller} sin tur:")
    while True:
        try:
            kolonne = int(input("Hvilken kolonne vil du plassere i?\n"))
            if not (kolonne >= 0 and kolonne <= 2):
                print("Må være fra og med 0 til og med 2")
                continue

            rad = int(input("Hvilken rad vil du plassere i?\n"))
            if not (rad >= 0 and rad <= 2):
                print("Må være fra og med 0 til og med 2")
                continue

        except ValueError:
            print("Skriv et tall")
            continue
        else:
            break

    if brett[rad][kolonne] == " ":
        brett[rad][kolonne] = spiller


def print_brett():
    [print(rad) for rad in brett]
    print()


while True:
    print_brett()
    kolonne_og_rad_input("x")
    print_brett()
    kolonne_og_rad_input("o")
