import pandas as pd

class DataProcessor:
    def __init__(self, file1, file2):
        self.df1 = pd.read_csv(file1)
        self.df2 = pd.read_csv(file2)

    # Merge tables
    def merge_tables(self, key):
        return pd.merge(self.df1, self.df2, on=key)

    # Select specific columns
    def select_columns(self, df, columns):
        return df[columns]

    # Filter / split data
    def filter_data(self, df, column, value):
        return df[df[column] == value]

    # Preview
    def preview(self, df, rows=5):
        return df.head(rows)