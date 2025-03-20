import pandas as pd
import matplotlib.pyplot as plt
import sys

"""
>>> df.columns
Index(['Timestamp', 'Source IP Address', 'Destination IP Address',
       'Source Port', 'Destination Port', 'Protocol', 'Packet Length',
       'Packet Type', 'Traffic Type', 'Payload Data', 'Malware Indicators',
       'Anomaly Scores', 'Alerts/Warnings', 'Attack Type', 'Attack Signature',
       'Action Taken', 'Severity Level', 'User Information',
       'Device Information', 'Network Segment', 'Geo-location Data',
       'Proxy Information', 'Firewall Logs', 'IDS/IPS Alerts', 'Log Source'],
      dtype='object')
"""

df = pd.read_csv("sikkerheit_utf8.csv", delimiter=";")


def main():
    print("Mest brukte protokollar og hvor ofte de er brukt:")
    print(df["Protocol"].value_counts().to_frame())
    print()

    fig, ax = plt.subplots(1, 2)
    fig.suptitle("Sikkerhet", fontsize=16)

    attackTypes = df["Attack Type"].value_counts().count()
    print(f"Antall ulike typer Attack Type: {attackTypes}")

    rows = df.shape[0]
    ddos = df[df["Attack Type"] == "DDoS"]["Attack Type"].count()
    prosentandel = ddos / rows * 100
    print(f"Prosentandel DDoS: {prosentandel}%")

    df["Attack Type"].value_counts().plot(
        kind="pie",
        title="Prosentandel fordeling av angripsmetoder",
        ylabel="",
        ax=ax[0],
    )

    # https://stackoverflow.com/a/53415824
    # .values.sum() visste jeg ikke om fra før
    windows = df["Device Information"].str.contains("Windows").values.sum()
    macintosh = df["Device Information"].str.contains("Macintosh").values.sum()

    ax[1].pie(
        [windows, macintosh],
        labels=["Windows", "Macintosh"],
    )
    ax[1].set(title="Prosentandel operativsystem som blir angripe oftast")

    plt.show()


if __name__ == "__main__" and not sys.flags.interactive:
    main()
