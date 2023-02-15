import pandas as pd

# Load the csv file into a pandas DataFrame
df = pd.read_csv("C:\Adam\Experiment Data\AntiCrush\Crush_Test\data_longtest_heav01.csv", low_memory=False)

# Convert all columns to numeric and replace non-numeric values with NaN
df = df.apply(pd.to_numeric, errors='coerce')

# Drop all rows with NaN values
df.dropna(inplace=True)

# Reset the index
df.reset_index(drop=True, inplace=True)

# Save the cleaned DataFrame to a new csv file
df.to_csv("C:\Adam\Experiment Data\AntiCrush\Crush_Test\data_longtest_heav01cleaned.csv", index=False)