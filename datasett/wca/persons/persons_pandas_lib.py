import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

df = pd.read_csv("../data/WCA_export_Persons.tsv", delimiter="\t")

image_path = "tmp.png"


def gender_names() -> str:
    gender_names = {"m": "Male", "f": "Female", "o": "Other"}

    df["gender"].replace(gender_names).value_counts().plot(
        kind="pie", title="Gender", xlabel="Gender", ylabel=""
    )
    plt.savefig(image_path)
    plt.clf()
    return image_path


def countries() -> str:
    df["countryId"].value_counts().head(10).sort_values(ascending=True).plot(
        kind="barh", title="Countries", xlabel="Count", ylabel="Countries"
    )
    plt.savefig(image_path)
    plt.clf()
    return image_path


def changes() -> str:
    df["id"].value_counts().value_counts().rename(lambda x: x - 1).tail(2).plot(
        kind="bar",
        title="Name or country changes",
        xlabel="Times changed",
        ylabel="Total persons",
    )
    plt.savefig(image_path)
    plt.clf()
    return image_path


names = df["name"].str.replace(r"\(.*?\)", "", regex=True).str.split(" ")


def first_names() -> str:
    first_names = names.str[0]
    first_names.value_counts().head(10).sort_values(ascending=True).plot(
        kind="barh", title="Firstnames", xlabel="Count", ylabel="Name"
    )
    plt.savefig(image_path)
    plt.clf()
    return image_path


def last_names() -> str:
    last_names = names.str[-1]
    last_names.value_counts().head(10).sort_values(ascending=True).plot(
        kind="barh", title="Lastnames", xlabel="Count", ylabel="Name"
    )
    plt.savefig(image_path)
    plt.clf()
    return image_path


def unigue_names() -> str:
    first_names = names.str[0]
    unique_names = first_names.value_counts().value_counts()
    unique_names.head(10).plot(
        kind="bar",
        title="Unique names",
        xlabel="Number of people with same name",
        ylabel="Total",
    )
    plt.savefig(image_path)
    plt.clf()
    return image_path


# names[names.apply(len) == 9] can be used to see who has long names
def name_lengths() -> str:
    name_lengths = names.apply(len)
    name_lengths.value_counts().plot(
        kind="bar", title="Name length", xlabel="Length", ylabel="Total"
    )
    plt.savefig(image_path)
    plt.clf()
    return image_path
