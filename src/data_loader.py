import pandas as pd
import logging

logging.basicConfig(level = logging.INFO)

def Data_Loader(data_path:str):
    '''
    Function that loads the data
    Args:
        data_path: path to the csv file containing the data
    Returns:
        data in a dataframe
    '''
    try:
        logging.info("Data Loading Initialized")
        return pd.read_csv(data_path)
    except Exception as e:
        logging.exception(f"An Error Occurred During Data Loading {e}")
