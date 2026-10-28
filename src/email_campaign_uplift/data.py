from pathlib import Path

import pandas as pd

url = "http://www.minethatdata.com/Kevin_Hillstrom_MineThatData_E-MailAnalytics_DataMiningChallenge_2008.03.20.csv"

def load_hillstrom_data(url: str) -> pd.DataFrame:
    data = pd.read_csv(url)

    return data

def explore_hillstrom_data(data: pd.DataFrame) -> None:
    """ explore the data """

    #get a preview of the data
    print(data.head(10))

    #check the size of the data
    print(f"data has {data.shape[0]} records and {data.shape[1]} features")

    #check if there are any missing values
    print(data.isna().sum())

    #check data types
    print(data.dtypes)

    #check value_counts and proportions, particularly in segment category
    for col in data.columns:
        print(data[col].value_counts())

#save the data to disk
def save_hillstrom_data(data: pd.DataFrame) -> None:
    data_dir = Path("data/")
    data.to_csv(data_dir / "hillstrom_data.csv", index=False)

if __name__ == "__main__":
    data = load_hillstrom_data(url)
    explore = explore_hillstrom_data(data)
    save = save_hillstrom_data(data)