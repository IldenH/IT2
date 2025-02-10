import matplotlib.pyplot as plt
import csv
import re

mail = {}

pattern = r"@([^}]+)}"

with open("data/WCA_export_Competitions.tsv") as file:
    contents = csv.DictReader(file, delimiter="\t")
    for row in contents:
        matches = re.findall(pattern, row["organiser"])
        for match in matches:
            mail[match] = mail.get(match, 0) + 1

mail_sorted = sorted(mail.items(), key=lambda m: -m[1])[:10]
plt.bar(*zip(*mail_sorted))
plt.show()
