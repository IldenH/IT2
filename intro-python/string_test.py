hallo = "Hallo!"

print(hallo[len(hallo) - 1])

HALLO = "HALLO!"

print(HALLO.title())

tekst = "Datamaskiner er ubrukelige. De kan bare gi oss svar."

tekst = tekst.replace("er ubrukelige. De ", "")
tekst = tekst.replace("bare ", "")

print(tekst)


class Bruker:
    def __init__(self, fornavn, etternavn, telefonnummer):
        self.fornavn = fornavn.capitalize()
        self.etternavn = etternavn.capitalize()
        self.telefonnummer = telefonnummer

    def print(self):
        print(f"{self.fornavn} {self.etternavn} har telefonnummer {self.telefonnummer}")


person = Bruker("navn", "navnesen", 123456789)
person.print()

meter = "100 m"
kilometer_i_sekundet = "300 000 km/s"
e = "2,718 281 828 459 045"

meter = int(meter.replace("m", ""))
kilometer_i_sekundet = int(kilometer_i_sekundet.replace("km/s", "").replace(" ", ""))
e = float(e.replace(",", ".").replace(" ", ""))

print(meter, kilometer_i_sekundet, e)
