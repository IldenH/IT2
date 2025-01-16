import csv
import matplotlib.pyplot as plt
from datetime import datetime


def parse_row(row):
    tid = int(datetime.strptime(row["tid"], "%Y-%m-%d %H:%M:%S").timestamp())

    try:
        temperatur = float(row["temperatur"])
    except ValueError:
        temperatur = "-"

    if temperatur != "-":
        data[tid] = temperatur


def parse_file(contents: csv.DictReader):
    for row in contents:
        parse_row(row)


def plot(data):
    tid = list(data.keys())
    temperatur = list(data.values())

    plt.plot(tid, temperatur)
    plt.xlabel("Tid")
    plt.ylabel("Temperatur")
    plt.title("Nordnes sjøbad temperatur i vannet over tid")
    plt.grid()
    plt.show()


if __name__ == "__main__":
    file = "./data.csv"
    data = {}

    with open(file, encoding="utf-8") as file:
        parse_file(csv.DictReader(file, delimiter=","))

    plot(data)
