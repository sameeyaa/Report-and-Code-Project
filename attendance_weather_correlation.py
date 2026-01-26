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
