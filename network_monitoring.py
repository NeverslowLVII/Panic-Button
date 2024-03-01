import threading
import time
from network_devices import NetworkDevice
from config import NETWORK_DEVICES
from intrusion_detection import IntrusionDetectionSystem
from logging import log_event

class NetworkMonitor:
    def __init__(self):
        """
        Initialise le moniteur réseau avec les dispositifs réseau configurés et les systèmes de détection d'intrusion.
        """
        self.devices = [NetworkDevice(device_info) for device_info in NETWORK_DEVICES.values()]
        self.ids_systems = [IntrusionDetectionSystem(system_type) for system_type in ['snort', 'suricata']]
        self.monitoring = False

    def start_monitoring(self):
        """
        Démarre la surveillance du réseau et les vérifications de détection d'intrusion dans des threads séparés.
        """
        self.monitoring = True
        device_thread = threading.Thread(target=self.monitor_devices)
        ids_thread = threading.Thread(target=self.monitor_ids)

        device_thread.start()
        ids_thread.start()

        device_thread.join()
        ids_thread.join()

    def stop_monitoring(self):
        """
        Arrête la surveillance du réseau et les vérifications de détection d'intrusion.
        """
        self.monitoring = False

    def monitor_devices(self):
        """
        Vérifie en continu la connectivité aux dispositifs réseau.
        """
        while self.monitoring:
            for device in self.devices:
                device.connect()
                time.sleep(5)  # Attendre 5 secondes avant la prochaine vérification
                device.disconnect()
            time.sleep(60)  # Vérifier chaque minute

    def monitor_ids(self):
        """
        Vérifie en continu les alertes provenant des systèmes de détection d'intrusion.
        """
        while self.monitoring:
            for ids in self.ids_systems:
                alerts = ids.check_alerts()
                if alerts:
                    for alert in alerts:
                        log_event(f"Alerte IDS : {alert}")
            time.sleep(30)  # Vérifier toutes les 30 secondes

if __name__ == "__main__":
    network_monitor = NetworkMonitor()
    try:
        network_monitor.start_monitoring()
    except KeyboardInterrupt:
        network_monitor.stop_monitoring()
        print("Surveillance arrêtée.")
