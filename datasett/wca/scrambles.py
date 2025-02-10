import matplotlib.pyplot as plt
import csv

events = {}

gruppe = "D"

with open("data/WCA_export_Scrambles.tsv") as file:
    contents = csv.DictReader(file, delimiter="\t")
    for row in contents:
        if row["groupId"] == gruppe:
            events[row["eventId"]] = events.get(row["eventId"], 0) + 1

events_sorted = sorted(events.items(), key=lambda event: -event[1])
plt.bar(*zip(*events_sorted))
plt.title(f"Antall blandinger i gruppe {gruppe}")
plt.xlabel("Event")
plt.ylabel("Antall")
plt.show()
