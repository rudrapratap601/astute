import pandas as pd 


def data_loader(data_name: str):

    """This Function will load data - this is a simple version which only support csv files
    
    This function takes name of the data with it's extention and return the dataset (Data Frame)
    """

    df = pd.read_csv(rf"C:\Users\rudra\OneDrive\Desktop\astute\data\{data_name}", encoding = "latin1")

    return df
