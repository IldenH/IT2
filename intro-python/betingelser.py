tall = []

for i in range(1, 4):
    tall.append(int(input(f"Oppgi tall {i}:")))

minst = tall[0]

for nummer in tall:
    if nummer < minst:
        minst = nummer

print(f"Det minste tallet er {minst}")
