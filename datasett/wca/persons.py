import pandas as pd

api = "https://raw.githubusercontent.com/robiningelbrecht/wca-rest-api/master/api/"
url = api + "persons.json"

df = pd.read_json(url, typ="series")
df = pd.DataFrame(df["items"])

print(df)
