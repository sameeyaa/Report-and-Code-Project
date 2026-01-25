#plot a graph displaying total A&E attendance from April 2025-December 2025

#load necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

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
    print(f"Reading: {filename}")
    dfs.append(pd.read_csv(filename))
df = pd.concat(dfs, ignore_index = True)