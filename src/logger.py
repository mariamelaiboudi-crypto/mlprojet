import logging
import os
from datetime import datetime

# nom du fichier log avec timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# chemin du dossier logs
logs_path = os.path.join(os.getcwd(), "logs")

# créer le dossier logs
os.makedirs(logs_path, exist_ok=True)

# chemin complet du fichier log
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# configuration du logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


     
