#plot a graph showing mean temperature for April 2025-December2025 
#using the EnlandWeather.csv dataset

import pandas as pd
import matplotlib.pyplot as plt

#load csv file and get rid of rows not needed
df = pd.read_csv("EnglandWeather.csv", skiprows = 5, sep = r"\s+")

#filter out data to only show April 2025-December 2025
data_2025 = df[df["year"]== 2025]
months = [
    "apr", "may", "jun",
    "jul", "aug", "sep", "oct",
    "nov", "dec"
    ]
monthly_temperature = data_2025[months].iloc[0]

#plot the mean temperature graph
plt.figure(figsize = (12, 8))
plt.plot(months, monthly_temperature, marker = 'o')

#plot graph labels
plt.xlabel("Month")
plt.ylabel("Monthly Mean Temperature (degrees)")
plt.title("2025 Mean Temperature in England")
plt.tight_layout()
plt.grid(True)
plt.show()