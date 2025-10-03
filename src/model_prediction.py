import logging
import joblib
import pandas as pd

logging.basicConfig( filename = 'logs/Model Prediction.log',
                      level = logging.INFO,
                      format = '%(asctime)s - %(levelname)s - %(message)s')

def Prediction(X_test, model_path):
    ''' Function for model Prediction
    Args:
      X_test: Predicting Variables
    Returns
      Y_pred: Predicted Values
    '''
    try:
      # Ensuring Right Number of Columns is to be Predicted
      if len(X_test.columns) != 30:
          logging.warning(' The dataset provided is invalid ')
      logging.info('Model Prediction In Progress')
      model = joblib.load(model_path)
      y_prob = model.predict_proba(X_test)[ : ,1]
      y_pred = (y_prob > 0.3).astype(int)
      return y_pred
    except Exception as e:
      logging.exception(f" An Error Occurred During Model Prediction {e}")
