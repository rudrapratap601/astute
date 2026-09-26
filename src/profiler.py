import pandas as pd

from loader import data_loader

def profile_dataset(df: pd.DataFrame):

     column_profiles = {}

     for i in range(df.shape[1]):

         column_profiles[df.columns[i]] = {

             "dtype" : df[df.columns[i]].dtype,
             "missing_count" : int(df[df.columns[i]].isnull().sum()),
             "missing_percentage" : round(float(df[df.columns[i]].isnull().sum() / df.shape[0] * 100), 2),
             "unique_count" : int(df[df.columns[i]].nunique())
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

