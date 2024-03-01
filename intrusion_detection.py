# intrusion_detection.py

import os
import json
from config import INTRUSION_DETECTION_CONFIG
from logging import log_incident

class IntrusionDetectionSystem:
    def __init__(self, system_type):
        """
        Initialise le système de détection d'intrusion avec le type spécifié (par exemple, 'snort' ou 'suricata').
        :param system_type: Le type du système IDS.
        """
        self.system_type = system_type
        self.config = INTRUSION_DETECTION_CONFIG.get(system_type, {})
        self.log_directory = self.config.get('log_directory', '')
        self.alert_file = self.config.get('alert_file', '')

    def check_alerts(self):
        """
        Vérifie les nouvelles alertes dans le fichier journal du système IDS.
        """
        alert_path = os.path.join(self.log_directory, self.alert_file)
        try:
            if self.system_type == 'snort':
                # En supposant le format alert.fast de Snort pour simplifier
                with open(alert_path, 'r') as alert_file:
                    alerts = alert_file.readlines()
                    for alert in alerts:
                        print(f"Alerte détectée : {alert.strip()}")
                        log_incident(alert.strip())
            elif self.system_type == 'suricata':
                # En supposant le format eve.json de Suricata
                with open(alert_path, 'r') as alert_file:
                    for line in alert_file:
                        alert = json.loads(line)
                        print(f"Alerte détectée : {alert['alert']['signature']}")
                        log_incident(alert['alert']['signature'])
            else:
                print(f"Type de système IDS non pris en charge : {self.system_type}")
        except FileNotFoundError:
            print(f"Fichier d'alerte non trouvé : {alert_path}")
        except Exception as e:
            print(f"Erreur lors de la vérification des alertes : {e}")

def initialize_intrusion_detection_systems():
    """
    Initialise et retourne une liste d'instances de système de détection d'intrusion basées sur la configuration.
    :return: Liste d'instances de IntrusionDetectionSystem.
    """
    systems = []
    for system_type in INTRUSION_DETECTION_CONFIG.keys():
        system = IntrusionDetectionSystem(system_type)
        systems.append(system)
    return systems

if __name__ == "__main__":
    # Exemple d'utilisation
    ids_systems = initialize_intrusion_detection_systems()
    for system in ids_systems:
        system.check_alerts()
