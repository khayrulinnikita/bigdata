import paho.mqtt.client as mqtt
import time
from json import dumps, loads
from kafka import KafkaProducer


username = 'Hans'
password = 'Test'

mqtt_client = mqtt.Client("BridgeMQTT2Kafka")
mqtt_client.username_pw_set(username, password=password)
mqtt_client.connect(host='194.67.112.161', port=1883)


producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

def on_message(client, userdata, message):
    msg_payload = loads(message.payload.decode('utf-8'))
    print("Received MQTT message: ", msg_payload)
    print(type(msg_payload))
    producer.send('v14', value=msg_payload)
    print("published to v14:", msg_payload)

mqtt_client.loop_start()
mqtt_client.subscribe("v14")
mqtt_client.on_message = on_message
time.sleep(300)
mqtt_client.loop_stop()
