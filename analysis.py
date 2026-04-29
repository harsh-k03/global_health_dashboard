import pandas as pd

def load_data():
    # Load CSV and skip metadata rows
    df = pd.read_csv("data/API_8_DS2_en_csv_v2_41823.csv", skiprows=4)

    return df

def reshape_data(df):
    df = df.melt(
        id_vars=["Country Name", "Country Code", "Indicator Name"],
        var_name="Year",
        value_name="Value"
    )

    # Keep only numeric years
    df = df[df["Year"].str.isnumeric()]
    df["Year"] = df["Year"].astype(int)

    return df