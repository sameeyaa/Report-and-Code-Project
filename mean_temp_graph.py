#plot a graph showing mean temperature for April 2025-December2025 

import pandas as pd
import matplotlib.pyplot as plt

#load csv file and get rid of rows not needed
df = pd.read_csv("EnglandWeather.csv", skiprows = 5, sep = r"s+")
