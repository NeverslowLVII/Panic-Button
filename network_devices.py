from config import NETWORK_DEVICES
from netmiko import ConnectHandler
from security_frameworks import secure_connection

class NetworkDevice:
    def __init__(self, device_info):
        """
        Initialise l'instance NetworkDevice avec les informations de l'appareil.
        :param device_info: Dictionnaire contenant les détails de l'appareil.
        """
        self.device_info = device_info
        self.connection = None

    def connect(self):
        """
        Établit une connexion sécurisée avec l'appareil réseau en utilisant Netmiko.
        """
        try:
            # Encapsule la connexion avec les configurations des cadres de sécurité
            secure_device_info = secure_connection(self.device_info)
            self.connection = ConnectHandler(**secure_device_info)
            print(f"Connexion réussie à {self.device_info['ip']}")
        except Exception as e:
            print(f"Échec de la connexion à {self.device_info['ip']}: {e}")

    def disconnect(self):
        """
        Ferme la connexion avec l'appareil réseau.
        """
        if self.connection:
            self.connection.disconnect()
            print(f"Déconnecté de {self.device_info['ip']}")

    def execute_command(self, command):
        """
        Exécute une commande sur l'appareil réseau et retourne la sortie.
        :param command: Commande à exécuter.
        :return: Sortie de la commande.
        """
        if not self.connection:
            print("Appareil non connecté. Veuillez établir une connexion d'abord.")
            return None
        try:
            return self.connection.send_command(command)
        except Exception as e:
            print(f"Échec de l'exécution de la commande sur {self.device_info['ip']}: {e}")
            return None

def initialize_network_devices():
    """
    Initialise et retourne une liste d'instances NetworkDevice basées sur la configuration.
    :return: Liste d'instances NetworkDevice.
    """
    devices = []
    for device_name, device_info in NETWORK_DEVICES.items():
        device = NetworkDevice(device_info)
        devices.append(device)
    return devices

# Exemple d'utilisation
if __name__ == "__main__":
    devices = initialize_network_devices()
    for device in devices:
        device.connect()
        output = device.execute_command("show version")
        print(output)
        device.disconnect()
