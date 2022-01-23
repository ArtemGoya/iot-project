
"""
   Ten modol będzie udostępnia metody do komunikacji z brokerem mqtt
"""

import paho.mqtt.client as mqtt

# The gallery   ID - can be any string.
GALLERY_ID = "1"


# The MQTT client.
client = mqtt.Client()

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
