import pandas as pd
import numpy as np


def normalize_array(x):
    if x is not None:
        return x[2:-2]

    return x


def normalize_description(x):
    if x is not None:
        return x.replace("- ", "")
    return x


def normal_price(x):
    if x is not None:
        x = x.replace(" €", "")
        return x.replace(",", ".")
    return x


def analysis_products():
    df = pd.read_csv("all_products.csv")
    df.head()
    df.Price = df.Price.apply(normalize_array)
    df.Name = df.Name.apply(normalize_array)
    df.Previous_Price = df.Previous_Price.apply(normalize_array)
    df.Description = df.Description.apply(normalize_description)
    df.Description = df.Description.apply(lambda x: np.array(x))
    df.Price = df.Price.apply(normal_price)
    df.Price = df.Price.astype(float)

    indexMax = df.groupby(["Brand"])["Price"].transform(max) == df["Price"]
    indexMin = df.groupby(["Brand"])["Price"].transform(min) == df["Price"]
    meanGroup = df.groupby(["Brand"]).Price.mean()

    dfMin = df[indexMin]

    for index, row in df[indexMax].iterrows():
        print("\n\n\n\n")
        print(
            "{0}\nMax Price:{1} € [Product Name:{2},Product Url:{3}]\n".format(
                row.Brand, row.Price, row.Name, row.Url
            )
        )
        minAttributes = dfMin.loc[dfMin.Brand == row.Brand].reset_index()
        print(
            "\nMin Price:{0} € [Product Name:{1},Product Url:{2}]\n".format(
                minAttributes.Price[0], minAttributes.Name[0], minAttributes.Url[0]
            )
        )
        print("\nAverage Brand Price:{0}\n".format(meanGroup[row.Brand]))

    print("\n\nProducts that are on sale and their total count \n\n\n")
    df.Previous_Price = df.Previous_Price.apply(normal_price)
    df.Previous_Price = df.Previous_Price.apply(lambda x: np.nan if x == "" else x)
    df.Previous_Price = df.Previous_Price.astype(float)
    sale_count = df.loc[df.Previous_Price > 0].groupby("Brand")["Name"].count()
    print(sale_count)
