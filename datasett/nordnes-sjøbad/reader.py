import csv
import matplotlib.pyplot as plt
from datetime import datetime
import requests
import os


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


def safe_get(url: str) -> requests.Response:
    response = requests.get(url, stream=True)
    while response.status_code != 200:
        response = requests.get(url, stream=True)
    return response


def write_file(local_file: str, response: requests.Response):
    with open(local_file, "wb") as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)


def init_file(local_file: str):
    response = safe_get(
        "https://raw.githubusercontent.com/hausnes/nordnes-sjobad/refs/heads/main/temperatur.csv"
    )
    write_file(local_file, response)


if __name__ == "__main__":
    local_file = "data.csv"

    data = {}

    if not os.path.exists(local_file):
        init_file(local_file)

    with open(local_file, encoding="utf-8") as file:
        parse_file(csv.DictReader(file, delimiter=","))

    plot(data)
