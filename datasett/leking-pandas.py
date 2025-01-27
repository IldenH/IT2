import pandas
import numpy

data = pandas.DataFrame(
    {
        "A": 1.0,
        "B": pandas.Timestamp("20130102"),
        "C": pandas.Series(1, index=list(range(4)), dtype="float32"),
        "D": numpy.array([3] * 4, dtype="int32"),
        "E": pandas.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)

print(data)
print(data.dtypes)
