import pandas as pd

from loader import data_loader


try :
    data = data_loader("sales_data_sample.csv")

except FileNotFoundError:
    print("File Note Found!")

else:
    print(data.head())

