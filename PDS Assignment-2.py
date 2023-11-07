import pandas as pd
import datetime
import re

# Load the dataset
data = pd.read_csv('C:\\Users\\Asus\\Desktop\\PDS Assignment-2\\train.csv')

def extract_numeric_value(text):
    if pd.notna(text):
        matches = re.findall(r'(\d+\.\d+|\d+)', str(text))
        if matches:
            return float(matches[0])
    return None

# Check for missing values in each column
missing_values = data.isnull().sum()

# You can choose to drop columns with a significant number of missing values or impute them.
# For example, if "New_Price" has too many missing values, you can drop it.
data.drop(columns=["New_Price"], inplace=True)

# For other columns with missing values, impute them with the mean or median
data['Mileage'] = data['Mileage'].str.extract('(\d+\.\d+)').astype(float)  # Extract and convert to float
data['Engine'] = data['Engine'].str.extract('(\d+)').astype(float)  # Extract and convert to float
data['Power'] = data['Power'].str.extract('(\d+\.\d+)').astype(float)  # Extract and convert to float


# Impute missing values with the mean or median
data['Mileage'].fillna(data['Mileage'].median(), inplace=True)
data['Engine'].fillna(data['Engine'].median(), inplace=True)
data['Power'].fillna(data['Power'].median(), inplace=True)
data["Seats"].fillna(data["Seats"].median(), inplace=True)

#Task
#Remove the units from some of the attributes and only keep the numerical values (for example remove kmpl from “Mileage”, CC from “Engine”, bhp from “Power”, and lakh from “New_price”)

data["Mileage"] = data["Mileage"].apply(extract_numeric_value)
data["Engine"] = data["Engine"].apply(extract_numeric_value)
data["Power"] = data["Power"].apply(extract_numeric_value)


# Change the categorical variables (“Fuel_Type” and “Transmission”) into numerical one hot encoded value

data = pd.get_dummies(data, columns=["Fuel_Type", "Transmission"])


#Create one more feature and add this column to the dataset (you can use mutate function in R for this). For example, you can calculate the current age of the car by subtracting “Year” value from the current year. 

current_year = datetime.datetime.now().year
data['Current_Age'] = current_year - data['Year']

# Display the modified dataset
print(data.head())

# Save the modified dataset to a new CSV file if needed
data.to_csv("C:\\Users\\Asus\\Desktop\\PDS Assignment-2\\used_car_data_cleaned.csv", index=False)