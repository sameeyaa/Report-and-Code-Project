#plots the mean temperature graph using met data - however is for unit testing

#import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

#load the dataset
df = pd.read_csv(
    "EnglandWeather.csv",
    skiprows=5,
    sep=r"\s+",
    engine="python"
)