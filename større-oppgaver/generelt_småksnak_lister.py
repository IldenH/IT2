liste = []
skal_deles_med = 7
for i in range(1, 101):
    liste.append(i)


def delelig_med(liste_med_tall, dele_tallet):
    delelig_liste = []
    for tall in liste_med_tall:
        if tall % dele_tallet == 0:
            delelig_liste.append(tall)

    return delelig_liste


print(f"Lista har {len(liste)} element.")
print(f"Startar søket etter tal delbare med {skal_deles_med}:")
for tall in delelig_med(liste, skal_deles_med):
    print(tall)
