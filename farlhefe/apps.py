import signal
from django.conf import settings

from paho.mqtt.client import Client as MQTTClient

from django.apps import AppConfig

from . import mqtt
from . import settings


class FarlhefeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'farlhefe'


    def ready(self) -> None:
        mqtt_client = MQTTClient(settings.MQTT_CLIENT_ID)
        mqtt_client.connect(settings.MQTT_BROKER_HOST)

        mqtt_client.on_connect = mqtt.on_connect

        mqtt_client.loop_start()

        for s in (signal.SIGINT, signal.SIGTERM):
            signal.signal(s, mqtt_client.loop_stop)
