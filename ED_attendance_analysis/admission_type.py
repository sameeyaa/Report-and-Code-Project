#create a bar graph showing the type of ED admissions to decipher where most attendances come from
#Type 1 attendace: major ED that is open 24/7, serious life-threatening illnesses
#Type 2 attendance: single specialty services, less severe, not open 24/7
#other departments: minor injurys, walk ins, urgent treatment centre

#import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

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

    #group the attendance by admission type
    rows.append({
        "Type 1": total["A&E attendances Type 1"],
        "Type 2": total["A&E attendances Type 2"],
        "Other A&E": total["A&E attendances Other A&E Department"]
    })

#create a dataframe for easier plotting and calculate an average of admissions
admissions_df = pd.DataFrame(rows)
average = admissions_df.mean()