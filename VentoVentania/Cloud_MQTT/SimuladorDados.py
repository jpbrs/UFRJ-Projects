import paho.mqtt.client as mqtt
import time
import json
import random
from datetime import date


class simulador_UM:

    def __init__(self, velocidade_media : int, temperatura_media : int, umidade_media : int, localidade : str, numero : str, scale : int):
        #Dados a serem simulados e enviados à Cloud da IBM
        self.velocidade_media = velocidade_media
        self.temperatura_media = temperatura_media
        self.umidade_media = umidade_media
        self.localidade = localidade
        self.numero = numero

        #######################################################################################################
        self.username = "use-token-auth" #usuário padrão para autenticação de devices na IBM Cloud
        self.password = "ventoventania"+self.numero #Senha registrada na cloud
        self.topic = "iot-2/evt/status/fmt/json" #Tópico obrigatório para publicações, único parâmetro mutável é "status"
        self.org_id = "n7bzm3" #número de reconhecimento único para a Cloud

        #Client ID segue padrão abaixo, sendo UnidadeMeteorologica o Device Type e UM# o device ID
        self.client = mqtt.Client(client_id="d:{}:UnidadeMeteorologica:UM{}".format(self.org_id, self.numero))
        self.client.username_pw_set(self.username, password=self.password)

        #######################################################################################################

        self.scale = scale # 1 para 1 segundo e 60 para 1 minuto
        self.time_interval = 15
        self.blow_interval = 0.5



    def get_velocidade(self):
        return (random.randint(self.velocidade_media - 5, self.velocidade_media + 5))

    def get_temperatura(self):
        return (random.randint(self.temperatura_media-1, self.temperatura_media+1))

    def get_umidade(self):
        return (random.randint(self.umidade_media-1, self.umidade_media+1))

    def get_classificacao(self, vento):
        if(vento >= 0 and vento<=18.5):
            return "Vento Fraco"
        elif(vento<= 51.9):
            return "Vento Moderado"
        elif(vento<=76):
            return "Vento Forte"
        elif(vento <=120):
            return "Vento Muito Forte"
        else:
            return "Erro de Classificação"

    def mqtt_connect(self):
        self.client.connect("{}.messaging.internetofthings.ibmcloud.com".format(self.org_id), 1883)


    def generate_payload(self, vento, umidade, temperatura, rajada, classificacao):
        data = str(date.today())
        hora = time.strftime('%X')
        payload = {"d": {"Localidade":self.localidade, "Data":data, "Hora": hora, "Velocidade do Vento": vento, "Rajada" : rajada,"Classificacao": classificacao, "Umidade": umidade, "Temperatura":temperatura }}
        payload = json.dumps(payload)
        return payload



    def main(self):
        while True:
            times = int(self.time_interval/self.blow_interval) #Vezes que irá colher os dados no intervalo de tempo entre envio
            velocidade = 0
            rajada = 0
            for i in range(1,times+1):

                velocidade = self.get_velocidade()
                rajada = max(velocidade, rajada)

                time.sleep(self.blow_interval*self.scale)

            umidade = self.get_umidade()
            temperatura = self.get_temperatura()
            classificacao = self.get_classificacao(velocidade)
            payload = self.generate_payload(velocidade, umidade, temperatura, rajada, classificacao)

            #Nova conexão a cada envio, visto que o tempo de conexão é 60 segundos
            self.mqtt_connect()
            self.client.publish(self.topic, payload=payload, qos=2, retain=False)
            print("Published : {}".format(payload))











