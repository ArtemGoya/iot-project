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

def send_data_to_server(temp_external, humidity_external, lighting_external, wind_external, temp_internal, humidity_internal, lighting_internal):
   client.publish(
        "data_reader/",
        temp_external + "," + 
        humidity_external + "," + 
        lighting_external + "," + 
        wind_external + "," + 
        temp_internal + "," + 
        humidity_internal + "," + 
        lighting_internal)
