import pandas as pd

from loader import data_loader

def profile_dataset(df: pd.DataFrame):

     column_profiles = {}

     for i in df.columns:

         column_profiles[i] = {

             "dtype" : df[i].dtype,
             "missing_count" : int(df[i].isnull().sum()),
             "missing_percentage" : round(float(df[i].isnull().sum() / df.shape[0] * 100), 2),
             "unique_count" : int(df[i].nunique())
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

