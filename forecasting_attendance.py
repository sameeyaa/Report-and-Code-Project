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
