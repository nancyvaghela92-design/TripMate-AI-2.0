import pandas as pd


def get_hotels(destination):

    df = pd.read_csv("data/hotels.csv")

    hotels = df[
        df["Destination"].str.lower() == destination.lower()
    ]

    return hotels