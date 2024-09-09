rader = 8
kolonner = 8

# alternativ 1
tabell = []
for i in range(rader):
    rad = [0] * kolonner
    tabell.append(rad)

# alternativ 2
tabell = [[0 for _ in range(kolonner)] for _ in range(rader)]

# alternativ 3
tabell = [[0] * kolonner] * rader

# print(tabell)

sjakkbrett = [
    ["H" if i % 2 == 0 else "S" for i in range(j % 2, j % 2 + kolonner)]
    for j in range(rader)
]

[print(rad) for rad in sjakkbrett]
