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