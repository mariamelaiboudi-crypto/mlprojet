import sys  # bibliothèque système utilisée pour obtenir les informations sur l'erreur (traceback)
from src.logger import logging

# Fonction qui construit un message d'erreur détaillé
def error_message_detail(error, error_details: sys):
    # exc_info() retourne : (type, valeur, traceback)
    _, _, exc_error = error_details.exc_info()

    # récupérer le nom du fichier où l'erreur s'est produite
    file_name = exc_error.tb_frame.f_code.co_filename

    # créer un message d'erreur complet avec :
    # - le fichier
    # - la ligne de l'erreur
    # - le message de l'erreur
    error_message = 'error occured in python script name [{0}], line number [{1}] error message [{2}]'.format(
        file_name,
        exc_error.tb_lineno,
        str(error)
    )

    return error_message  # retourner le message


# Création d'une exception personnalisée
class CustomException(Exception):

    # constructeur de la classe
    def __init__(self, error_message, error_details: sys):
        # appeler le constructeur de la classe parent (Exception)
        super().__init__(error_message)

        # générer un message d'erreur détaillé
        self.error_message = error_message_detail(
            error_message,
            error_details=error_details
        )

    # méthode appelée quand on affiche l'erreur
    def __str__(self):
        return self.error_message
    



