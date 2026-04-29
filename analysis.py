import pandas as pd

def load_and_prepare_data():
    # Load data (skip metadata rows)
    df = pd.read_csv("data/API_8_DS2_en_csv_v2_41823.csv", skiprows=4)

    # Reshape (wide → long)
    df = df.melt(
        id_vars=["Country Name", "Country Code", "Indicator Name"],
        var_name="Year",
        value_name="Value"
    )

    # Clean Year column
    df = df[df["Year"].str.isnumeric()]
    df["Year"] = df["Year"].astype(int)

    # Filter important indicators
    indicators = [
        "Life expectancy at birth, total (years)",
        "Current health expenditure (% of GDP)",
        "Mortality rate, infant (per 1,000 live births)"
    ]
    df = df[df["Indicator Name"].isin(indicators)]

    # Pivot to final format
    df = df.pivot_table(
        index=["Country Name", "Country Code", "Year"],
        columns="Indicator Name",
        values="Value"
    ).reset_index()

    # Rename columns
    df = df.rename(columns={
        "Country Name": "Country",
        "Country Code": "Code",
        "Life expectancy at birth, total (years)": "Life Expectancy",
        "Current health expenditure (% of GDP)": "Health Expenditure",
        "Mortality rate, infant (per 1,000 live births)": "Infant Mortality"
    })

    # Drop missing values
    df = df.dropna()

    return df