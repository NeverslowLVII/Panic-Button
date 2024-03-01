import logging
from datetime import datetime
import os

# Créer un répertoire de logs s'il n'existe pas
if not os.path.exists('logs'):
    os.makedirs('logs')

# Configurer le logging
logging.basicConfig(filename=f'logs/panic_button_{datetime.now().strftime("%Y-%m-%d")}.log',
                    filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)

def log_action(action_message, level='info'):
    """
    Enregistre une action dans le fichier journal du système.
    :param action_message: Le message à enregistrer.
    :param level: Le niveau de logging ('info', 'warning', 'error').
    """
    if level == 'info':
        logging.info(action_message)
    elif level == 'warning':
        logging.warning(action_message)
    elif level == 'error':
        logging.error(action_message)
    else:
        logging.info(f"Niveau de logging inconnu pour le message : {action_message}")

def log_error(error_message):
    """
    Fonction de commodité pour enregistrer une erreur.
    :param error_message: Le message d'erreur à enregistrer.
    """
    log_action(error_message, 'error')

def log_warning(warning_message):
    """
    Fonction de commodité pour enregistrer un avertissement.
    :param warning_message: Le message d'avertissement à enregistrer.
    """
    log_action(warning_message, 'warning')

# Exemple d'utilisation :
# log_action("Bouton de panique activé.", "info")
# log_error("Échec de l'isolation de l'appareil 192.168.1.1.")
# log_warning("Le temps de réponse de l'appareil 192.168.1.2 est lent.")
