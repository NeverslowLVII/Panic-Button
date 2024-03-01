# user_interface.py

def display_alert(message):
    """
    Affiche un message d'alerte à l'utilisateur.
    :param message: Le message à afficher.
    """
    print(f"ALERT: {message}")

def request_confirmation(prompt):
    """
    Demande une confirmation à l'utilisateur avec une invite oui/non.
    :param prompt: L'invite à afficher à l'utilisateur.
    :return: True si l'utilisateur confirme, False sinon.
    """
    response = input(prompt).lower()
    while response not in ['yes', 'no']:
        print("Veuillez répondre par 'yes' ou 'no'.")
        response = input(prompt).lower()
    return response == 'yes'

def show_menu():
    """
    Affiche les options du menu principal à l'utilisateur.
    """
    print("\n--- Menu du Système du Bouton de Panique ---")
    print("1. Voir les Appareils Réseau")
    print("2. Activer le Mode Panique")
    print("3. Initier le Processus de Récupération")
    print("4. Quitter")
    print("--------------------------------")

def get_user_choice():
    """
    Obtient le choix de menu de l'utilisateur.
    :return: Le choix de l'utilisateur sous forme d'entier.
    """
    try:
        choice = int(input("Entrez votre choix : "))
        return choice
    except ValueError:
        print("Veuillez entrer un nombre valide.")
        return None

def display_network_devices(devices):
    """
    Affiche une liste des appareils réseau.
    :param devices: Une liste d'instances de NetworkDevice.
    """
    print("\n--- Appareils Réseau ---")
    for device in devices:
        print(f"IP: {device.device_info['ip']}, Type: {device.device_info['device_type']}")
    print("-----------------------")
