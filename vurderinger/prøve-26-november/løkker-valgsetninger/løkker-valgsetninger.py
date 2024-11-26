def BMI(vekt: float, høyde: float):
    """Regner ut BMI utifra vekt (kilogram) og høyde (meter)"""
    return vekt / (høyde * høyde)


def BMI_centimeter(vekt: float, høyde: float):
    """Regner ut BMI utifra vekt (kilogram) og høyde (centimeter)"""
    return BMI(vekt, høyde / 100)


def BMI_vurdering(bmi: float) -> str:
    """Vurderer om BMI under-, normal- eller overvektig"""
    if bmi <= 18.4:
        return "undervektig"
    if bmi > 18.4 and bmi < 25:
        return "normalvektig"
    if bmi >= 25:
        return "overvektig"
    return "klarte ikke vurdere vekt"


class Kalkulator:
    """BMI-kalkulator"""

    def __init__(self) -> None:
        self.running = True
        self.current_høyde = 0
        self.current_vekt = 0
        self.høyde_input = ""

    def run(self) -> None:
        while self.running:
            self.ta_input()

            # Sjekke om noe har blitt skrevet inn enda, er tom dersom bruker avslutter tidlig
            if self.høyde_input != "":
                bmi = BMI_centimeter(self.current_vekt, self.current_høyde)
                print(f"BMI: {bmi:.1f} ({BMI_vurdering(bmi)})")

    def ta_input(self) -> None:
        while True:
            try:
                self.høyde_input = input("Skriv inn høyden i cm: ")
                if self.høyde_input == "":
                    self.running = False
                    break
                self.current_høyde = float(self.høyde_input)
                self.current_vekt = float(input("Skriv inn vekten i kg: "))
            except ValueError:
                print("Du må skrive et heltall!")
                continue
            except KeyboardInterrupt:
                self.running = False
                break
            else:
                break


if __name__ == "__main__":
    print("BMI-kalkulator")
    kalkulator = Kalkulator()
    kalkulator.run()
    print("\nTakk for nå.")
