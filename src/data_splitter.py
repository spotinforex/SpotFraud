from src.data_loader import Data_Loader

from sklearn.model_selection import train_test_split
import pandas as pd
import logging


logging.basicConfig(level = logging.INFO)

def data_split(data:pd.DataFrame,target_column:str):
    '''
    function for splitting data into train and test set
    Args:
      data: the dataframe
      target_column: target column variable in the dataset
    Returns:
      X_train: training features
      X_test: testing features
      y_train: training target
      y_test: testing target
    '''
    try:
        logging.info(" Data Splitting In Progress")
        X = data.drop(target_column, axis = 1)
        y = data[target_column]
        X_train,X_test,y_train,y_test = train_test_split(X,y, random_state = 42, test_size = 0.2,
            shuffle = True, stratify = y)
        logging.info("Data Splitted Successfully")
        return X_train,X_test, y_train, y_test

    except Exception as e:
        logging.exception(f"An Error Occurred while splitting data {e}")



