#plot a graph showing mean temperature for April 2025-December2025 

import pandas as pd
import matplotlib.pyplot as plt

#load csv file and get rid of rows not needed
df = pd.read_csv("EnglandWeather.csv", skiprows = 5, sep = r"\s+")

#filter out data to only show April 2025-December 2025
data_2025 = df[df["year"]== 2025]
months = ["apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
monthly_temperature = data_2025[months].iloc[0]
