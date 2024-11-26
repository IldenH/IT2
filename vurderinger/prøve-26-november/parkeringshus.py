import datetime


class Car:
    def __init__(self, registreringsnummer: str, model: str, color: str) -> None:
        print(f"\nOpprettet {color} {model} med reg.nr {registreringsnummer}.")
        self.registreringsnummer = registreringsnummer
        self.model = model
        self.color = color
        self.innkjørings_tid: datetime.datetime
        self.parkingprice = 1.5

    def list_info(self) -> str:
        return f"{self.registreringsnummer}: {self.model} ({self.color})"


class Lastebil(Car):
    def __init__(self, registreringsnummer: str, model: str, color: str) -> None:
        super().__init__(registreringsnummer, model, color)
        self.parkingprice = 3.0


class Parkinghouse:
    def __init__(self, space: int, cars: dict = {}) -> None:
        print(f"Opprettet parkeringshus med {space} plasser.")
        self.cars = cars
        self.space = space

    def add_car(self, car: Car, time: datetime.datetime) -> None:
        if self.space > len(self.cars):
            print(f"{car.registreringsnummer} kjørte inn {time.hour}:{time.minute}")
            car.innkjørings_tid = time
            self.cars[car.registreringsnummer] = car
        else:
            print(
                f"Kan ikke legge til {car.registreringsnummer} da det er for mange biler i parkeringshuset."
            )

    def remove_car(self, car_registreringsnummer: str, time) -> None:
        print(f"\n{car_registreringsnummer} kjørte ut {time.hour}:{time.minute}")

        car = self.cars[car_registreringsnummer]
        parkeringstid = self.calculate_minutes_parked(car, time)
        avgift = self.calculate_price(car, parkeringstid)
        print(f"Parkeringstid: {parkeringstid} min., avgift kr {avgift:.2f}")

        self.cars.pop(car_registreringsnummer)

    def calculate_minutes_parked(self, car: Car, time) -> int:
        # https://stackoverflow.com/a/1345852
        total_time_parked = time - car.innkjørings_tid
        SECONDS_IN_DAY = 24 * 60 * 60
        seconds_parked = (
            total_time_parked.days * SECONDS_IN_DAY + total_time_parked.seconds
        )
        minutes_parked = seconds_parked // 60
        return minutes_parked

    def calculate_price(self, car: Car, parkeringstid: int) -> float:
        return parkeringstid * car.parkingprice

    def list_cars(self, color: str = "") -> None:
        plass = f"ledige plasser: {self.space - len(self.cars)}"
        print("")
        if color != "":
            print(f"Biler ({color}) i parkeringshuset ({plass}):")
            for car in self.cars.values():
                if car.color == color:
                    print(f"- {car.list_info()}")
        else:
            print(f"Biler i parkeringshuset ({plass}):")
            for car in self.cars.values():
                print(f"- {car.list_info()}")


if __name__ == "__main__":
    parkinghouse = Parkinghouse(space=20)

    car = Car("AB12345", "Tesla", "rød")
    time = datetime.datetime(2023, 11, 29, 13, 37)
    parkinghouse.add_car(car, time)

    car = Car("EK13002", "eGolf", "hvit")
    time = datetime.datetime(2023, 11, 29, 13, 45)
    parkinghouse.add_car(car, time)

    time = datetime.datetime(2023, 11, 29, 14, 41)
    parkinghouse.remove_car("AB12345", time)

    car = Car("TV12345", "Ford", "hvit")
    time = datetime.datetime(2023, 11, 29, 14, 50)
    parkinghouse.add_car(car, time)

    car = Car("VD77077", "Ford", "blå")
    time = datetime.datetime(2023, 11, 29, 14, 55)
    parkinghouse.add_car(car, time)

    lastebil = Lastebil("RM42069", "Monster", "rosa")
    time = datetime.datetime(2023, 11, 29, 15, 12)
    parkinghouse.add_car(lastebil, time)

    time = datetime.datetime(2023, 11, 30, 15, 31)
    parkinghouse.remove_car("RM42069", time)

    parkinghouse.list_cars()
    parkinghouse.list_cars("hvit")


"""
Feil som kan oppstå siden systemet baserer seg på manuell registrering:

Bilene kan kjøre inn i parkeringshuset uten å fortelle parkeringshuset det.
Da er det både færre ledige plasser enn reklamert og bilen slipper å betale avgift.

Avgiftene til bilene kan bilen selv endre på
da det er ingen sikkerhet rundt endring av egne verdier.

Bilene kan også si at de kun parkerte i 0 minutt selv om de parkerte lengre. 
Eller til og med si at de har parkert et negativt antall minutter, via å skrive
utkjørselsdato som en dato før innkjørselsdato, og
da *få* penger for å parkere.
"""
