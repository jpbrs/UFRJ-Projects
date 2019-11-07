#Código para se inscrever na Cloud da IBM e receber os dados
import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("iot-2/type/UnidadeMeteorologica/id/UM1/evt/status/fmt/json")
    client.subscribe("iot-2/type/UnidadeMeteorologica/id/UM2/evt/status/fmt/json")



# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


#Id do cliente MQTT segue o padrão a:orgId:AplicationID
client = mqtt.Client(client_id="a:n7bzm3:watciy7eub")
client.on_connect = on_connect
client.on_message = on_message

#Para a aplicação o username segue o padrão a-orgID-AplicationID
username = "a-n7bzm3-watciy7eub"
#Senha é um token de autenticação criado na hora da criação da aplicação na Cloud
password = "&-Q4!d!C-3IBm_bJ2h"
client.username_pw_set(username, password=password)

#URL de conexão da Nuvem segue o Padrão OrgID.messaging.internetofthings.ibmcloud.com
client.connect("n7bzm3.messaging.internetofthings.ibmcloud.com", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()