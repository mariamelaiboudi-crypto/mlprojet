import sys
import os
from src.exception import CustomException
import dill


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