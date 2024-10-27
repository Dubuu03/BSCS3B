import pandas as pd

health_data=pd.read_csv("data.csv", header=0,sep=",")

# 1
# print(health_data)

#2
# print(health_data.head())

#3
health_data.dropna(axis=0,inplace=True)
print(health_data)

#4
health_data.dropna(axis=0,inplace=True)
print(health_data.info())

#5
health_data.dropna(axis=0,inplace=True)

health_data["Average_Pulse"] = health_data['Average_Pulse'].astype(float)
health_data["Max_Pulse"] = health_data["Max_Pulse"].astype(float)
print(health_data.info())

#6
health_data.dropna(axis=0,inplace=True)

health_data["Average_Pulse"] = health_data['Average_Pulse'].astype(float)
health_data["Max_Pulse"] = health_data["Max_Pulse"].astype(float)

print(health_data.describe())