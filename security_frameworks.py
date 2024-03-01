import paramiko
from cryptography.fernet import Fernet

class SecurityManager:
    """
    Cette classe gère les aspects de sécurité du système de bouton de panique, y compris
    la sécurité de la communication SSH et le chiffrement des données.
    """

    def __init__(self):
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.encryption_key = None

    def generate_encryption_key(self):
        """
        Génère une nouvelle clé de chiffrement pour le stockage sécurisé des données et la communication.
        """
        self.encryption_key = Fernet.generate_key()

    def get_encryption_key(self):
        """
        Retourne la clé de chiffrement actuelle.
        """
        return self.encryption_key

    def encrypt_data(self, data):
        """
        Chiffre les données en utilisant la clé de chiffrement actuelle.
        """
        if not self.encryption_key:
            raise ValueError("Clé de chiffrement non définie.")
        fernet = Fernet(self.encryption_key)
        encrypted_data = fernet.encrypt(data.encode())
        return encrypted_data

    def decrypt_data(self, encrypted_data):
        """
        Déchiffre les données en utilisant la clé de chiffrement actuelle.
        """
        if not self.encryption_key:
            raise ValueError("Clé de chiffrement non définie.")
        fernet = Fernet(self.encryption_key)
        decrypted_data = fernet.decrypt(encrypted_data).decode()
        return decrypted_data

    def establish_ssh_connection(self, hostname, port, username, password):
        """
        Établit une connexion SSH à un appareil réseau.
        """
        try:
            self.ssh_client.connect(hostname, port=port, username=username, password=password)
            print(f"Connexion réussie à {hostname}")
        except paramiko.SSHException as e:
            print(f"Échec de la connexion à {hostname}: {e}")

    def execute_ssh_command(self, command):
        """
        Exécute une commande sur l'appareil distant via SSH.
        """
        stdin, stdout, stderr = self.ssh_client.exec_command(command)
        return stdout.read().decode()

    def close_ssh_connection(self):
        """
        Ferme la connexion SSH actuelle.
        """
        self.ssh_client.close()
        print("Connexion SSH fermée.")

# Exemple d'utilisation
if __name__ == "__main__":
    security_manager = SecurityManager()
    security_manager.generate_encryption_key()
    encryption_key = security_manager.get_encryption_key()
    print(f"Clé de chiffrement: {encryption_key}")

    # Exemple de chiffrement et déchiffrement des données
    encrypted_data = security_manager.encrypt_data("Informations sensibles")
    print(f"Données chiffrées: {encrypted_data}")
    decrypted_data = security_manager.decrypt_data(encrypted_data)
    print(f"Données déchiffrées: {decrypted_data}")

    # Exemple d'établissement d'une connexion SSH et d'exécution d'une commande
    security_manager.establish_ssh_connection("192.168.1.1", 22, "admin", "password")
    output = security_manager.execute_ssh_command("show ip interface brief")
    print(output)
    security_manager.close_ssh_connection()
