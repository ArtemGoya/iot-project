"""
   Ten modol będzie udostępnia metody do komunikacji z brokerem mqtt
"""

import paho.mqtt.client as mqtt

# The gallery   ID - can be any string.
GALLERY_ID = "1"
# The broker name or IP address.
broker = "localhost"


# The MQTT client.
client = mqtt.Client()


def call_worker(worker_name):
    client.publish(
        "worker/name",
        worker_name + "." + GALLERY_ID,
    )


def connect_to_broker():
    # Connect to the broker.
    client.connect(broker)
    # Send message about conenction.
    call_worker("Client connected")


def send_data_to_server(temp_external, hum_external, light_external, wind_external, temp_internal, hum_internal, light_internal, is_opened_windows, is_light_on):
    client.publish(
        "galery_data/" + str(GALLERY_ID),
        str(temp_external) + "," +
        str(hum_external) + "," +
        str(light_external) + "," +
        str(wind_external) + "," +
        str(temp_internal) + "," +
        str(hum_internal) + "," +
        str(light_internal) + "," +
        str(is_opened_windows) + "," +
        str(is_light_on))
