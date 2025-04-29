import pytest
from datetime import datetime
import math


MONTHS = [
    "Januar",
    "Februar",
    "Mars",
    "April",
    "Mai",
    "Juni",
    "Juli",
    "August",
    "September",
    "November",
    "Desember",
]


class Person:
    def __init__(self, navn: str, kjønn: str, fødselsdato: datetime) -> None:
        if navn == "" or kjønn == "":
            raise ValueError("Navn og/eller kjønn kan ikke være tomt")
        self.navn = navn
        self.kjønn = kjønn

        self.fødselsdato = fødselsdato
        alder = self.alder()
        if alder < 0:
            raise ValueError("Alder kan ikke være lavere enn 0")

    def alder(self) -> int:
        today = datetime.today()
        alder = (today - self.fødselsdato).days
        return math.floor(alder / 365)


class Lærer(Person):
    def __init__(self, navn: str, kjønn: str, fødselsdato: datetime) -> None:
        super().__init__(navn, kjønn, fødselsdato)
        self.elever: dict[str, list[dict]] = {}

    def add_elev(self, fag: str, elev: "Elev") -> None:
        if fag not in self.elever:
            self.elever[fag] = []
        self.elever[fag].append({"elev": elev, "karakter": 5})

    def set_karakter_elev(self, fag: str, input_elev: "Elev", karakter: int):
        for elev in self.elever[fag]:
            if elev == input_elev:
                elev["karakter"] = karakter
                return

    def elever_str(self) -> str:
        resultat = "\n"
        for fag_navn, fag in self.elever.items():
            resultat += f"\t{fag_navn}\n"
            for elev in fag:
                resultat += f"\t\t{elev["elev"].navn}\t{elev["karakter"]}\n"
        return resultat


class Elev(Person):
    def __init__(
        self, navn: str, kjønn: str, fødselsdato: datetime, kontaktlærer: Lærer
    ) -> None:
        super().__init__(navn, kjønn, fødselsdato)
        self.kontaktlærer = kontaktlærer


class Skole:
    def __init__(self, navn: str) -> None:
        self.navn = navn

        self.elever: list[Elev] = []
        self.lærere: list[Lærer] = []

    def add_elev(self, elev: Elev) -> None:
        self.elever.append(elev)

    def add_lærer(self, lærer: Lærer) -> None:
        self.lærere.append(lærer)

    def print_elever(self) -> None:
        print(f"{self.navn} elever")
        for i, elev in enumerate(self.elever):
            print(
                f"""{i}
    Navn:\t\t{elev.navn}
    Alder:\t\t{elev.alder()}
    Kjønn:\t\t{elev.kjønn}
    Fødselsdato:\t{elev.fødselsdato.day}. {MONTHS[elev.fødselsdato.month - 1]} {elev.fødselsdato.year}
            """
            )

    def print_lærere(self) -> None:
        print(f"{self.navn} lærere")
        for i, lærer in enumerate(self.lærere):
            print(
                f"""{i}
    Navn:\t\t{lærer.navn}
    Alder:\t\t{lærer.alder()}
    Kjønn:\t\t{lærer.kjønn}
    Fødselsdato:\t{lærer.fødselsdato.day}. {MONTHS[lærer.fødselsdato.month - 1]} {lærer.fødselsdato.year}
    Elever:\t\t{lærer.elever_str()}
            """
            )


if __name__ == "__main__":
    skole = Skole("Amalie Skram")
    kontaktlærer = Lærer("Per Anderson", "Mann", datetime(1984, 6, 2))
    trond = Elev("Trond", "Mann", datetime(2013, 6, 28), kontaktlærer)
    tor = Elev("Tor", "Mann", datetime(2009, 6, 28), kontaktlærer)
    maria = Elev("Maria", "Kvinne", datetime(1, 6, 28), kontaktlærer)
    skole.add_elev(trond)
    skole.add_elev(maria)
    skole.print_elever()
    skole.add_lærer(kontaktlærer)
    kontaktlærer.add_elev("Matte", trond)
    kontaktlærer.add_elev("Matte", tor)
    kontaktlærer.add_elev("Engelsk", maria)
    skole.print_lærere()


def test_personer():
    lærer = Lærer("Lærer", "Mann", datetime(1990, 2, 12))
    with pytest.raises(ValueError):
        Elev("Person", "Kvinne", datetime(2026, 6, 28), lærer)
    elev = Elev("ÆØÅ_-,.$%&¤()", "Annet", datetime(2000, 1, 1), lærer)
    assert isinstance(elev, Elev)
