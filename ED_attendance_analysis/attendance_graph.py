# plot a graph displaying total A&E attendance from April 2025-December 2025

# load necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# resolve directory so all CSV files are found
directory = Path(__file__).resolve().parent

# load all CSV files from April to December
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

monthly_data = []

#create a dataframe with all CSV files
for filename in files:
    file_path = directory / filename
    print(f"Reading: {filename}")

    # read the monthly dataset
    df = pd.read_csv(file_path)

    #only use the Total row as it tallies attendance
    mask_total = df["Org name"].astype(str).str.strip().str.upper() == "TOTAL"
    if not mask_total.any() and "Period" in df.columns:
        mask_total = df["Period"].astype(str).str.strip().str.upper() == "TOTAL"

    if not mask_total.any():
        raise ValueError(f"No TOTAL row found in {filename}.")

    total_row = df.loc[mask_total].iloc[0]

    #filter out data to show April 2025- December 2025
    #this is shown in the 'Period' column
    #As the values of this column is weird (MSitAE-APRIL-2025), we filter the data to only find APRIL-2025
    filter_period = (
        df.loc[~mask_total, "Period"]
        .iloc[0]
        .split("-")[-2:]
    )

    #change the data format into datetime
    month = pd.to_datetime("-".join(filter_period).title(), format="%B-%Y")

    #Calculate the total attendees for each month as they are in secions
    #only looking at Type 1, Type 2 and Other Departments as booked appointments do not count as unexpected turnout
    #admissions do not also count due to this report analysing overall attendance even if its for 1 hour
    total_attendance = (
        total_row["A&E attendances Type 1"]
        + total_row["A&E attendances Type 2"]
        + total_row["A&E attendances Other A&E Department"]
    )
    
    monthly_data.append({
        "Month": month,
        "Total_ED_Attendees": total_attendance
    })

#make a dataframe for easier plotting
result = pd.DataFrame(monthly_data).sort_values("Month")

#plot graph
plt.figure(figsize=(12, 8))
plt.plot(result["Month"], result["Total_ED_Attendees"])
plt.title("Total Emergency Department Attendances 2025")
plt.xlabel("Month")
plt.ylabel("Number of attendees")
plt.xticks(rotation=45)
plt.ticklabel_format(style="plain", axis='y')
plt.tight_layout()
plt.grid(True)
plt.show()

#add results to a csv for a unit test
result.to_csv("combined_ed_totals.csv", index=False)

