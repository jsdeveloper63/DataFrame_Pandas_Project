import pandas as pd
import re

df = pd.read_csv('../MelbourneData/melbdata.csv')

#Create a condition to return data for rooms
#required_rooms = df['Rooms']>3
#print(required_rooms)
#print(df[df['Rooms']==1])

#Prints non-boolean values of variable required_rooms
#print(df[required_rooms])


#Prints data from Williamstown Suburb
#desirable_suburb = df['Suburb'] == 'Williamstown'
#print(df[desirable_suburb])
#print(df[df['Suburb']=='Williamstown'])

#Ccreate very powerful and sophisticated expressions by combining logical operations with the operators

#print(df[(df['Rooms']>2) & (df['Suburb']== 'Williamstown')])

#Prints data from CouncilArea Yarra
#desirable_council_area = df['CouncilArea'] == 'Yarra'
#print(df[desirable_council_area])
