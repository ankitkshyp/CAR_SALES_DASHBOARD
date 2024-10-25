import pandas as pd

import matplotlib.pyplot as plt

import subprocess

powerbipath = "C:\\Program Files (x86)\\Microsoft Power BI Desktop\\bin\\PBIDesktop.exe"
filepath = "powerbiproject.pbix"
subprocess.Popen([powerbipath, filepath])

print("----------------------------------first---------------------------------------------------------")
# Read the CSV file
data = pd.read_csv("Norway_car_sales_by_make.csv")

#print csv file
print(data)
print("-------------------------------------------------------------------------------------------")

print("-----------------------------------second--------------------------------------------------------")

# Read the CSV file
df = pd.read_csv("cars_dataset.csv")
#print csv file
print(df)
print("-------------------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------------------")

# Load the dataset from the CSV file
file_path = "powerbiproject.pbix.pbix"  # Replace this with the correct file path
cars_dataset = pd.read_csv("cars_dataset.csv")
# This will define 'cars_dataset'

# Print all the column names to check for the correct one
print("Column Names in the Dataset:")
print(cars_dataset.columns)

# Assuming the model name column is 'Model' or similar, adjust as necessary
possible_model_columns = ['Model', 'model', 'Car Model', 'car_model']  # Add variations if needed

# Find the correct column for model names
model_column = None
for col in possible_model_columns:
    if col in cars_dataset.columns:
        model_column = col
        break

# Print the model names if the column is found
if model_column:
    model_names = cars_dataset[model_column]
    print(f"Model Names from column '{model_column}':")
    print(model_names)
else:
    print("Model column not found in the dataset.")
print("------------------------------------------------------------------------------------------")

# Print all the column names to check for the correct one
print("Column Names in the Dataset:")
print(cars_dataset.columns)

# Assuming the model name column is 'Model' or similar, adjust as necessary
possible_model_columns = ['Model', 'model', 'Car Model', 'car_model']  # Add variations if needed

# Find the correct column for model names
model_column = None
for col in possible_model_columns:
    if col in cars_dataset.columns:
        model_column = col
        break

# Print the model names if the column is found
if model_column:
    model_names = cars_dataset[model_column]
    print(f"Model Names from column '{model_column}':")
    print(model_names)
else:
    print("Model column not found in the dataset.")

print("-------------------------------------------------------------------------------------------")

# Group by 'Year' and get the maximum 'Quantity' for each year
max_Quantity_per_year = data.groupby('Year')['Quantity'].max().reset_index()

# Plot the graph
plt.figure(figsize=(10, 6))
plt.plot(max_Quantity_per_year['Year'], max_Quantity_per_year['Quantity'], marker='o', linestyle='-', color='b')

# Adding labels and title
plt.title('Highest Selling Quantity by Year')
plt.xlabel('Year')
plt.ylabel('Quantity')

# Display the plot
plt.grid(True)

plt.show()
