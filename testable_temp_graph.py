#plots the mean temperature graph using met data - however is for unit testing

#import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

#load the dataset
#df = pd.read_csv(
 #   "EnglandWeather.csv",
 #   skiprows=5,
#    sep=r"\s+",
 #   engine="python"
#)
#print(df.head())

def load_data():
    csv_path = Path(__file__).resolve().parent / "EnglandWeather.csv"
    return pd.read_csv(csv_path, skiprows=5, sep=r"\s+", engine="python")

#filter out the data to only show 2025 data
def get_monthly_temps(df, year):
#data only for April 2025 to December 2025 needed
    months = ["apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
    data_year = df[df["year"] == year]

    if data_year.empty:
        raise ValueError(f"Year {year} not found")

    return data_year[months].iloc[0]

#plot the graph for the mean temperature
def temp_graph(months, temps, year = 2025):
    fig, ax = plt.subplots()
    ax.plot(months, temps, marker="o")
    ax.set_xlabel("Month")

#add labels
    ax.set_ylabel("Mean Temperature (degrees)")
    ax.set_title("Monthly Mean Temperature in England 2025")
    ax.grid(True)
    fig.tight_layout()
    return fig, ax

#show the graph
def main():
    df = load_data()
    months = ["apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
    temps = get_monthly_temps(df, 2025)

    temp_graph(months, temps, 2025)
    plt.show()

if __name__ == "__main__":
    main()