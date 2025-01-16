import csv
import matplotlib.pyplot as plt
from datetime import datetime


def parse_row(row):
    tid = int(datetime.strptime(row["tid"], "%Y-%m-%d %H:%M:%S").timestamp())

    try:
        temperatur = float(row["temperatur"])
    except ValueError:
        temperatur = "-"

    try:
        lufttemperatur = float(row["lufttemperatur"])
    except ValueError:
        lufttemperatur = "-"

    if temperatur != "-" and lufttemperatur != "-":
        data[tid] = {"temperatur": temperatur, "lufttemperatur": lufttemperatur}


def parse_file(contents: csv.DictReader):
    for row in contents:
        parse_row(row)


def plot(data):
    tid = list(data.keys())
    temperatur = [tid["temperatur"] for tid in data.values()]
    lufttemperatur = [tid["lufttemperatur"] for tid in data.values()]

    plt.plot(tid, temperatur, label="vann temperatur")
    plt.plot(tid, lufttemperatur, label="luft temperatur")
    plt.xlabel("Tid")
    plt.ylabel("Temperatur")
    plt.title("Nordnes sjøbad temperatur over tid")
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == "__main__":
    file = "./data.csv"
    data = {}

    with open(file, encoding="utf-8") as file:
        parse_file(csv.DictReader(file, delimiter=","))

    plot(data)
