import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/WCA_export_Persons.tsv", delimiter="\t")

fig, ax = plt.subplots(2, 3)
fig.suptitle("Persons", fontsize=16)
fig.subplots_adjust(wspace=0.3, hspace=0.25)

gender_names = {"m": "Male", "f": "Female", "o": "Other"}

df["gender"].replace(gender_names).value_counts().plot(
    kind="pie", title="Gender", xlabel="Gender", ylabel="", ax=ax[0][0]
)

df["countryId"].value_counts().head(10).sort_values(ascending=True).plot(
    kind="barh", title="Countries", xlabel="Count", ylabel="Countries", ax=ax[0][1]
)

df["id"].value_counts().value_counts().rename(lambda x: x - 1).tail(2).plot(
    kind="bar",
    title="Name or country changes",
    xlabel="Times changed",
    ylabel="Total persons",
    ax=ax[0][2],
)

names = df["name"].str.split(" ")
first_names = names.str[:1]
first_names.value_counts().head(10).sort_values(ascending=True).plot(
    kind="barh", title="Firstnames", xlabel="Count", ylabel="Name", ax=ax[1][0]
)

last_names = names.str[1:]
last_names.value_counts().head(10).sort_values(ascending=True).plot(
    kind="barh", title="Lastnames", xlabel="Count", ylabel="Name", ax=ax[1][1]
)

unique_names = first_names.value_counts().value_counts()
unique_names.head(10).plot(
    kind="bar",
    title="Unique names",
    xlabel="Number of people with same name",
    ylabel="Total",
    ax=ax[1][2],
)

# TODO: name length


plt.show()
