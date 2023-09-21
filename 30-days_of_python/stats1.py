#!/usr/bin/python3
import pandas as pd
import os
def custom_describe(dataframe):
    columns = dataframe.columns
    summary_stats = {
        'mean': [],
        'std': [],
        'min': [],
        '25%': [],
        '50%': [],
        '75%': [],
        'max': []
    }
    
    for col_name in columns:
        col = dataframe[col_name]
        summary_stats['mean'].append(col.mean())
        summary_stats['std'].append(col.std())
        summary_stats['min'].append(col.min())
        summary_stats['25%'].append(col.quantile(0.25))
        summary_stats['50%'].append(col.median())
        summary_stats['75%'].append(col.quantile(0.75))
        summary_stats['max'].append(col.max())
    
    return pd.DataFrame(summary_stats, index=columns)

# Get the current directory where the script is located
# current_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the file path relative to the current directory
#file_path = os.path.join(current_directory, 'Sales.csv')

df = pd.read_csv("Sales.csv") # Load the dataset from the CSV file
numeric_df = df.select_dtypes(include='number')
result = custom_describe(numeric_df)

print("Summary statistics for all columns:")
print(result)


