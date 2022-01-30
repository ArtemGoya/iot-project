import paho.mqtt.client as mqtt
import time
import database

# The broker name or IP address.
broker = "localhost"

# The MQTT client.
client = mqtt.Client()

def process_message(client, userdata, message):

    # Decode message.
    # database.save_measure(message)
    database.save_measure(str(message.payload.decode("utf-8")))
    message_decoded = (str(message.payload.decode("utf-8"))).split(",")

    # Print message to console.
    if (
        message_decoded[0] != "Client connected"
        and message_decoded[0] != "Client disconnected"
    ):
    # temp_external, hum_external, light_external, wind_external, temp_internal, hum_internal, light_internal, is_opened_windows, is_light_on
        print("Saving data: " + str(time.ctime()) + ", " + 
        str(message_decoded[0]) + "," +
        str(message_decoded[1]) + "," +
        str(message_decoded[2]) + "," +
        str(message_decoded[3]) + "," +
        str(message_decoded[4]) + "," +
        str(message_decoded[5]) + "," +
        str(message_decoded[6]) + "," +
        str(message_decoded[7]) + "," +
        str(message_decoded[8]))

        # Save to sqlite database.
    #     connention = sqlite3.connect("iot.db")
    #     cursor = connention.cursor()
    #     cursor.execute(
    #         "INSERT INTO pomiary VALUES (?,?,?,?,?,?,?,?,?)",
    #         (time.ctime(),
    #         message_decoded[0],
    #         message_decoded[1],
    #         message_decoded[2],
    #         message_decoded[3],
    #         message_decoded[4],
    #         message_decoded[5],
    #         message_decoded[6],
    #         message_decoded[7],
    #         message_decoded[8]),
    #     )
    #     connention.commit()
    #     connention.close()
    # else:
    #     print(message_decoded[0] + " : " + message_decoded[1])

def connect_to_broker():
    # Connect to the broker.
    client.connect(broker)
    # Send message about conenction.
    client.on_message = process_message
    # Starts client and subscribe.
    client.loop_start()
    client.subscribe("galery_data/+")

def disconnect_from_broker():
    # Disconnet the client.
    client.loop_stop()
    client.disconnect()

def run_receiver():
    connect_to_broker()
    # create_main_window()
    # Start to display window (It will stay here until window is displayed)
    # window.mainloop()
    # disconnect_from_broker()
