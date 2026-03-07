import os 
import sys
import pandas as pd
from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass 
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from xgboost import XGBRegressor
from catboost import CatBoostRegressor
from sklearn.ensemble import AdaBoostRegressor
from src.utils import evaluate_model,save_obj
from sklearn.metrics import r2_score
 

@dataclass
class ModelTrainerConfig:
    file_path_model_trainer=os.path.join('artifacts','modelTrainer.pkl')

class ModelTrainer:
    def __init__(self):
        self.file_path_model=ModelTrainerConfig()

    def initiate_model_trainer(self, train,test):
        try:
            logging.info('spliting data')
            xtrain,ytrain,xtest,ytest=(
                train[:,:-1],
                train[:,-1],
                test[:,:-1],
                test[:,-1]
            )
            models_trainer = {

                "Random Forest": RandomForestRegressor(),

                "Decision Tree": DecisionTreeRegressor(),

                "Gradient Boosting": GradientBoostingRegressor(),

                "Linear Regression": LinearRegression(),

                "K-Neighbors Regressor": KNeighborsRegressor(),

                "XGBoost Regressor": XGBRegressor(),

                "CatBoost Regressor": CatBoostRegressor(verbose=False),

                "AdaBoost Regressor": AdaBoostRegressor()

            }

            report_models:dict=evaluate_model(  
                X_train=xtrain,
                y_train=ytrain,
                X_test=xtest,
                y_test=ytest,
                models=models_trainer)
            best_score=max(sorted(report_models.values()))
#             best_model_name = list(report_models.keys())[ 
#                 list(report_models.values()).index(best_score)
# ]
            best_model_name = max(report_models, key=report_models.get)

            best_model = models_trainer[best_model_name]
            if best_score<0.6:
                raise CustomException('no best model found')

            logging.info(f'best found model ')

            save_obj(
            file_path=self.file_path_model.file_path_model_trainer, 
            data=best_model)
            predicted=  best_model.predict(xtest)
            score=r2_score(ytest,predicted)
            return score, best_model_name,report_models
        except Exception as e:
            raise CustomException(e,sys)
