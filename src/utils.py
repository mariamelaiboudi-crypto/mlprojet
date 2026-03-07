import sys
import os
from src.exception import CustomException
import dill
from sklearn.metrics import r2_score


def save_obj(file_path, data):
    try:
        # créer le dossier artifacts si il n'existe pas
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        # sauvegarder l'objet
        with open(file_path, 'wb') as file_obj:
            dill.dump(data, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    
def evaluate_model(X_train,y_train,X_test,y_test,models) :
    report={}
    try:

        for i in range(len(list(models))):
            model=list(models.values())[i]
           
            model.fit(X_train,y_train)
            y_pre=model.predict(X_test)
            r2_test_score=r2_score(y_test,y_pre)

            report[list(models.keys())[i]]=r2_test_score

        return report


    except Exception as e:
        raise CustomException(e,sys)
