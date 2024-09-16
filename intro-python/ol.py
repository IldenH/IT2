# sommer_ol = [
#     {"årstall": 2004, "vinnertider": {"100 m": 10.93, "200 m": 22.06, "400 m": 49.41}},
#     {"årstall": 2008, "vinnertider": {"100 m": 10.78, "200 m": 21.74, "400 m": 49.62}},
#     {"årstall": 2012, "vinnertider": {"100 m": 10.75, "200 m": 21.88, "400 m": 49.55}},
#     {"årstall": 2016, "vinnertider": {"100 m": 10.71, "200 m": 21.78, "400 m": 49.44}},
#     {"årstall": 2020, "vinnertider": {"100 m": 10.61, "200 m": 21.53, "400 m": 48.36}},
# ]
#
# for ol in sommer_ol:
#     år = ol["årstall"]
#     vinnertid_100m = ol["vinnertider"]["100 m"]
#     print(f"I {år} var vinnertiden på 100 m: {vinnertid_100m}.")

sommer_ol = {
    "100 m": {
        "2004": 10.93,
        "2008": 10.78,
        "2012": 10.75,
        "2016": 10.71,
        "2020": 10.61,
    },
    "200 m": {
        "2004": 22.06,
        "2008": 21.74,
        "2012": 21.88,
        "2016": 21.78,
        "2020": 21.53,
    },
    "400 m": {
        "2004": 49.41,
        "2008": 49.62,
        "2012": 49.55,
        "2016": 49.44,
        "2020": 48.36,
    },
}

for gren, tider in sommer_ol.items():
    for årstall, tid in tider.items():
        print(f"I {gren} var vinnertiden i {årstall} {tid} sekunder")
    print()
