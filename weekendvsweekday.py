#bar chart to see whether weekdays or weekends have higher attendances

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

#seperate days into weekend and weekday
weekday = df[df["Reporting Period"].isin(
    ["Monday","Tuesday", "Wednesday", "Thursday", "Friday"]
    )][time_column].sum()

weekend = df[df["Reporting Period"].isin(
    ["Saturday", "Sunday"]
)][time_column].sum()