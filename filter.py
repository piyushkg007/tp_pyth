import pandas as pd

# Load data from the CSV file
df = pd.read_csv('com_data.csv')

# Convert the "Time" column to a datetime object
df["Time"] = pd.to_datetime(df["Time"])

# Find the minimum and maximum times in the dataset
min_time = df["Time"].min()
max_time = df["Time"].max()

# Initialize an empty DataFrame to store the extracted data
extracted_data = pd.DataFrame(columns=["Time", "Reading"])

# Loop through 30-second intervals from min_time to max_time
current_time = min_time
while current_time <= max_time:
    # Find the data point closest to the current time
    closest_data_point = df.iloc[(df["Time"] - current_time).abs().argsort()[0]]
    
    # Append the closest data point to the extracted_data DataFrame
    extracted_data = pd.concat([extracted_data, closest_data_point.to_frame().T], ignore_index=True)
    
    # Move to the next 30-second interval
    current_time += pd.Timedelta(seconds=30)

# Print the extracted data
print(extracted_data)

# Save the extracted data to a new CSV file
extracted_data.to_csv('extracted_data.csv', index=False)
