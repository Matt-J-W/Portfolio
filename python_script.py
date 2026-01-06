
### What factors drive customer purchasing behaviour, and how can a business increase conversions?
# rmarkdown::render_site()
# Importing the data

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data_import = pd.read_excel(r"C:\Users\Matthew.Webb12\Desktop\GitHub Repos\Portfolio\python data\carbon_emissions_fleet_dataset.xlsx")

print(data_import.head())
print(data_import.columns)

# Exploring the data for completeness
columns_to_check = ["Vehicle_Type", "Route_Type", "Delivery_Type"]

# Create empty dictionary for the tables to be stored in
count_tables = {} 

for col in columns_to_check:
  count_tables[col] = data_import[col].value_counts().to_frame(name="Count")

count_tables

# Handling columns
data_import["CO2_Emissions_kg"] = (data_import["CO2_Emissions_g"] / 1000).round(2)
data_import = data_import[data_import["Vehicle_Type"] != "S"]

# Creating an average fuel efficiency per litre for each vehicle type
# And also the count of delivery types for each vehicle type
data_import.groupby("Vehicle_Type")["Fuel_Efficiency_kmpl"].mean()
data_import.groupby("Delivery_Type")["Fuel_Efficiency_kmpl"].mean()
data_import.groupby("Delivery_Type")["Distance_km"].mean()
data_import.groupby("Vehicle_Type")["Delivery_Type"].value_counts()

# My plan is to calculate the rate of on time deliveries for each vehicle / delivery type
# Step 1: Create a resuable function for calculating the mean of a given metric

def matrix_function(value_column):
  return data_import.pivot_table(
    index="Vehicle_Type",
    columns="Delivery_Type",
    values=value_column,
    aggfunc="mean"
  ).round(2).T

on_time_matrix = matrix_function("On_Time_Delivery")
co2_matrix = matrix_function("CO2_Emissions_kg")
fuel_matrix = matrix_function("Fuel_Efficiency_kmpl")

# Step 2: Now combining them into one for ease of reading
combined_matrix = pd.concat(
    [on_time_matrix, co2_matrix, fuel_matrix],
    axis=0,
    keys=["On_Time", "CO2_kg", "Fuel_kmpl"]
)

combined_matrix.index = combined_matrix.index.map('_'.join)

# This plot is 
sns_load_util = sns.lmplot(
  data=data_import, 
  x="Load_Utilization_%", 
  y="Fuel_Efficiency_kmpl", 
  hue="Vehicle_Type", 
  height=6, 
  aspect=1.3, 
  scatter = False 
  )
plt.title("Effect of Load Utilization on Fuel Efficiency")
plt.xlabel("Load Utilization %")
plt.ylabel("Fuel Efficiency kmpl")
plt.show()
  
  


