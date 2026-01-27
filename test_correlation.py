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
    Path("ED_attendance_analysis")/ "combined_ed_totals.csv",
    parse_dates=["Month"]
)
