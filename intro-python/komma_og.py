class Elev:
    def __init__(self, navn: str, karakterer: list[int]):
        self.navn = navn
        self.karakterer = karakterer

    def karakterer_tekst(self) -> str:
        karaktertekst = ""
        for i in range(len(self.karakterer)):
            if i == len(self.karakterer) - 1:
                karaktertekst += " og "
            elif i > 0:
                karaktertekst += ", "
            karaktertekst += str(self.karakterer[i])
        return karaktertekst


bob = Elev("Bob", [1, 2, 3, 4, 5, 6])
print(bob.karakterer_tekst())
