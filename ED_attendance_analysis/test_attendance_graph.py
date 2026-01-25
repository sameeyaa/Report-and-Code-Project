from pathlib import Path
import pandas as pd

#read one csv and return the month and number of attendees
def extract_values(filepath: Path) -> dict:
    df = pd.read_csv("April-2025-CSV-revised.csv")
