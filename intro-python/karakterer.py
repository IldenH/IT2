for poengsum in range(0, 101):
    karakter = 0

    if poengsum < 81:
        karakter_hopp = 20
    else:
        karakter_hopp = 10
        # fjerner de første karakterene, siden hoppene er lavere
        karakter -= 4

    # legger til 1 dersom poengsummen ikke er ved grenseverdiene
    karakter += poengsum % karakter_hopp != 0

    karakter += poengsum // karakter_hopp

    print(f"Poengsum {poengsum} fører til karakter {karakter}")
