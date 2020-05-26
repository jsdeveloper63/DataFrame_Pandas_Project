import numpy as np
import pandas as pd

df = pd.read_csv('../MelbourneData/melbdata.csv')

# Print df to make sure it works// It prints the data of csv as is
#print(df)

#Checking data type
#print(type(df))

#Checking df shape
#print(df.shape)

#View column names
#print(df.columns)

#Inspecting first 10 rows of data
#print(df.head(10))

#Inpsecting last 10 rows of data
#print(df.tail(5))

#view summmary of df
#print(df.info())

#To view a specific column from the data
#print(df.Regionname.head(2))
#print(df.Landsize)
#print(df.Price)
#print(df.index)
#print(df.values)
#print(df.ndim)
#print(df.axes)

#Extracting a particular column from a dataframe
#print(df['Landsize'])
#landsize = df['Landsize']
#Creating a variable
#print(landsize)
#print(landsize.head(5))
#When we extract a column from dataframe it becomes a datatype series
#print(type(landsize))
#When we extract values from landsize variable we get the type as numpy array
#new_landsize = landsize.values
#print(type(new_landsize))

#print(df['Rooms'])
rooms = df['Rooms']
#print(rooms)
#print(type(df['Rooms']))
#print(type(rooms))
new_rooms = rooms.values
#print(type(new_rooms))

#To view more than one column from dataframe
#print(df[['Landsize', 'Rooms', 'CouncilArea']].tail(5))
#print(df[['Landsize', 'Rooms', 'CouncilArea']].head(5))
#print(df[['Landsize', 'Rooms', 'CouncilArea']])

#Using the describe method
#print(df.describe())
#print()
