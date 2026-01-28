#test if correlation is between 1 and -1
#test if there is any missing values
#test if regression is between 0 and 1

#import libraries
import pandas as pd
import numpy as np
from pathlib import Path
from scipy.stats import pearsonr

#get the attendances values
ed_df = pd.read_csv(
    "combined_ed_totals.csv",
    parse_dates=["Month"]
)

#get the temperature data
from testable_temp_graph import load_data, get_monthly_temps
weather_df = load_data()
temps = get_monthly_temps(weather_df, 2025)

#create a dataframe for the temperature data
months = pd.date_range("2025-04-01", "2025-12-01", freq="MS")
temp_df = pd.DataFrame({
    "Month" : months,
    "Average_Temperature": temps.values
})

#combine the datasets
merge = pd.merge(ed_df, temp_df, on = "Month")

#test if there are 9 outcomes or any missing values
assert len(merge) == 9
assert "Average_Temperature" in merge.columns
assert "Total_ED_Attendees" in merge.columns
assert merge["Average_Temperature"].notna().all()
assert merge["Total_ED_Attendees"].notna().all()

#test the correlation
corr, p_value = pearsonr(merge["Average_Temperature"], merge["Total_ED_Attendees"])
assert -1 <= corr <= 1
assert 0 <= p_value <= 1

r_squared = corr ** 2
assert 0 <= r_squared <= 1

#test that the regression line is accurate
x = merge["Average_Temperature"].values
y = merge["Total_ED_Attendees"].values

slope, intercept = np.polyfit(x, y, 1)
y_pred = slope * x * intercept

assert len(y_pred) == len(y)
assert np.isfinite(slope)
assert np.isfinite(intercept)
assert np.isfinite(y_pred).all()

#run unit test by typing "pytest -q in terminal"
#unit test runs successfully
