#unit test the output of the admission type bar graph
#import necessary libraries
import pandas as pd
import matplotlib
from pathlib import Path
#avoid GUI showing during testing
matplotlib.use("Agg")

#test reliability and accuracy of data
def test_data():
    #test if all data is extracted
    directory = Path("ED_attendance_analysis")

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

    rows = []
    for file in files:
        df = pd.read_csv(directory / file)

        #clarify if a TOTAL row is present
        assert (df["Org name"].astype(str).str.strip().str.upper() == "TOTAL").any(), \
            f"No total row found in {file}"
        
        #take the total row
        total = df[df["Org name"].astype(str).str.strip().str.upper() == "TOTAL"].iloc[0]

        #seperate attendance by admission type
        rows.append([
            total["A&E attendances Type 1"],
            total["A&E attendances Type 2"],
            total("A&E attendances Other A&E Department")
        ])

    #create a dataframe
    admissions_df = pd.DataFrame( rows, columns = ["Type 1", "Type 2", "Other A&E"])

    #test if there is 9 months of data and each month has 3 admission types
    assert admissions_df.shape == (9, 3)
    #test if there is missing values 
    assert admissions_df.notna().all().all()

    #run "pytest -q" in terminal to run unit test


        

