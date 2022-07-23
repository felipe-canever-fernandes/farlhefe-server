from . import settings


def on_connect(client, userdata, flags, result):
    del userdata
    del flags
    del result

    client.subscribe(settings.MQTT_MEAL_TOPIC)


def on_meal(client, userdata, message):
    del client
    del userdata

    message_string = str(message.payload.decode("utf-8"))
    values_strings = message_string.split(";")

    duration = int(values_strings[0])
    quantity = int(values_strings[1])

    from .models import Meal
    Meal(duration=duration, quantity=quantity).save()
