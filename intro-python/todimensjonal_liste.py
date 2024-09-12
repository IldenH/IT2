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

# 10 x 10 spillbrett med tilfeldige som er True
import random

rader = 10
kolonner = 10
antall_true = 20

spillbrett = [[False for _ in range(kolonner)] for _ in range(rader)]

for _ in range(antall_true):
    spillbrett[random.randint(0, rader - 1)][random.randint(0, kolonner - 1)] = True

[print(rad) for rad in spillbrett]
