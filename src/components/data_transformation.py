import pandas  as  pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.pipeline import Pipeline 
from sklearn.compose import ColumnTransformer
from dataclasses import dataclass
import os
from src.logger import logging
from src.exception import CustomException
import sys
from src.utils import save_obj
@dataclass 
class DataTransformationConfig:
    preprocessing_obj_path=os.path.join('artifacts','preprocessing.pkl')

class DataTransformation:
    def __init__(self):
          self.DataTransformationConfig=DataTransformationConfig()
    def Transform_obj(self):
          '''
          this function is responsible for data transformation
          '''
          try:
             cat_col=[
                 "gender",
                  "race_ethnicity",
                  "parental_level_of_education",
                  "lunch",
                  "test_preparation_course"
                  ]
             num_col=[
                 "reading_score",
                 "writing_score"]
             cat_pipeline=Pipeline(
                    steps=[
                        ('impute',SimpleImputer(strategy='most_frequent')),
                        ('encoder',OneHotEncoder())
                       
                    ]
                )
             num_pipeline=Pipeline(
                 steps=[
                     ('impute',SimpleImputer(strategy='most_frequent')),
                     ('scaler',StandardScaler())
                 ]
             )

             logging.info('num col standarscaler completed')
             logging.info('cat col encoding  completed')


             preprocessor = ColumnTransformer(
                    transformers=[
                        ('numpipeline', num_pipeline, num_col),
                        ('catpipeline', cat_pipeline, cat_col)
                    ]
                )
             return preprocessor

          except Exception as e:
              raise  CustomException(e,sys)
        
    def initialise_Data_Transformation(self,train_path,test_path):
        try:
             logging.info('read train ad test data')
             train=pd.read_csv(train_path)
             test=pd.read_csv(test_path)
             target ='math_score'

             train_input_df=train.drop(target,axis=1)
             target_feature_train_df=train[target]
             test_input_df=test.drop(target,axis=1)
              
             
             target_feature_test_df=test[target]
             
             preprocessing_obj=self.Transform_obj()
             logging.info('applying preprocessing object on training data')
             input_train_arr=  preprocessing_obj.fit_transform(train_input_df)
             input_test_arr=  preprocessing_obj.transform(test_input_df)
             train_arr=np.c_[input_train_arr,np.array(target_feature_train_df)]
             test_arr=np.c_[input_test_arr,np.array(target_feature_test_df)]
             logging.info('saved preprocessing obj')

             save_obj(
                 file_path=self.DataTransformationConfig.preprocessing_obj_path,
                 data=preprocessing_obj
             )
             return (
                 train_arr,
                 test_arr,
                 self.DataTransformationConfig.preprocessing_obj_path
             )
        except Exception as e:
            raise CustomException(e,sys)        
