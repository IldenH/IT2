import pandas as pd
import matplotlib.pyplot as plt
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(), logging.FileHandler("persons.log", mode="w")],
)

df = pd.read_csv("data/WCA_export_Persons.tsv", delimiter="\t")
logger.info("Read data")

fig, ax = plt.subplots(2, 4)
fig.suptitle("Persons", fontsize=16)
fig.subplots_adjust(wspace=0.3, hspace=0.25)
logger.info("Created figure")

gender_names = {"m": "Male", "f": "Female", "o": "Other"}

df["gender"].replace(gender_names).value_counts().plot(
    kind="pie", title="Gender", xlabel="Gender", ylabel="", ax=ax[0][0]
)
logger.info("Plot gender")

df["countryId"].value_counts().head(10).sort_values(ascending=True).plot(
    kind="barh", title="Countries", xlabel="Count", ylabel="Countries", ax=ax[0][1]
)
logger.info("Plot country")

df["id"].value_counts().value_counts().rename(lambda x: x - 1).tail(2).plot(
    kind="bar",
    title="Name or country changes",
    xlabel="Times changed",
    ylabel="Total persons",
    ax=ax[0][2],
)
logger.info("Plot changes")

names = df["name"].str.replace(r"\(.*?\)", "", regex=True).str.split(" ")
first_names = names.str[0]
first_names.value_counts().head(10).sort_values(ascending=True).plot(
    kind="barh", title="Firstnames", xlabel="Count", ylabel="Name", ax=ax[1][0]
)
logger.info("Plot firstnames")

last_names = names.str[-1]
last_names.value_counts().head(10).sort_values(ascending=True).plot(
    kind="barh", title="Lastnames", xlabel="Count", ylabel="Name", ax=ax[1][1]
)
logger.info("Plot lastnames")

unique_names = first_names.value_counts().value_counts()
unique_names.head(10).plot(
    kind="bar",
    title="Unique names",
    xlabel="Number of people with same name",
    ylabel="Total",
    ax=ax[1][2],
)
logger.info("Plot unique names")

# names[names.apply(len) == 9] can be used to see who has long names
name_lengths = names.apply(len)
name_lengths.value_counts().plot(
    kind="bar",
    title="Name length",
    xlabel="Length",
    ylabel="Total",
    ax=ax[1][3],
)
logger.info("Plot name lengths")

plt.show()
