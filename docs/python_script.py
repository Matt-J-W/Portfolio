
### What factors drive customer purchasing behaviour, and how can a business increase conversions?

# Importing the data

import pandas as pd

data_import = pd.read_excel(r"C:\Users\Matthew.Webb12\Desktop\GitHub Repos\Portfolio\python data\carbon_emissions_fleet_dataset.xlsx")

print(data_import.head())

# Exploring the data 

columns_to_check = ["Vehicle_Type", "Route_Type", "Delivery_Type"]

for col in columns_to_check:
  print(f"Count for {col}")
  print(data_import[col].value_counts())

# Handling columns to make it easier to read
data_import["CO2_Emissions_kg"] = data_import["CO2_Emissions_g"] / 1000
data_import["On_Time_Delivery"] = data_import["On_Time_Delivery"].replace({1: "Yes", 0: "No"})

# Removing the one row where Vehicle_Type == S as this isn't meaningful data
data_import[data_import["Vehicle_Type"] != "S"]

# Creating an average fuel efficiency per litre for each vehicle type

data_import.groupby("Vehicle_Type")["Fuel_Efficiency_kmpl"].mean()

    
  
  
  


