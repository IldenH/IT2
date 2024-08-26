"""
Lag teksten maaneder = "JanFebMarAprMaiJunJulAugSepOktNovDes".
Lag et program som lar brukeren skrive inn et tall som representerer et månedsnummer.
Programmet skal deretter hente ut og skrive ut riktig månedsforkortelse fra teksten maaneder.
"""

months = "JanFebMarAprMaiJunJulAugSepOktNovDes"

# Komma til punktum og fjerner mellomrom
month_number = input("Månede nummer: ").replace(",", ".").replace(" ", "")
# Runder ned til nærmeste heltall
month_number = int(float(month_number))

while not (month_number <= 12 and month_number > 0):
    print("Tallet må være fra og med 1 til og med 12")
    month_number = int(input("Månede nummer: "))

print(months[3 * (month_number - 1) : 3 * month_number])
