#!/usr/bin/python3
import pandas as pd
import numpy as np

def custom_describe(dataframe, percentiles=None, include=None, exclude=None):
    """
    Generate summary statistics of numeric columns in a DataFrame.

    Parameters:
        dataframe (pd.DataFrame): The DataFrame to describe.
        percentiles (list-like, optional): The percentiles to include in the output.
            Default is [25%, 50%, 75%].
        include (str or list-like, optional): Specify which data types to include.
            By default, all numeric types are included.
        exclude (str or list-like, optional): Specify which data types to exclude.
            By default, nothing is excluded.

    Returns:
        pd.DataFrame: Summary statistics of the numeric columns.
    """
    if dataframe.empty:
        return pd.DataFrame([])

    if include is None:
        include = [np.number]

    if exclude is None:
        exclude = []

    numeric_cols = dataframe.select_dtypes(include=include, exclude=exclude)

    if numeric_cols.empty:
        raise ValueError("No numeric types to summarize")

    if percentiles is None:
        percentiles = [0.25, 0.5, 0.75]

    agg_funcs = {
        'Count': 'count',
        'Mean': 'mean',
        'Std': 'std',
        'Min': 'min',
        '25%': lambda x: x.quantile(0.25),
        '50%': 'median',
        '75%': lambda x: x.quantile(0.75),
        'Max': 'max'
    }

    result_df = numeric_cols.agg(agg_funcs).T

    return result_df

# Example usage:
data = {'Age': [25, 30, 35, 40, 45],
        'Salary': [50000, 60000, 75000, 80000, 90000]}
df = pd.DataFrame(data)

summary = custom_describe(df)
print(summary)

