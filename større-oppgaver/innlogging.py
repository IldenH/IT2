"""
Lag eit system som handterer innlogging.
Ha eit fokus på korleis du kan sjekke kriterier på best måte (kva er "best"?).
Brukaren må skrive inn brukarnavn og passord, og skal få tydelege feilmeldingar.
"""


class Bruker:
    def __init__(self, navn=input("Navn: "), passord=input("Passord: ")):
        self.navn = navn
        self.passord = passord


brukere = [Bruker("abc", "def"), Bruker()]
for bruker in brukere:
    print(f"Bruker {brukere.index(bruker)}:")
    print(f"Brukernavn: {bruker.navn}")
    print(f"Passord: {bruker.passord}")
    print()
