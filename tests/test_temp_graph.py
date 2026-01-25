from pathlib import Path
import matplotlib.pyplot as plt
#headless backend for CircleCI
matplotlib.use("Agg")
import pandas as pd
import pytest

#call the graph file
from testable_temp_graph import load_data, get_monthly_temps, temp_graph
