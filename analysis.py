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

def filter_data(df):
    indicators = [
        "Life expectancy at birth, total (years)",
        "Current health expenditure (% of GDP)",
        "Mortality rate, infant (per 1,000 live births)"
    ]

    df = df[df["Indicator Name"].isin(indicators)]

    return df