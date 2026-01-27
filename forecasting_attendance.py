#forecast 6 months of ED attendance
#this will help staff allocation and resource distribution
#uses historical data

#import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

#use historical data
df = pd.read_csv(Path(__file__).resolve().parent / "combined_ed_totals.csv",
                 parse_dates = ["Month"]).sort_values("Month")

#use a time index
t = np.arange(len(df))
y = df["Total_ED_Attendees"].values

#add linear regression
slope, intercept = np.polyfit(t, y, 1)

#forecast 6 months attendance
forecast_scope = 6 #for 6 months
future_t = np.arange(len(df), len(df) + forecast_scope)
forecast_data = slope * future_t + intercept
forecast_months = pd.date_range(
    df["Month"].iloc[-1] + pd.offsets.MonthBegin(1),
    periods = forecast_scope,
    freq = "MS"
)

#create a dataframe for easier plotting of graph
forecast_df = pd.DataFrame({
    "Month" : forecast_months,
    "Predicted_Attendance" : forecast_data
})

#plot the graph
plt.figure(figsize = (12, 8))
plt.plot(df["Month"], df["Total_ED_Attendees"], label = "Observed", color = "pink")
plt.plot(
    forecast_df["Month"],
    forecast_df["Predicted_Attendance"],
    linestyle = '--',
    label = "6 Month Forecast",
    color = "yellow"
)

#set labels
plt.title("Six Month Forecast of A&E Attendance - England 2025")
plt.xlabel("Month")
plt.ylabel("Emergency Department Attendances (millions)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()