#plot a graph displaying total A&E attendance from April 2025-December 2025

#load necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

#load all CSV files from April to December
dfs = []
for file in Path(".").glob("*.csv"):
    print(f"Reading: {file.name}")
    dfs.append(pd.read_csv(file))

df = pd.concat(dfs, ignore_index = True)
