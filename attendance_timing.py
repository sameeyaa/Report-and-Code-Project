#analyse what time of day has the most A&E attendances

#import libraries
import pandas as pd
import matplotlib.pyplot as plt

#load csv file but skip rows that are simply text
df = pd.read_csv("attendance by time of day.csv", skiprows = 9) 
#print(df.head())

df = df[df["Measure Type"].str.contains("Number of A&E" , na= False)]

#select time columns
#classify ending with :00 as time
time_column = [c for c in df.columns if c.endswith(":00")]
df[time_column] = df[time_column].replace(",", "", regex = True).astype(int)

