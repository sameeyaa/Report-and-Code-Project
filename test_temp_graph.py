from pathlib import Path
import matplotlib
#headless backend for CircleCI
matplotlib.use("Agg")
import pandas as pd
import pytest

#call the graph file
from testable_temp_graph import load_data, get_monthly_temps, temp_graph

#test if loading data reads files and columns
def test_load_data():
    df = load_data()
    assert "year" in df.columns
    for col in ["apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]:
        assert col in df.columns

#test to see if 9 values are returned as April-December is 9 months
def test_2025_values():
    df = load_data()
    temps = get_monthly_temps(df, 2025)
    assert len(temps) == 9
    #check if temps contains a numeric value
    assert pd.api.types.is_numeric_dtype(temps)

#if there is data missing, the outcome will be an error
df = load_data()
with pytest.raises(ValueError):
    get_monthly_temps(df,2030)

#test if the plot of the graph is accurate
def test_plot():
    df = load_data()
    months = ["apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
    temps = get_monthly_temps(df, 2025)
    fig, ax = temp_graph(months, temps, 2025)

    #check if one line is plotted and labels are the same
    assert len(ax.lines) == 1
    assert ax.get_xlabel() == "Month"
    assert ax.get_ylabel() == "Mean Temperature (degrees)"
    assert ax.get_title() == "Monthly Mean Temperature in England 2025"

