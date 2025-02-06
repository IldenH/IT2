import csv
from datetime import datetime

weekday = ["Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag", "Lørdag", "Søndag"]
counts = {
    "Mandag": 0,
    "Tirsdag": 0,
    "Onsdag": 0,
    "Torsdag": 0,
    "Fredag": 0,
    "Lørdag": 0,
    "Søndag": 0,
}

with open("studietid.csv") as file:
    contents = csv.DictReader(file, delimiter=",")
    for row in contents:
        date = datetime.strptime(row["Dato"], "%d.%m.%Y")
        day = weekday[date.weekday()]
        counts[day] += 1

print(counts)
