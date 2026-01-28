#analyse what time of day has the most A&E attendances

#import libraries
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("attendance by time of day.csv")
print(df.head())