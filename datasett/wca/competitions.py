import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/WCA_export_Competitions.tsv", delimiter="\t")

print(df.columns)

fig, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4)

ax1.set_title("WCA competitions by year")
ax1.set_xlabel("Year")
ax1.set_ylabel("Competitions")
df["year"].value_counts().sort_index().plot(kind="bar", ax=ax1)

ax2.set_title("Cancelled competitions by year")
ax2.set_xlabel("Year")
ax2.set_ylabel("Competitions")
df.loc[df["cancelled"] == True, "year"].value_counts().sort_index().plot(
    kind="bar", ax=ax2
)

ax3.set_title("Competitions by event")
ax3.set_xlabel("Event")
ax3.set_ylabel("Competitions")
df["eventSpecs"].str.split().explode().value_counts().sort_index().plot(
    kind="bar", ax=ax3
)

ax4.set_title("Competitions by country")
ax4.set_xlabel("Country")
ax4.set_ylabel("Competitions")
df["countryId"].value_counts().head(10).sort_index().plot(kind="bar", ax=ax4)


plt.show()
