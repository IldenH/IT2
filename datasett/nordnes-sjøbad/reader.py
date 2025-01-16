import csv
import matplotlib.pyplot as plt
from datetime import datetime

file = "./data.csv"

data = {}

with open(file, encoding="utf-8") as fil:
    filinnhold = csv.DictReader(fil, delimiter=",")

    for rad in filinnhold:
        tid = int(datetime.strptime(rad["tid"], "%Y-%m-%d %H:%M:%S").timestamp())
        try:
            temperatur = float(rad["temperatur"])
        except ValueError:
            temperatur = "-"

        if temperatur != "-":
            data[tid] = temperatur


tid = list(data.keys())
temperatur = list(data.values())

plt.plot(tid, temperatur)
plt.xlabel("Tid")
plt.ylabel("Temperatur")
plt.title("Nordnes sjøbad temperatur i vannet over tid")
plt.grid()
plt.show()
