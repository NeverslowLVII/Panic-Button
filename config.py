# config.py

# Ce fichier de configuration contient les paramètres globaux et les constantes pour le système de bouton de panique.

# Configuration des appareils réseau
# Définir les appareils réseau à surveiller et potentiellement isoler en cas d'incident de sécurité.
NETWORK_DEVICES = {
    'router1': {
        'device_type': 'cisco_ios',
        'ip': '192.168.1.1',
        'username': 'admin',
        'password': 'password',
        'secret': 'secret',  # Pour les appareils nécessitant un mode enable.
    },
    'switch1': {
        'device_type': 'cisco_ios',
        'ip': '192.168.1.2',
        'username': 'admin',
        'password': 'password',
        'secret': 'secret',
    },
    # Ajouter plus d'appareils selon les besoins.
}

# Configuration des cadres de sécurité
# Configuration pour les cadres de sécurité comme Paramiko et Cryptography.
SECURITY_FRAMEWORKS_CONFIG = {
    'paramiko': {
        'ssh_port': 22,
        'timeout': 30,  # Délai d'attente en secondes pour les connexions SSH.
    },
    'cryptography': {
        'encryption_algorithm': 'AES256',
    },
}

# Configuration du système de détection d'intrusion
# Paramètres pour les outils IDS comme Snort ou Suricata.
INTRUSION_DETECTION_CONFIG = {
    'snort': {
        'log_directory': '/var/log/snort',
        'alert_file': 'alert.fast',
    },
    'suricata': {
        'log_directory': '/var/log/suricata',
        'alert_file': 'eve.json',
    },
}

# Configuration de la surveillance réseau
# Configuration pour les outils de surveillance réseau.
NETWORK_MONITORING_CONFIG = {
    'monitoring_interval': 60,  # Temps en secondes entre chaque cycle de surveillance.
}

# Configuration du bouton de panique
# Paramètres liés au fonctionnement de la fonctionnalité du bouton de panique.
PANIC_BUTTON_CONFIG = {
    'isolation_mode': 'manual',  # Peut être 'manual' ou 'automatic'.
    'notification_email': 'security@company.com',  # Email à notifier en cas d'isolation.
}

# Configuration de l'interface utilisateur
# Paramètres pour l'interface utilisateur du système de bouton de panique.
USER_INTERFACE_CONFIG = {
    'web_interface_port': 8080,
}

# Configuration de l'authentification
# Paramètres pour le mécanisme d'authentification.
AUTHENTICATION_CONFIG = {
    'multi_factor': True,
    'allowed_users': ['admin', 'security_officer'],
}

# Configuration de la journalisation
# Paramètres pour la journalisation et les pistes d'audit.
LOGGING_CONFIG = {
    'log_file': 'panic_button_system.log',
    'log_level': 'INFO',  # Peut être 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'.
}

# Configuration de la récupération
# Paramètres pour le processus de récupération après un incident.
RECOVERY_CONFIG = {
    'auto_recovery_enabled': True,
    'recovery_script_path': '/path/to/recovery_script.sh',
}


