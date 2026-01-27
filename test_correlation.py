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

