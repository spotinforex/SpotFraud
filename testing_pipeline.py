from src.data_loader import Data_Loader
from src.data_splitter import data_split
from src.model_training import Model_Training
from src.model_prediction import Prediction
from src.params import Model_Params

path = "data/creditcard.csv"

if __name__ == "__main__":
    data = Data_Loader(path)
    X_train, X_test, y_train, y_test = data_split(data, "Class")
    #model = Model_Training()
    #params = Model_Params()
    #model_path = model.train(X_train, y_train, **params.to_dict())
    y_pred = Prediction(X_test, 'models\model_V1.pkl')
    print (y_pred)


