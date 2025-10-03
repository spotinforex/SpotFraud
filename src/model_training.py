import pandas as pd
from sklearn.ensemble import RandomForestClassifier as RFC
import logging
from abc import ABC, abstractmethod
import joblib
import logging

logging.basicConfig(filename = 'logs/Model_Training.log',
                    level = logging.INFO,
                    format = '%(asctime)s - %(levelname)s - %(message)s')

class Model_Development(ABC):
    ''' Abstract Class For Model Development '''
    @abstractmethod
    def train(self, X_train, y_train, **params):
        pass

class Model_Training(Model_Development):
  ''' Class for training LightGBM Model '''
  def train(self, X_train, y_train, **params):
      ''' Function for training the model
        Args:
          X_train: Training features
          y_train: Training target
          params: Parameters for model training
        Returns:
          path to the saved model
        '''
      try:
          logging.info(" Model Training in Progress")
          model = RFC(**params)
          model.fit(X_train,y_train)
          logging.info('Model Training Complete')
          model_path = 'models/model_V1.pkl'
          joblib.dump(model, model_path)
          logging.info('Model Saved Successfully')
          return model_path

      except Exception as e:
          logging.exception(f'An Error Occurred during Model Training or Saving {e}')



