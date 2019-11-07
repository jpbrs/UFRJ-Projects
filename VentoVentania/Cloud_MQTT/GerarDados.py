from Cloud_MQTT import SimuladorDados
import threading
import random

#Cria um nó virtual para simular uma unidade meteorológica que produzirá os dados
def simular(vento, umidade, temperatura, local, numero, escala):
    um = SimuladorDados.simulador_UM(vento, temperatura, umidade, local, numero, escala)
    um.main()


n = 3 #Numero de threads/conexões com a cloud, maximo suportado é 30
for i in range(1,n):

    vento = random.randint(0,80)
    umidade = random.randint(50,70)
    temperatura = random.randint(20,40)
    local = "Local {}".format(i)
    numero = str(i)

    t = threading.Thread(target=simular,args=(vento,umidade,temperatura,local,numero,1))
    t.start()





#
# um01 = SimuladorDados.simulador_UM(50, 40, 50, "Cidade Universitaria", "01",1)
# um01.main()