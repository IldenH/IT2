verdensdeler = [
    "Afrika",
    "Antarktis",
    "Asia",
    "Europa",
    "Nord-Amerika",
    "Oseania",
    "Sør-Amerika",
]

print(verdensdeler[0], verdensdeler[len(verdensdeler) // 2], verdensdeler[-1])

heltall = [_ for _ in range(1, 51)]

print(heltall)

oddetall = [_ for _ in range(1, 200, 2)]

print(oddetall, len(oddetall))

kvadrattall = [x**2 for x in range(0, 20)]

print(kvadrattall)


kvadrattall = [x**3 for x in range(0, 15)]

print(kvadrattall)

print(min(kvadrattall), max(kvadrattall), sum(kvadrattall))
