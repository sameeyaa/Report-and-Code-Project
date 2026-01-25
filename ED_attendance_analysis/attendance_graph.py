#plot a graph displaying total A&E attendance from April 2025-December 2025

#load necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

#resolve directory so all CSV files are found
directory = Path(__file__).resolve().parent

#load all CSV files from April to December
files = [
    "April-2025-CSV-revised.csv",
    "May-2025-CSV-revised.csv",
    "June-2025-CSV-revised.csv",
    "July-2025-CSV-revised.csv",
    "August-2025-CSV-revised.csv",
    "September-2025-CSV-revised.csv",
    "October-2025-CSV-hg6dl.csv",
    "November-2025-CSV-G9pr3.csv",
    "December-2025-CSV-K7F4Sp.csv",
]

#create a dataframe with all CSV files
dfs = []
for filename in files:
    file_path = directory / filename
    print(f"Reading: {filename}")
    dfs.append(pd.read_csv(directory / filename))
df = pd.concat(dfs, ignore_index = True)

#filter out data to show April 2025- December 2025
#this is shown in the 'Period' column
#As the values of this column is weird (MSitAE-APRIL-2025), we filter the data to only find APRIL-2025
df["Filter_Period"] = (
    df["Period"]
    .str.extract(r"([A-Z]+-\d{4})")[0]
    .str.title()
)

#change the data format into datetime
df["Month"] = pd.to_datetime(df["Filter_Period"], format = "%B-%Y")
#Calculate the total attendees for each month as they are in secions
#only looking at Type 1, Type 2 and Other Departments as booked appointments do not count as unexpected turnout
#admissions do not also count due to this report analysing overall attendance even if its for 1 hour
df["Total_ED_attendees"] = (
    df["A&E attendances Type 1"]
    + df["A&E attendances Type 2"]
    +df["A&E attendances Other A&E Department"]
)

#total the attendances for each month
monthly_total = (df.groupby("Month")["Total_ED_attendees"].sum().sort_index())

#plot graph
plt.figure (figsize = (12,8))
plt.plot(monthly_total.index, monthly_total.values)
plt.title("Total Emergency Department Attendances 2025")
plt.xlabel("Month")
plt.ylabel("Number of attendees")
plt.xticks(rotation = 45)
plt.tight_layout()
plt.grid(True)
plt.show()