import paho.mqtt.client as mqtt
import time
import random
import json

username = "use-token-auth"
password = "coloque o token aqui"
topic = "iot-2/evt/status/fmt/json"

client = mqtt.Client(client_id="d:orgId:DeviceType:DeviceID")
client.username_pw_set(username, password=password)

client.connect("orgID.messaging.internetofthings.ibmcloud.com", 1883, 60)

while True:
	bpm = random.randint(60,80)
	bpmstr = str(bpm)
	payload = "{\"d\":{\"BPM\":\"" + bpmstr + "\"}}";

	client.publish(topic, payload=payload, qos=0, retain=False)
	time.sleep(2)
