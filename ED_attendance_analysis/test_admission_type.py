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
    