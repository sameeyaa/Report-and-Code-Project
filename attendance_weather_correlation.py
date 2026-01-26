#testing the correlation and regression between weather and monthly attendance

#load libraries
import pandas as pd
from pathlib import Path
from scipy.stats import pearsonr
import numpy as np

#load the combined data of Emergency Department attendances
ed_df = pd.read_csv(Path(__file__).resolve().parent / "combined_ed_totals.csv", parse_dates = ["Month"]
)
#load temperature data
from testable_temp_graph import load_data, get_monthly_temps
weather_df = load_data()
temps = get_monthly_temps(weather_df, 2025)

#use only April 2025- December 2025 and match the datasets
months = pd.date_range("2025-04-01", "2025-12-01", freq = "MS")
temp_df = pd.DataFrame({
    "Month": months,
    "Mean_Temperature": temps.values
})

#merge the datasets together
merged_datasets = pd.merge(ed_df, temp_df, on = "Month")

#calculate the correlation
corr, p_value = pearsonr(
    merged_datasets["Mean_Temperature"],
    merged_datasets["Total_ED_Attendees"]
)

print(f"Correlation Coefficient : {corr:.3f}")
print(f"P-value: {p_value:.4f}")

#calculate linear regression
r_squared = corr ** 2
print(f"Regression value: {r_squared:.3f}")