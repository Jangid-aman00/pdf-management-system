import pandas as pd


class DataProcessor:
    """Process and manipulate CSV data"""
    
    def __init__(self, file1, file2):
        """Initialize with two CSV files"""
        self.df1 = pd.read_csv(file1)
        self.df2 = pd.read_csv(file2)
    
    def merge_tables(self, on):
        """Merge two tables on a common column"""
        return pd.merge(self.df1, self.df2, on=on, how='inner')
    
    def select_columns(self, dataframe, columns):
        """Select specific columns from dataframe"""
        return dataframe[columns]
    
    def filter_data(self, dataframe, column, value):
        """Filter dataframe where column value is greater than specified value"""
        return dataframe[dataframe[column] > value]
    
    def preview(self, dataframe, rows=5):
        """Preview first N rows of dataframe"""
        return dataframe.head(rows)
