from pathlib import Path
import pandas as pd

#test to see if all 9 months have data
def test_monthly_data():
    result = pd.read_csv("combined_ed_totals.csv")

    #expect 9 months
    assert len(result) == 9
    #check for missing values
    assert result["Month"].notna().all()
    assert result["Total_ED_Attendees"].notna().all()

    result.to_csv("monthly_ed_total.csv", index = False)
#test successfully runs
#run "pytest -q in terminal