#calculate the percentage change between months for ED attendances

#import libraries
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

#load dataset
df = pd.read_csv("combined_ed_totals.csv",
                 parse_dates = ["Month"]).sort_values("Month")

#percentage change
df["percentage_change"] = df["Total_ED_Attendees"].pct_change() * 100

#plot graph
plt.figure(figsize = (12,8))
plt.bar(df["Month"].dt.strftime("%b"), df["percentage_change"])
plt.title("Monthly A&E attendance percentage change")
plt.xlabel("Months")
plt.ylabel("Percentage Change (%)")
plt.tight_layout()
plt.show()
