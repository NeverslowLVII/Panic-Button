import getpass
from security_frameworks import SecurityManager

class AuthenticationManager:
    """
    Cette classe gère le processus d'authentification pour le système de bouton de panique,
    y compris l'authentification multi-facteurs et le stockage sécurisé des mots de passe.
    """

    def __init__(self):
        self.security_manager = SecurityManager()
        self.users = self.load_users()

    def load_users(self):
        """
        Charge les identifiants des utilisateurs à partir d'un stockage sécurisé.
        Retourne un dictionnaire des noms d'utilisateur et de leurs mots de passe cryptés.
        """
        # Ceci est un espace réservé pour le chargement des données utilisateur. Dans une application réelle,
        # cela proviendrait d'une base de données sécurisée ou d'un fichier crypté.
        encrypted_password = self.security_manager.encrypt_data('password123')
        return {'admin': encrypted_password}

    def authenticate_user(self, username, password):
        """
        Authentifie un utilisateur par son nom d'utilisateur et son mot de passe.
        Retourne True si l'authentification est réussie, False sinon.
        """
        if username in self.users:
            encrypted_password = self.users[username]
            decrypted_password = self.security_manager.decrypt_data(encrypted_password).decode()
            return password == decrypted_password
        return False

    def multi_factor_authentication(self, username):
        """
        Effectue une authentification multi-facteurs pour le nom d'utilisateur donné.
        Retourne True si réussi, False sinon.
        """
        # Espace réservé pour le processus MFA. Dans une application réelle, cela pourrait impliquer
        # l'envoi d'un code au téléphone ou à l'email de l'utilisateur et sa vérification.
        print(f"Authentification multi-facteurs initiée pour {username}.")
        mfa_code = input("Entrez le code MFA envoyé à votre appareil : ")
        return mfa_code == "123456"  # Ceci est un espace réservé. En pratique, utilisez un code dynamique.

def main():
    auth_manager = AuthenticationManager()
    username = input("Nom d'utilisateur : ")
    password = getpass.getpass("Mot de passe : ")

    if auth_manager.authenticate_user(username, password):
        if auth_manager.multi_factor_authentication(username):
            print("Authentification réussie.")
        else:
            print("Échec de l'authentification multi-facteurs.")
    else:
        print("Échec de l'authentification.")

if __name__ == "__main__":
    main()
