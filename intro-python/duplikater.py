liste = [
    "duplikat",
    1,
    1,
    "streng",
    2,
    "streng",
    1,
    0,
    0.0,
    2,
    2,
    "duplikat",
    2,
    3,
    4,
    3,
    "duplikat",
    9,
    False,
    False,
    True,
]

for i in range(len(liste)):
    # sjekk om indeks som har samme verdi som i er før i
    if liste.index(liste[i]) < i:
        liste[i] = None  # markerer duplikatene

# fjerner None-ene
for _ in range(len(liste)):
    try:
        liste.remove(None)
    except ValueError:
        continue

print(liste)
