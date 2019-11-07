#Simulador simples para simular um dispositivo apenas, seu uso é desnecssário
#Melhor uso seria pela classe SimuladorDados

import paho.mqtt.client as mqtt
import time
import json
import random

numero = "01"
username = "use-token-auth"
password = "ventoventania01"
topic = "iot-2/evt/status/fmt/json"
org_id = "n7bzm3"

client = mqtt.Client(client_id="d:n7bzm3:UnidadeMeteorologica:UM01")
client.username_pw_set(username, password=password)

client.connect("n7bzm3.messaging.internetofthings.ibmcloud.com", 1883)

while True:
    print(client.is_connected())
    vento = random.randint(60,80)
    ventostr = str(vento)
    # payload = "{\"d\":{\"Velocidade\":\""+ ventostr + "\",\"umidade\":\"18\"}}"
    payload = {"d":{"Velocidade do Vento":ventostr, "umidade":"18"}}
    payload = json.dumps(payload)
    client.publish(topic, payload=payload, qos=2, retain=False)
    print(payload)
    time.sleep(5)
