import pandas as pd
import requests

api = "https://raw.githubusercontent.com/robiningelbrecht/wca-rest-api/master/api"
url = f"{api}/persons.json"

params = {
    "page": 0,
    "size": 1000,
}

all_data = []
while True:
    response = requests.get(url, params)
    if response.status_code != 200:
        break

    data = response.json()
    if not data:
        break
    all_data.extend(data)

    params["page"] += 1


print(all_data)
# df = pd.read_json(all_data, typ="series")
# df = pd.DataFrame(df["items"])
#
# print(df)
