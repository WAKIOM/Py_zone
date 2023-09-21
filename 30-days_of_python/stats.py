#!/usr/bin/python3
import pandas as pd

def custom_describe(dataframe, *columns):
    summary_stats = {}
    if len(columns) == 0:
        columns = dataframe.columns
    
    for col_name in columns:
        col = dataframe[col_name]
        summary_stats[f'{col_name}_mean'] = col.mean()
        summary_stats[f'{col_name}_std'] = col.std()
        summary_stats[f'{col_name}_min'] = col.min()
        summary_stats[f'{col_name}_25%'] = col.quantile(0.25)
        summary_stats[f'{col_name}_50%'] = col.median()
        summary_stats[f'{col_name}_75%'] = col.quantile(0.75)
        summary_stats[f'{col_name}_max'] = col.max()
    
    return pd.DataFrame(summary_stats, orient='index', columns=['value'])

# Example usage:
data = {'col1': [1, 2, 3, 4, 5],
        'col2': [10, 20, 30, 40, 50],
        'col3': [5, 4, 3, 2, 1]}

df = pd.DataFrame(data)

# Describe all columns
result_all = custom_describe(df)

# Describe specific columns
result_specific = custom_describe(df, 'col1', 'col2')

print("Summary statistics for all columns:")
print(result_all)

print("\nSummary statistics for specific columns:")
print(result_specific)

