#do a chi-squared test to figure out if admission types vary by months

#import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from scipy.stats import chi2_contingency

#load the csv files
directory = Path(__file__).resolve().parent
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

#make a contingency table where rows = months, column = admission type
rows = []
months = []

for file in files:
    df = pd.read_csv(directory / file)
    #use the total row
    total = df[df["Org name"].astype(str).str.strip().str.upper() == "TOTAL"].iloc[0]
    #take the month from filename
    month = file.split("-")[0]
    months.append(month)

    #calculate the attendances by admission type
    rows.append([
        total["A&E attendances Type 1"],
        total["A&E attendances Type 2"],
        total["A&E attendances Other A&E Department"],
    ])

contingency = pd.DataFrame(rows, index = months, columns = ["Type 1 Attendances", "Type 2 Attendances", "Other A&E Attendances"])

#chi-squared test
chi2, p, dof, expected = chi2_contingency(contingency.values)

print("Chi-Squared test: Admission type vs Month")
print(f"chi^2 = {chi2:.2f}, dof = {dof}, p-value = {p:.6f}")
