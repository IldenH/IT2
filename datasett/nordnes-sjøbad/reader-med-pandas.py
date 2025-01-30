import pandas
import matplotlib.pyplot as plt
import numpy

data = pandas.read_csv("data.csv")

data[data == "NaN"] = numpy.nan
data[data == "-"] = numpy.nan

data["temperatur"] = pandas.to_numeric(data["temperatur"])
data["lufttemperatur"] = pandas.to_numeric(data["lufttemperatur"])
data["tid"] = pandas.to_datetime(data["tid"])

data.plot(x="tid", y=["temperatur", "lufttemperatur"])
plt.xlabel("Tid")
plt.ylabel("Temperatur")
plt.title("Nordnes sjøbad temperatur over tid")
plt.legend()
plt.grid()
plt.show()
