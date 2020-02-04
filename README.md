# Aufgabe-11

Der Schwarmroboter fährt auf einen MQTT Befehl gerade aus erzeugt dabei 4 Bilder im Abstand von jeweils 2 Sekunden, und übermittelt diese via MQTT an einen Broker.

## Anleitung

* Das Skript wird auf dem Pi mit `sudo python3 Python/Main.py` ausgeführt
* Das Skript zum Empfangen der Bilder liegt in [der Broker Repository](https://github.com/GretaThunbergUltras/Broker), unter `final/final/receive_file_.py`. Die Doku für das Empfangen liegt ebenfalls in dieser Repo.
* Der Start-Befehl `mosquitto_pub -h gruppe11 -t img_capture -m execMakePhoto` kann von jedem Pi mit Mosquitto im Pi-Net ausgeführt werden.
