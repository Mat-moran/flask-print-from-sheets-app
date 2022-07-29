from __future__ import print_function
import pandas as pd


def searchIngredients(id):
    df = pd.read_csv("database2.csv", sep=";")
    print(df)
    row = df.loc[df["CODIGO"] == int(id)]
    print(id)
    print("ROW: ", row.values[0])
    return row.values[0]


if __name__ == "__main__":
    print(searchIngredients("4"))
