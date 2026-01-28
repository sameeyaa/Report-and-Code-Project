#calculate the percentage change between months for ED attendances

#import libraries
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

#load dataset
df = pd.read_csv("combined_ed_totals.csv",
                 parse_dates = ["Month"]).sort_values("Month")

