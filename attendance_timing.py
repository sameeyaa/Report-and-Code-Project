#analyse what time of day has the most A&E attendances

#import libraries
import pandas as pd
import matplotlib.pyplot as plt

#load csv file but skip rows that are simply text
df = pd.read_csv("attendance by time of day.csv", skiprows = 9) 
print(df.head())

