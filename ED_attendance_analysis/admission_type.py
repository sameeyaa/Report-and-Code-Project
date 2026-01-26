#create a bar graph showing the type of ED admissions to decipher where most attendances come from
#Type 1 attendace: major ED that is open 24/7, serious life-threatening illnesses
#Type 2 attendance: single specialty services, less severe, not open 24/7
#other departments: minor injurys, walk ins, urgent treatment centre

#import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np

#state the directory
directory = Path(__file__).resolve().parent

#load all csv files
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

#simply filter to show the attendance totals for each month
rows = []
for file in files:
    df = pd.read_csv(directory / file)

    #only use the totals row
    total = df[df["Org name"].astype(str).str.strip().str.upper() == "TOTAL"].iloc[0]
    #extract each month
    extract_month = file.split("-")[0]

    #group the attendance by admission type
    rows.append({
        "Type 1": total["A&E attendances Type 1"],
        "Type 2": total["A&E attendances Type 2"],
        "Other A&E": total["A&E attendances Other A&E Department"]
    })

#create a dataframe for easier plotting
admissions_df = pd.DataFrame(rows)
admissions_df["Month"] = [f.split("-")[0] for f in files]
#average = admissions_df.mean() 
print(admissions_df.columns)
admissions_df.set_index("Month", inplace = True)

#plot the bar graph
#make a stacked bar chart to show each month
#instead make a clustered bar chart for easier analysis
#admissions_df.plot(
#    kind = "bar",
 #   stacked = True,
#    figsize = (12,8))

months = admissions_df.index
x = np.arange(len(months))
width = 0.25

plt.figure(figsize = (12,8))
plt.bar(x - width, admissions_df["Type 1"], width, label = "Type 1 attendance")
plt.bar(x, admissions_df["Type 2"], width, label = "Type 2 attendance")
plt.bar(x + width, admissions_df["Other A&E"], width, label = "Other A&E attendances")
plt.title("Monthly Attendance by Type of Admission in England")
plt.ylabel("Monthly Attendance")
plt.xticks(x, months, rotation = 45)
plt.legend()
plt.tight_layout
plt.show()