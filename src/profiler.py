import pandas as pd

from loader import data_loader

def profile_dataset(df: pd.DataFrame) -> dict:

     column_profiles = {}

     for col in df.columns:

         missing_count = df[col].isnull().sum()

         column_profiles[col] = {

             "dtype" : str(df[col].dtype),
             "missing_count" : int(missing_count),
             "missing_percentage" : round(float(missing_count / df.shape[0] * 100), 2),
             "unique_count" : int(df[col].nunique())
         }

     data_dict = {
         "rows" : int(df.shape[0]),
         "columns" : int(df.shape[1]),
         "duplicates" : int(df.duplicated().sum()),
         "column-profiles" : column_profiles

     }

     return data_dict
    

try :
    data = data_loader("sales_data_sample.csv")

except FileNotFoundError:
    print("File Note Found!")

else:
    print(profile_dataset(data))

