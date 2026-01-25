#plot a graph displaying total A&E attendance from April 2025-December 2025

#load necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

#resolve directory so all CSV files are found
directory = Path(__file__).resolve().parent

#load all CSV files from April to December
files = [
    "April-2025-CSV-revised.csv",
    "May-2025-CSV-revised.csv",
    "June-2025-CSV-revised.csv",
    "July-2025-CSV-revised.csv",
    "August-2025-CSV-revised.csv",
    "September-2025-CSV-revised.csv",
    "October-2025-CSV-hg6dl.csv",
    "November-2025-CSV-G9pr3.csv",
    "December-2025-CSV-K7F4Sp.csv",
]

#create a dataframe with all CSV files
dfs = []
for filename in files:
    file_path = directory / filename
    print(f"Reading: {filename}")
    dfs.append(pd.read_csv(directory / filename))
df = pd.concat(dfs, ignore_index = True)

#filter out data to show April 2025- December 2025
#this is shown in the 'Period' column
#As the values of this column is weird (MSitAE-APRIL-2025), we filter the data to only find APRIL-2025
df["Period_clean"] = (
    df["Period"]
    .str.extract(r"([A-Z]+-\d{4})")[0]
    .str.title()
)