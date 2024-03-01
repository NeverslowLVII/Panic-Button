import threading
from network_devices import NetworkDevice
from config import NETWORK_DEVICES
from logging import log_action
from recovery import initiate_recovery_process
from user_interface import display_alert, request_confirmation

class PanicButton:
    def __init__(self):
        self.devices = [NetworkDevice(device_info) for _, device_info in NETWORK_DEVICES.items()]
        self.lock = threading.Lock()

    def isolate_network_device(self, device):
        """
        Isole un appareil réseau en le déconnectant.
        :param device: L'instance de NetworkDevice à isoler.
        """
        try:
            device.disconnect()
            log_action(f"Appareil {device.device_info['ip']} isolé.")
        except Exception as e:
            log_action(f"Échec de l'isolation de l'appareil {device.device_info['ip']}: {e}")

    def activate_panic_mode(self):
        """
        Active le mode panique en isolant tous les appareils réseau.
        """
        with self.lock:
            confirmation = request_confirmation("Êtes-vous sûr de vouloir activer le mode panique ? (oui/non) : ")
            if confirmation.lower() == 'oui':
                display_alert("Activation du mode panique. Isolation de tous les appareils...")
                threads = []
                for device in self.devices:
                    t = threading.Thread(target=self.isolate_network_device, args=(device,))
                    t.start()
                    threads.append(t)
                for t in threads:
                    t.join()
                log_action("Mode panique activé. Tous les appareils sont isolés.")
                initiate_recovery_process()
            else:
                display_alert("Activation du mode panique annulée.")

if __name__ == "__main__":
    panic_button = PanicButton()
    # Exemple d'utilisation
    panic_button.activate_panic_mode()
