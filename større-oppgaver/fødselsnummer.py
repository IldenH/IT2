import datetime
import time


class bcolors:
    RED = "\033[91m"


class Bruker:
    def __init__(self, fødselsnummer: str):
        if len(fødselsnummer) != 11:
            raise ValueError("Fødselsnummer er ikke 11 siffer")
        self.fødselsnummer = fødselsnummer

        fødselsår = int(fødselsnummer[4:6])
        årstall_nå = int(str(time.localtime().tm_year)[2:])
        if fødselsår > årstall_nå:  # antar at personen ikke er 100 år eller eldre
            fødselsår = f"19{fødselsår}"
        else:
            fødselsår = f"20{fødselsår}"

        self.fødselsdato = datetime.date(
            int(fødselsår),
            int(fødselsnummer[2:4]),
            int(fødselsnummer[:2]),
        )

        self.kjønn = ""
        if int(self.fødselsnummer[9]) % 2 == 0:
            self.kjønn = "kvinne"
        else:
            self.kjønn = "mann"

    def utskrift_fødselsdato(self, fin_utskrift=False) -> str:
        if fin_utskrift:
            return f"Fødselsdatoen er {self.fødselsdato:%e}. {self.fødselsdato:%B} {self.fødselsdato:%Y} ({self.kjønn})"
        else:
            return f"{self.fødselsdato:%d}.{self.fødselsdato:%m}.{self.fødselsdato:%Y}"


# while True:
#     try:
#         ole = Bruker(int(input("Fødselsnummer\n")))
#     except ValueError:
#         print("Ugyldig fødselsnummer")
#         continue
#     else:
#         break

ole = Bruker("02068210793")
print(ole.utskrift_fødselsdato())
print(f"{bcolors.RED}{ole.utskrift_fødselsdato(True)}")
