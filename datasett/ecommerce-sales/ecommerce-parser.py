import pandas

data = pandas.read_csv("data.csv")
categories = data["ProductCategory"].value_counts()

print(categories)
