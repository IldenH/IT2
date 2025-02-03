import pandas as pd

url = "https://raw.githubusercontent.com/robiningelbrecht/wca-rest-api/master/api/continents.json"

df = pd.read_json(url, typ="series")
df = pd.DataFrame(df["items"])

print(df)
